import re


# The code is written for my particular input.
# It may not work for other inputs or for general cases

with open("day17/input.txt", "r", encoding="utf-8") as f:
    puzzle_input = f.read()

target = tuple(map(int, re.findall(r"-?\d+", puzzle_input)))


def simulate(initial_velocity, target):
    initial_vx, initial_vy = initial_velocity
    tgt_xmin, tgt_xmax, tgt_ymin, tgt_ymax = target
    x = y = 0
    vx, vy = initial_vx, initial_vy
    while True:
        x += vx
        y += vy
        vy -= 1
        if vx < 0:
            vx += 1
        elif vx > 0:
            vx -= 1
        if x >= tgt_xmin and x <= tgt_xmax and y >= tgt_ymin and y <= tgt_ymax:
            return True
        if x > tgt_xmax or y < tgt_ymin:
            break
    return False


hits_target_sum = 0
for vx in range(1, target[1] + 1):
    for vy in range(target[2], 1000):  # vy upper bound was estimated
        if simulate((vx, vy), target):
            hits_target_sum += 1

print(hits_target_sum)