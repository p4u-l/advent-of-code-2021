from collections import Counter


def pairs_from_str(string):
    # generates all pairs in string, e.g. NNCB -> NN, NC, CB
    return [x + y for x, y in zip(string, string[1:])]


def solve(polymer, rules, n):
    # pairs             letters
    # (NNCB:)           NNCB
    # NN -> NC, CN      +C
    # NC -> NB, BC      +B
    # CB -> CH, HB      +H

    # (NCNBCHB:)
    # NC -> NB, BC      +B
    # CN -> CC, CN      +C
    # NB -> ...         +...
    # BC
    # CH
    # HB

    pair_counter = Counter(pairs_from_str(polymer))
    letter_counter = Counter(polymer)

    for _ in range(n):
        for key, count in list(pair_counter.items()):
            pair_counter[key] -= count
            to_insert = rules[key]
            letter_counter[to_insert] += count
            pair_counter[key[0] + to_insert] += count
            pair_counter[to_insert + key[1]] += count

    most_common_value = letter_counter.most_common()[0][1]
    least_common_value = letter_counter.most_common()[-1][1]
    
    return most_common_value - least_common_value


def main():
    with open("day14/input.txt", "r", encoding="utf-8") as f:
        puzzle_input = f.read()

    template, rule_strings = puzzle_input.split("\n\n")
    
    rules = {}
    for rule in rule_strings.split("\n"):
        k, v = rule.split(" -> ")
        rules[k] = v

    print("Part 1:", solve(template, rules, 10))
    print("Part 2:", solve(template, rules, 40))


if __name__ == "__main__":
    main()
