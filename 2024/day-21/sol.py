# from collections import Counter, defaultdict, deque
# from functools import lru_cache
# import heapq
from collections import defaultdict, deque
import itertools
import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(ROOT_DIR)
from utils.aoc_tools import time_function, nums, dir4

sys.setrecursionlimit(15000000)

num_keypad_layout = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]

dir_keypad_layout = [[None, "^", "A"], ["<", "v", ">"]]


def part_1_solution(file_name: str):
    data = [line.strip() for line in open(file_name).readlines()]

    from collections import deque
    from itertools import product

    def map_keypad_positions(keypad):
        positions = {}
        for row_index, row in enumerate(keypad):
            for col_index, key in enumerate(row):
                if key is not None:
                    positions[key] = (row_index, col_index)
        return positions

    def generate_sequences(keypad):
        positions = map_keypad_positions(keypad)
        sequences = {}

        for start_key, start_pos in positions.items():
            for end_key, end_pos in positions.items():
                if start_key == end_key:
                    sequences[(start_key, end_key)] = ["A"]
                    continue

                queue = deque([(start_pos, "")])
                shortest_length = float("inf")
                valid_sequences = []

                while queue:
                    (row, col), path = queue.popleft()

                    for dr, dc, move in [
                        (-1, 0, "^"),
                        (1, 0, "v"),
                        (0, -1, "<"),
                        (0, 1, ">"),
                    ]:
                        new_row, new_col = row + dr, col + dc

                        if not (
                            0 <= new_row < len(keypad) and 0 <= new_col < len(keypad[0])
                        ):
                            continue

                        next_key = keypad[new_row][new_col]
                        if next_key is None:
                            continue

                        if next_key == end_key:
                            if len(path) + 1 > shortest_length:
                                break
                            shortest_length = len(path) + 1
                            valid_sequences.append(path + move + "A")
                        else:
                            queue.append(((new_row, new_col), path + move))
                    else:
                        continue
                    break

                sequences[(start_key, end_key)] = valid_sequences

        return sequences

    def calculate_possible_paths(input_string, sequences):
        path_options = [
            sequences[(x, y)] for x, y in zip("A" + input_string, input_string)
        ]
        return ["".join(combination) for combination in product(*path_options)]

    num_sequences = generate_sequences(num_keypad_layout)
    dir_sequences = generate_sequences(dir_keypad_layout)
    total_distance = 0

    for input_line in data:
        initial_paths = calculate_possible_paths(input_line, num_sequences)
        current_paths = initial_paths

        for _ in range(2):
            next_paths = []
            for path in current_paths:
                next_paths.extend(calculate_possible_paths(path, dir_sequences))
            min_length = min(map(len, next_paths))
            current_paths = [path for path in next_paths if len(path) == min_length]

        total_distance += len(current_paths[0]) * int(input_line[:-1])

    return total_distance


def part_2_solution(file_name: str):
    data = [line.strip() for line in open(file_name).readlines()]

    from functools import cache
    from itertools import product

    def map_keypad_positions(keypad):
        positions = {}
        for row_index, row in enumerate(keypad):
            for col_index, key in enumerate(row):
                if key is not None:
                    positions[key] = (row_index, col_index)
        return positions

    def generate_sequences(keypad):
        positions = map_keypad_positions(keypad)
        sequences = {}

        for start_key, start_pos in positions.items():
            for end_key, end_pos in positions.items():
                if start_key == end_key:
                    sequences[(start_key, end_key)] = ["A"]
                    continue

                queue = deque([(start_pos, "")])
                shortest_length = float("inf")
                valid_sequences = []

                while queue:
                    (row, col), path = queue.popleft()

                    for dr, dc, move in [
                        (-1, 0, "^"),
                        (1, 0, "v"),
                        (0, -1, "<"),
                        (0, 1, ">"),
                    ]:
                        new_row, new_col = row + dr, col + dc

                        if not (
                            0 <= new_row < len(keypad) and 0 <= new_col < len(keypad[0])
                        ):
                            continue

                        next_key = keypad[new_row][new_col]
                        if next_key is None:
                            continue

                        if next_key == end_key:
                            if len(path) + 1 > shortest_length:
                                break
                            shortest_length = len(path) + 1
                            valid_sequences.append(path + move + "A")
                        else:
                            queue.append(((new_row, new_col), path + move))
                    else:
                        continue
                    break

                sequences[(start_key, end_key)] = valid_sequences

        return sequences

    def calculate_possible_paths(input_string, sequences):
        path_options = [
            sequences[(x, y)] for x, y in zip("A" + input_string, input_string)
        ]
        return ["".join(combination) for combination in product(*path_options)]

    num_sequences = generate_sequences(num_keypad_layout)
    dir_sequences = generate_sequences(dir_keypad_layout)
    sequence_lengths = {pair: len(paths[0]) for pair, paths in dir_sequences.items()}

    @cache
    def compute_min_length(sequence, depth=25):
        if depth == 1:
            return sum(
                sequence_lengths[(x, y)] for x, y in zip("A" + sequence, sequence)
            )

        total_length = 0
        for x, y in zip("A" + sequence, sequence):
            total_length += min(
                compute_min_length(sub_sequence, depth - 1)
                for sub_sequence in dir_sequences[(x, y)]
            )

        return total_length

    total_distance = 0

    for input_line in data:
        initial_paths = calculate_possible_paths(input_line, num_sequences)
        shortest_length = min(map(compute_min_length, initial_paths))
        total_distance += shortest_length * int(input_line[:-1])

    return total_distance


# ---------------------------- SUBMIT ----------------------------

time_function(part_1_solution, "sample.txt")  # 1972
time_function(part_1_solution, "full.txt")  # 138764
time_function(part_2_solution, "sample.txt")  # 2379451789590
time_function(part_2_solution, "full.txt")  # 169137886514152
