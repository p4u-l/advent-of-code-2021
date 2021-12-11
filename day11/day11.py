from typing import Iterator
from collections import deque
from PIL import Image
from matplotlib import cm

Coord = tuple[int, int]


class OctupusMap:
    def __init__(self, octupus_map_str: str, flash_level: int = 10):
        self.octupus_arr = [[int(x) for x in line] for line in octupus_map_str]
        self.max_y = len(self.octupus_arr) - 1
        self.max_x = len(self.octupus_arr[0]) - 1
        self.size = (self.max_y + 1) * (self.max_x + 1)
        self.flash_level = flash_level

    def __str__(self) -> str:
        out_str = ""
        for row in self.octupus_arr:
            out_str += "".join(map(str, row)) + "\n"
        return out_str

    def __len__(self) -> int:
        return self.size
    
    def __getitem__(self, coords: Coord) -> int:
        x, y = coords
        return self.octupus_arr[y][x]

    def __setitem__(self, coords: Coord, value: int):
        x, y = coords
        self.octupus_arr[y][x] = value

    def __iter__(self) -> Iterator[Coord]:
        for y in range(self.max_y + 1):
            for x in range(self.max_x + 1):
                yield (x, y)

    def adj_coords(self, coords: Coord) -> list[Coord]:
        x, y = coords
        adjacent = []
        for ax in range(max(x-1, 0), min(x+1, self.max_x) + 1):
            for ay in range(max(y-1, 0), min(y+1, self.max_y) + 1):
                if ax == x and ay == y:
                    continue
                adjacent.append((ax, ay))
        return adjacent
    
    def __increase_all(self) -> list[Coord]:
        flashed_list = []
        for coords in self:
            new_value = (self[coords] + 1) % self.flash_level
            if new_value == 0:
                flashed_list.append(coords)
            self[coords] = new_value
        return flashed_list

    def generate_image(self, upscale: int = 32) -> Image:
        cmap = cm.get_cmap("plasma", self.flash_level)
        colors = [
            tuple(int(c * 255) for c in cmap(i)[:3])
            for i in range(self.flash_level)
        ]
        img = Image.new("RGB", (self.max_x + 1, self.max_y + 1), (0, 0, 0))
        pixels = img.load()
        for x, y in self:
            value = self[(x, y)]
            if value == 0:
                pixels[x, y] = (255, 255, 255)
            else:
                pixels[x, y] = colors[value]
        img_resized = img.resize(
            ((self.max_x+1) * upscale, (self.max_y+1) * upscale),
            Image.NEAREST
        )
        return img_resized

    def step(self) -> set:
        flash_queue = deque(self.__increase_all())
        already_flashed = set(flash_queue)
        while flash_queue:
            flashed = flash_queue.pop()
            for adj in self.adj_coords(flashed):
                if adj in already_flashed:
                    continue
                new_value = (self[adj] + 1) % self.flash_level
                if new_value == 0:
                    already_flashed.add(adj)
                    flash_queue.appendleft(adj)
                self[adj] = new_value
        return already_flashed


def solve(save_vis_frames=False):
    with open("day11/input.txt", "r", encoding="utf-8") as f:
        puzzle_input = f.read().splitlines()

    octupus_map = OctupusMap(puzzle_input)

    flash_count = 0
    sync_step = -1
    step = 0

    if save_vis_frames:
        frames = []

    while sync_step == -1 or step < 100:
        flashed = octupus_map.step()
        if step < 100:
            flash_count += len(flashed)
        if len(flashed) == len(octupus_map):
            sync_step = step
        step += 1

        if save_vis_frames:
            frames.append(octupus_map.generate_image())

    print("Part 1:", flash_count)
    print("Part 2:", sync_step + 1)

    if save_vis_frames:
        for i in range(len(frames)):
            frames[i].save(f"day11/frames/frame{i:03}.png")


if __name__ == "__main__":
    solve(save_vis_frames=False)
