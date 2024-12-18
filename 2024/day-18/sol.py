import argparse
from collections import Counter, defaultdict, deque
import heapq
import math
import os
from time import sleep
import time
import numpy as np
import pprint
import re
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(ROOT_DIR)
from utils.aoc_tools import time_function, nums

sys.setrecursionlimit(15000000)


def part_1_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input]

    rows, cols = 71, 71
    # rows, cols = 7, 7
    grid = [["." for _ in range(cols)] for _ in range(rows)]

    for point in input[:1024]:
        py, px = list(map(int, point.split(",")))
        grid[px][py] = "#"

    queue = deque()
    queue.appendleft((0, 0, 0))  # i, j, dist
    visited = set()
    while queue:
        i, j, dist = queue.pop()
        if i == rows - 1 and j == cols - 1:
            return dist

        visited.add((i, j))

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = i + dx, j + dy
            if (
                new_x in range(rows)
                and new_y in range(cols)
                and (new_x, new_y) not in visited
                and grid[new_x][new_y] != "#"
            ):
                queue.appendleft((new_x, new_y, dist + 1))


def part_2_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input]

    rows, cols = 71, 71
    # rows, cols = 7, 7

    def simulate(x):
        grid = [["." for _ in range(cols)] for _ in range(rows)]

        for point in input[:x]:
            py, px = list(map(int, point.split(",")))
            grid[px][py] = "#"

        queue = deque()
        visited = set()

        queue.appendleft((0, 0, 0))  # i, j, dist
        visited.add((0, 0))

        while queue:
            i, j, dist = queue.pop()
            if i == rows - 1 and j == cols - 1:
                return dist

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = i + dx, j + dy
                if (
                    new_x in range(rows)
                    and new_y in range(cols)
                    and (new_x, new_y) not in visited
                    and grid[new_x][new_y] != "#"
                ):
                    queue.appendleft((new_x, new_y, dist + 1))
                    visited.add((new_x, new_y))

        return -1

    l, r = 0, len(input) - 1
    while l < r:
        mid = (l + r) // 2
        if simulate(mid) == -1:
            r = mid - 1
        else:
            l = mid + 1

    return input[l - 1]


# ---------------------------- SUBMIT ----------------------------

# time_function(False, part_1_solution, "sample.txt")
# time_function(False, part_1_solution, "full.txt")
# time_function(False, part_2_solution, "sample.txt")
time_function(False, part_2_solution, "full.txt")
