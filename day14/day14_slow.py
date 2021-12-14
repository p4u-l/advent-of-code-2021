from collections import Counter

with open("day14/input.txt", "r", encoding="utf-8") as f:
    puzzle_input = f.read()

polymer, rule_strings = puzzle_input.split("\n\n")

rules = {}
for rule in rule_strings.split("\n"):
    k, v = rule.split(" -> ")
    rules[k] = v


def steps(poly, n):
    for _ in range(n):
        to_insert = [rules[poly[x] + poly[x+1]] for x in range(len(poly) - 1)]
        poly = "".join([a + b for a, b in zip(poly, to_insert)] + [poly[-1]])
    return poly


counter = Counter(steps(polymer, 10))
print(counter.most_common()[0][1] - counter.most_common()[-1][1])