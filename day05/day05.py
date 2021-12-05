import re
from collections import defaultdict
from PIL import Image
from matplotlib import cm

with open("day05/input.txt", "r", encoding="utf-8") as f:
    puzzle_input = f.readlines()


def visualize(point_dict: dict) -> Image:
    max_overlap = max(point_dict.values())
    colormap = cm.get_cmap("viridis", max_overlap + 1)
    img = Image.new("RGB", (1000, 1000), (0, 0, 0))
    pixels = img.load()
    for point, overlaps in point_dict.items():
        x, y = point
        r, g, b = (int(colormap(overlaps)[i] * 255) for i in range(3))
        pixels[x, y] = (r, g, b)
    return img


def smart_range(i: int, j: int) -> range:
    # inclusive range functions that works in both directions, e.g.:
    # i=2, j=4 => 2, 3, 4
    # i=4, j=2 => 4, 3, 2.
    if i <= j:
        return range(i, j+1)
    else:
        return range(i, j-1, -1)


def solve(lines_str: list[str], diagonals=False, save_vis=False) -> int:
    covered_points = defaultdict(int)
    for line_str in lines_str:
        x1, y1, x2, y2 = (int(i) for i in re.findall(r"[0-9]+", line_str))
        x_range = smart_range(x1, x2)
        y_range = smart_range(y1, y2)
        if x1 == x2 or y1 == y2:
            for x in x_range:
                for y in y_range:
                    covered_points[(x, y)] += 1
        elif diagonals:
            for point in zip(x_range, y_range):
                covered_points[point] += 1

    if save_vis:
        # Saves visualization of the solution.
        # Not needed for the solution.
        visualize(covered_points).save("day05/vis.png")
    
    return sum(1 for n in covered_points.values() if n >= 2)


print("Part 1:", solve(puzzle_input))
print("Part 2:", solve(puzzle_input, diagonals=True))
# print("Part 2:", solve(puzzle_input, diagonals=True, save_vis=True))