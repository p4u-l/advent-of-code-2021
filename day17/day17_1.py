import re


# The code is written for my particular input.
# It may not work for other inputs or for general cases

with open("day17/input.txt", "r", encoding="utf-8") as f:
    puzzle_input = f.read()


target_numbers = re.findall(r"-?\d+", puzzle_input)
target_xmin, target_xmax, target_ymin, target_ymax = map(int, target_numbers)


def find_highest_vy(max_vy=1000):  # max_vy was estimated
    highest_vy = 0
    for initial_vy in range(1, max_vy + 1):
        vy = initial_vy
        y = 0
        while y > target_ymin:
            y += vy
            vy -= 1
            if y >= target_ymin and y <= target_ymax:
                highest_vy = max(highest_vy, initial_vy)
                continue
    return highest_vy


def max_height(vy):
    y = 0
    max_height = 0
    while y >= max_height:
        y += vy
        vy -= 1
        max_height = max(max_height, y)
    return max_height


print(max_height(find_highest_vy()))