from pprint import pprint
from collections import deque


def read_file(filename):
    lines = [line.strip() for line in open(filename)]
    board = []
    for line in lines:
        board.append([i for i in line])
    return board


def is_valid(x, y, rows, cols):
    return x >= 0 and x < rows and y >= 0 and y < cols


def solve(board):
    rows, cols = len(board), len(board[0])
    ans = []
    # first top and bottom rows
    for c in range(cols):
        ans.append(solve_with_starting_coord_and_dir(board, 0, c, "down"))
        ans.append(solve_with_starting_coord_and_dir(board, rows - 1, c, "up"))

    # then left and right columns
    for r in range(rows):
        ans.append(solve_with_starting_coord_and_dir(board, r, 0, "right"))
        ans.append(solve_with_starting_coord_and_dir(board, r, cols - 1, "left"))

    print(ans)
    return max(ans)


def solve_with_starting_coord_and_dir(board, start_x, start_y, dir):
    rows, cols = len(board), len(board[0])
    new_board = []
    for i in range(rows):
        new_board.append(["." for i in range(cols)])

    visited = set()
    where_light_is = set()
    queue = deque()
    queue.appendleft(((start_x, start_y), dir))
    old_count = 0

    while len(queue) > 0:
        (x, y), dir = queue.pop()

        if is_valid(x, y, rows, cols) and ((x, y), dir) not in visited:
            new_board[x][y] = "#"
            if board[x][y] == ".":
                if dir == "left":
                    queue.appendleft([(x, y - 1), "left"])
                if dir == "right":
                    queue.appendleft([(x, y + 1), "right"])
                if dir == "up":
                    queue.appendleft([(x - 1, y), "up"])
                if dir == "down":
                    queue.appendleft([(x + 1, y), "down"])

            elif board[x][y] == "-":
                if dir in ["left", "right"]:
                    if dir == "left":
                        queue.appendleft([(x, y - 1), "left"])
                    if dir == "right":
                        queue.appendleft([(x, y + 1), "right"])
                else:
                    queue.appendleft([(x, y + 1), "right"])
                    queue.appendleft([(x, y - 1), "left"])

            elif board[x][y] == "|":
                if dir in ["up", "down"]:
                    if dir == "up":
                        queue.appendleft([(x - 1, y), "up"])
                    if dir == "down":
                        queue.appendleft([(x + 1, y), "down"])
                else:
                    queue.appendleft([(x - 1, y), "up"])
                    queue.appendleft([(x + 1, y), "down"])

            elif board[x][y] == "\\":  # same as '\'
                if dir == "up":
                    queue.appendleft([(x, y - 1), "left"])
                if dir == "down":
                    queue.appendleft([(x, y + 1), "right"])
                if dir == "left":
                    queue.appendleft([(x - 1, y), "up"])
                if dir == "right":
                    queue.appendleft([(x + 1, y), "down"])

            elif board[x][y] == "/":
                if dir == "down":
                    queue.appendleft([(x, y - 1), "left"])
                if dir == "up":
                    queue.appendleft([(x, y + 1), "right"])
                if dir == "right":
                    queue.appendleft([(x - 1, y), "up"])
                if dir == "left":
                    queue.appendleft([(x + 1, y), "down"])

            visited.add(((x, y), dir))

    ans = 0
    for r in range(rows):
        for c in range(cols):
            ans = ans + 1 if new_board[r][c] == "#" else ans
    return ans


def solution(filename):
    board = read_file(filename)

    ans = solve(board)
    return ans


if __name__ == "__main__":
    small = "input_small.txt"
    large = "input_large.txt"

    print(solution(small))
    print(solution(large))
