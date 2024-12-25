# from collections import Counter, defaultdict, deque
# from functools import lru_cache
# import heapq
from collections import defaultdict, deque
import itertools
import math
import os
from pprint import pprint
import sys
import networkx as nx

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(ROOT_DIR)
from utils.aoc_tools import time_function, nums, dir4

sys.setrecursionlimit(15000000)


def transpose(grid):
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]


def part_1_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input]

    grids = [[]]
    for row in input:
        if row == "":
            grids.append([])
        else:
            grids[-1].append([i for i in row])

    rows = len(grids[0])

    keys, locks = [], []
    for grid in grids:
        transposed = transpose(grid)
        lengths = [row.count("#") - 1 for row in transposed]

        if all(x == "#" for x in grid[0]):
            locks.append(lengths)
        elif all(x == "#" for x in grid[-1]):
            keys.append(lengths)

    all_combos = itertools.product(keys, locks)
    ans = 0
    for key, lock in all_combos:
        good = True
        for a, b in zip(key, lock):
            if a + b >= rows - 1:
                good = False
        if good:
            ans += 1
    return ans


def part_2_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input]


# ---------------------------- SUBMIT ----------------------------


time_function(part_1_solution, "sample.txt")
time_function(part_1_solution, "full.txt")
# time_function(part_2_solution, "sample.txt")
# time_function(part_2_solution, "full.txt")
