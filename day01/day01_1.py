with open("day01/input.txt", "r", encoding="utf-8") as f:
    puzzle_input = f.read().splitlines()

heights = [int(number_str) for number_str in puzzle_input]

increased_count = 0
previous_height = heights[0]
for height in heights[1:]:
    if height > previous_height:
        increased_count += 1
    previous_height = height

print(increased_count)
