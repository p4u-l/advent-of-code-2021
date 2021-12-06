from collections import deque

with open("day06/input.txt", "r", encoding="utf-8") as f:
    initial_lanternfish = [int(i) for i in f.read().split(",")]

def simulate_population(initial: list[int], days: int) -> int:
    fish_count = deque(initial.count(x) for x in range(9))
    for _ in range(days):
        # Shift deque to the left, remembering the leftmost element
        new_fish = fish_count.popleft()
        fish_count.append(new_fish)
        # Reset timer of the fish with a timer of 0 to 6
        fish_count[6] += new_fish
    return sum(fish_count)

print("Part 1:", simulate_population(initial_lanternfish, 80))
print("Part 2:", simulate_population(initial_lanternfish, 256))
