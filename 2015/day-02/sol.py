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
    input = [x.strip() for x in input]

    ans = 0
    for line in input:
        x, y, z = nums(line)
        a1, a2, a3 = x * y, x * z, y * z
        ans += 2 * (a1 + a2 + a3) + min(a1, a2, a3)
    return ans


def part_2_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input]

    ans = 0
    for line in input:
        sides = sorted(nums(line))
        ans += 2 * (sides[0] + sides[1]) + (sides[0] * sides[1] * sides[2])
    return ans


# ---------------------------- SUBMIT ----------------------------
time_function(part_1_solution, "full.txt")
time_function(part_2_solution, "full.txt")
