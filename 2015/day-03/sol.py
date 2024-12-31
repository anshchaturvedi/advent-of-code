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


def part_1_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input][0]

    dirs = {"^": (1, 0), "v": (-1, 0), "<": (0, -1), ">": (0, 1)}

    seen = defaultdict(int)
    cur = (0, 0)
    seen[cur] += 1

    for dir in input:
        (cx, cy), (nx, ny) = cur, dirs[dir]
        cur = (cx + nx, cy + ny)
        seen[cur] += 1

    return sum(1 if v >= 1 else 0 for v in seen.values())


def part_2_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input][0]

    dirs = {"^": (1, 0), "v": (-1, 0), "<": (0, -1), ">": (0, 1)}

    seen = defaultdict(int)
    cur1 = (0, 0)
    cur2 = (0, 0)
    seen[cur1] += 2

    for i in range(0, len(input) - 1, 2):
        (cx1, cy1), (cx2, cy2), (nx1, ny1), (nx2, ny2) = (
            cur1,
            cur2,
            dirs[input[i]],
            dirs[input[i + 1]],
        )
        cur1 = (cx1 + nx1, cy1 + ny1)
        cur2 = (cx2 + nx2, cy2 + ny2)
        seen[cur1] += 1
        seen[cur2] += 1

    return sum(1 if v >= 1 else 0 for v in seen.values())


# ---------------------------- SUBMIT ----------------------------
time_function(part_1_solution, "full.txt")
time_function(part_2_solution, "full.txt")
