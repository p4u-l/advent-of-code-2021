with open("day01/input.txt", "r", encoding="utf-8") as f:
    puzzle_input = f.read().splitlines()

heights = [int(number_str) for number_str in puzzle_input]

measurement_window = heights[:3]
previous_sum = sum(measurement_window)
increased_count = 0

for height in heights[len(measurement_window):]:
    measurement_window.pop(0)
    measurement_window.append(height)
    measurement_window_sum = sum(measurement_window)
    if measurement_window_sum > previous_sum:
        increased_count += 1
    previous_sum = measurement_window_sum

print(increased_count)
