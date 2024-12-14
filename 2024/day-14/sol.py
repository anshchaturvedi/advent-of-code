import argparse
from collections import Counter, defaultdict, deque
import heapq
import math
import os
import numpy as np
import pprint
import re
import sys


sys.setrecursionlimit(15000000)


def get_nums(x):
    pattern = r"-?\d+"
    if isinstance(x, str):
        matches = re.findall(pattern, x)
        return list(map(int, matches))
    if isinstance(x, list):
        stringified = "".join(x)
        matches = re.findall(pattern, stringified)
        return list(map(int, matches))


def part_1_solution(file_name: str):
    input = []

    with open(file_name) as input_file:
        line = input_file.readline()
        while line:
            a = line.strip()
            input.append(a)
            line = input_file.readline()

    rows, cols = 103, 101
    input = list(map(get_nums, input))

    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for line in input:
        x_pos, y_pos = line[1], line[0]
        x_vel, y_vel = line[3], line[2]
        x_pos = (x_pos + 100 * x_vel) % rows
        y_pos = (y_pos + 100 * y_vel) % cols
        grid[x_pos][y_pos] += 1

    c1, c2, c3, c4 = 0, 0, 0, 0
    for i in range(rows // 2):
        for j in range(cols // 2):
            c1 += grid[i][j]
            c2 += grid[i][cols - 1 - j]
            c3 += grid[rows - 1 - i][j]
            c4 += grid[rows - 1 - i][cols - 1 - j]

    return c1 * c2 * c3 * c4


def part_2_solution(file_name: str):
    input = []

    with open(file_name) as input_file:
        line = input_file.readline()
        while line:
            a = line.strip()
            input.append(a)
            line = input_file.readline()

    rows, cols = 103, 101
    input = list(map(get_nums, input))

    heap = []
    for step in range(1, rows * cols):
        grid = [["." for _ in range(cols)] for _ in range(rows)]
        for line in input:
            x_pos, y_pos = line[1], line[0]
            x_vel, y_vel = line[3], line[2]
            x_pos = (x_pos + step * x_vel) % rows
            y_pos = (y_pos + step * y_vel) % cols
            grid[x_pos][y_pos] = "#"

        beside = 0
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if grid[i][j] == "#":
                    for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                        if grid[i + dx][j + dy] == "#":
                            beside += 1

        heapq.heappush(heap, (-beside, step))

    _, time = heapq.heappop(heap)

    for line in input:
        x_pos, y_pos = line[1], line[0]
        x_vel, y_vel = line[3], line[2]
        x_pos = (x_pos + time * x_vel) % rows
        y_pos = (y_pos + time * y_vel) % cols
        grid[x_pos][y_pos] = "#"

    with open("christmas_tree.txt", "w") as f:
        for row in grid:
            f.write("".join(row) + "\n")

    return time


# ---------------------------- RUN AND SUBMIT ----------------------------

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(ROOT_DIR)
from utils.aoc_utils import time_function
from utils.get_input import get_puzzle_input

parser = argparse.ArgumentParser(description="Advent of Code Solution Script")
parser.add_argument(
    "-s", "--submit", action="store_true", help="Submit the solution to Advent of Code"
)
args = parser.parse_args()

get_puzzle_input(suppress_logs=True)

# time_function(part_1_solution, "sample.txt")
time_function(args.submit, part_1_solution, "full.txt")
# time_function(part_2_solution, "sample.txt")
time_function(args.submit, part_2_solution, "full.txt")
