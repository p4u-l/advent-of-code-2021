from collections import deque


def check_syntax(string, bracket_pairs):
    # Returns char that triggered the first syntax error (None if there
    # is no syntax error) and the remaining bracket stack
    bracket_stack = deque()
    syntax_error = None

    for char in string:
        if char in bracket_pairs.keys():  # Opening bracket
            bracket_stack.append(char)
        elif char in bracket_pairs.values():  # Closing bracket
            if char != bracket_pairs[bracket_stack.pop()]:
                syntax_error = char
                break

    return syntax_error, bracket_stack


def main():
    with open("day10/input.txt", "r", encoding="utf-8") as f:
        puzzle_input = f.read().splitlines()

    bracket_pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    corrupted_score_table = {")": 3, "]": 57, "}": 1197, ">": 25137}
    completion_score_table = {")": 1, "]": 2, "}": 3, ">": 4}

    corrupted_score = 0
    completion_scores = []

    for line in puzzle_input:
        first_syntax_err, remaining_stack = check_syntax(line, bracket_pairs)
        if first_syntax_err:
            corrupted_score += corrupted_score_table[first_syntax_err]
        else:
            # All syntax error-free lines are incomplete, according to
            # the description. The stack of opening brackets left over
            # from the previous syntax check is used for autocompletion.
            cs = 0
            while remaining_stack:
                matching_bracket = bracket_pairs[remaining_stack.pop()]
                cs = cs * 5 + completion_score_table[matching_bracket]
            completion_scores.append(cs)

    print("Part 1:", corrupted_score)
    print("Part 2:", sorted(completion_scores)[len(completion_scores)//2])


if __name__ == "__main__":
    main()
