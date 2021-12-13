with open("day13/input.txt", "r", encoding="utf-8") as f:
    puzzle_input = f.read()

Coord = tuple[int, int]


def fold(dots: set[Coord], axis: str, line: int) -> set[Coord]:
    dots_new = set()
    for dot in dots:
        x, y = dot
        if axis == "y":
            if y < line:
                dots_new.add(dot)
            else:
                dots_new.add((x, 2*line - y))  # = line - (y - line)
        elif axis == "x":
            if x < line:
                dots_new.add(dot)
            else:
                dots_new.add((2*line - x, y))  # = line - (x - line)
    return dots_new


def dots_to_str(dots: set[Coord]) -> str:
    len_x = max(c[0] for c in dots) + 1
    len_y = max(c[1] for c in dots) + 1
    arr_2d = [len_x * ["\u2591"] for _ in range(len_y)]
    for x, y in dots:
        arr_2d[y][x] = "\u2588"
    return "\n".join("".join(line) for line in arr_2d)


def solve():
    dots_str, instructions_str = puzzle_input.split("\n\n")
    dots = set([tuple(map(int, d.split(","))) for d in dots_str.split("\n")])

    instructions = []
    for instr_str in instructions_str.splitlines():
        axis, line_str = instr_str.split(" ")[-1].split("=")
        instructions.append((axis, int(line_str)))

    dots = fold(dots, *instructions[0])
    print("Part 1:", len(dots))
    for instruction in instructions[1:]:
        dots = fold(dots, *instruction)
    print(f"Part 2:\n{dots_to_str(dots)}")


if __name__ == "__main__":
    solve()
