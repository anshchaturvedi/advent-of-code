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
    for i in input[0]:
        ans = ans + 1 if i == "(" else ans - 1
    return ans


def part_2_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input]

    ans = 0
    for idx, i in enumerate(input[0], 1):
        ans = ans + 1 if i == "(" else ans - 1
        if ans == -1:
            return idx


# ---------------------------- SUBMIT ----------------------------
time_function(part_1_solution, "full.txt")
time_function(part_2_solution, "full.txt")
