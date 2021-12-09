from collections import deque
from typing import Iterator
from math import prod
from PIL import Image
from matplotlib import cm

Coord = tuple[int, int]


class Heightmap:
    def __init__(self, heightmap_str: str):
        self.heightmap_arr = [[int(x) for x in line] for line in heightmap_str]
        self.max_y = len(self.heightmap_arr) - 1
        self.max_x = len(self.heightmap_arr[0]) - 1

    def __getitem__(self, coords: Coord) -> int:
        x, y = coords
        return self.heightmap_arr[y][x]

    def __iter__(self) -> Iterator[Coord]:
        for y in range(self.max_y + 1):
            for x in range(self.max_x + 1):
                yield (x, y)

    def adjacent_coords(self, coords: Coord) -> list[Coord]:
        x, y = coords
        adjacent = []
        if x > 0:
            adjacent.append((x - 1, y))
        if x < self.max_x:
            adjacent.append((x + 1, y))
        if y > 0:
            adjacent.append((x, y - 1))
        if y < self.max_y:
            adjacent.append((x, y + 1))
        return adjacent

    def save_image(self, path: str):
        cmap = cm.get_cmap("magma", 10)
        colors = [tuple(int(c * 255) for c in cmap(i)[:3]) for i in range(10)]
        img = Image.new("RGB", (self.max_x + 1, self.max_y + 1), (0, 0, 0))
        pixels = img.load()
        for x, y in self:
            height = self[(x, y)]
            if height == 9:
                pixels[x, y] = colors[0]
            else:
                pixels[x, y] = colors[9-height]
        img.save(path)


def fill_basin(heightmap: Heightmap, start: int, visited: set) -> int:
    # find basin size using breadth-first search
    basin_size = 0
    visit_queue = deque([start])
    while visit_queue:
        basin = visit_queue.pop()
        adj_basins = heightmap.adjacent_coords(basin)
        for basin_edge in adj_basins:
            if basin_edge not in visited and heightmap[basin_edge] != 9:
                visited.add(basin_edge)
                visit_queue.appendleft(basin_edge)
                basin_size += 1
    return basin_size


def main():
    with open("day09/input.txt", "r", encoding="utf-8") as f:
        puzzle_input = f.read().splitlines()

    heightmap = Heightmap(puzzle_input)
    low_points = []
    risk_level_sum = 0
    for coords in heightmap:
        height = heightmap[coords]
        adj_heights = (heightmap[a] for a in heightmap.adjacent_coords(coords))
        if all(height < adj_h for adj_h in adj_heights):
            low_points.append(coords)
            risk_level_sum += 1 + height

    print("Part 1:", risk_level_sum)

    visited = set()
    basin_sizes = [fill_basin(heightmap, lp, visited) for lp in low_points]

    print("Part 2:", prod(sorted(basin_sizes)[-3:]))

    # heightmap.save_image("day09/images/vis.png")


if __name__ == "__main__":
    main()
