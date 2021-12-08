with open("day08/input.txt", "r", encoding="utf-8") as f:
    puzzle_input = f.read().splitlines()

sum_unique_output = 0
for entry in puzzle_input:
    output_values_str = entry.split(" | ")[1]
    output_values = output_values_str.split(" ")
    sum_unique_output += len([x for x in output_values if len(x) in (2, 3, 4, 7)])

print(sum_unique_output)