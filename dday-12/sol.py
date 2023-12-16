from pprint import pprint
import re
from functools import lru_cache


def read_file(filename):
    buffer = []
    with open(filename) as f:
        line = f.readline()
        while line:
            buffer.append(line.strip())
            line = f.readline()

    return buffer


def separate_board_numbers(input_string):
    pattern = r"(.*)\s(.*)"
    match = re.match(pattern, input_string)

    if match:
        board = [i for i in match.group(1)]
        numbers = list(map(int, match.group(2).split(",")))
        return board, numbers


def determine_if_valid(cur_board, counts):
    actual_counts = []

    acc = 0
    for elem in cur_board:
        if elem == "#":
            acc += 1
        else:
            if acc != 0:
                actual_counts.append(acc)
                acc = 0

    if acc != 0:
        actual_counts.append(acc)

    return 1 if actual_counts == counts else 0


def get_count(board, counts):
    @lru_cache
    def get_all_possible_boards_combinations(cur_board, idx):
        if idx >= len(cur_board):
            return determine_if_valid(cur_board, counts)

        cur_board = tuple(cur_board)
        ans = 0
        if cur_board[idx] == "?":
            cur_board[idx] = "#"
            ans += get_all_possible_boards_combinations(tuple(cur_board), idx + 1)

            cur_board[idx] = "."
            ans += get_all_possible_boards_combinations(tuple(cur_board), idx + 1)
        else:
            ans += get_all_possible_boards_combinations(tuple(cur_board), idx + 1)

        return ans

    return get_all_possible_boards_combinations(tuple(board), 0)


def solution(filename):
    lines = read_file(filename)
    boards = [separate_board_numbers(line) for line in lines]

    ans = 0
    for board, counts in boards:
        print(board, counts)
        ans += get_count(board, counts)
    return ans


if __name__ == "__main__":
    small = "input_small.txt"
    large = "input_large.txt"

    # print(solution(small))
    print(solution(large))
