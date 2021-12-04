with open("day04/input.txt", "r", encoding="utf-8") as f:
    puzzle_in = f.read()

order_input = [int(n) for n in puzzle_in.split("\n\n")[0].split(",")]
board_input = [
    [[int(n) for n in line.strip().split()] for line in board_str.split("\n")]
    for board_str in puzzle_in.split("\n\n")[1:]
]

Board = list[list[int]]


def check_board(board: Board, drawn_numbers: set[int]) -> bool:
    # Looks for a win in a row.
    for row in board:
        if all(field in drawn_numbers for field in row):
            return True

    # Looks for a win in a column.
    for x in range(len(board[0])):
        if all(field[x] in drawn_numbers for field in board):
            return True

    return False


def rate_board(board: Board, drawn_numbers: set[int], last_drawn: int) -> int:
    sum_unmarked = 0
    for row in board:
        for field in row:
            if field not in drawn_numbers:
                sum_unmarked += field
    return sum_unmarked * last_drawn


def solve(boards: list[Board], order: list[int]):
    boards_that_won = set()
    # Starting with 4 drawn numbers,
    # because it is not possible to win with less.
    for i in range(4, len(order)):
        # Save drawn numbers of this round as a set,
        # for performance reasons.
        drawn_numbers = set(order[:i+1])
        last_drawn = order[i]
        for board_num, board in enumerate(boards):
            if board_num in boards_that_won:
                continue
            if check_board(board, drawn_numbers):
                boards_that_won.add(board_num)
                # Part 1: If the number of boards that have won is 1,
                # a board has won for the first time.
                if len(boards_that_won) == 1:
                    board_rating = rate_board(board, drawn_numbers, last_drawn)
                    print("Part 1:", board_rating)
                # Part 2: If the number of boards that have won is equal
                # to the number of boards, the last board has won.
                if len(boards_that_won) == len(boards):
                    board_rating = rate_board(board, drawn_numbers, last_drawn)
                    print("Part 2:", board_rating)
                    return


solve(board_input, order_input)
