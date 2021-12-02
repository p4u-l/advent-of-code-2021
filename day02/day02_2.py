with open("day02/input.txt", "r", encoding="utf-8") as f:
    puzzle_input = f.read().splitlines()

instructions = [line.split() for line in puzzle_input]

horizontal_pos = 0
depth = 0
aim = 0

for instruction in instructions:
    operation = instruction[0]
    amount = int(instruction[1])
    if operation == "forward":
        horizontal_pos += amount
        depth += aim * amount
    elif operation == "down":
        aim += amount
    elif operation == "up":
        aim -= amount
    
print(horizontal_pos * depth)