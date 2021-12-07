with open("day07/input.txt", "r", encoding="utf-8") as f:
    puzzle_input = f.read()

crab_positions = [int(x) for x in puzzle_input.split(",")]

def little_gauss(n: int) -> int:
    return (n * (n + 1)) // 2

costs = []

for pos in range(min(crab_positions), max(crab_positions) + 1):
    costs.append(sum(little_gauss(abs(cpos - pos)) for cpos in crab_positions))

print(min(costs))