import argparse
from collections import Counter, defaultdict, deque
from functools import lru_cache
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

    towels = set([i.strip() for i in input[0].split(",")])
    words = [word for word in input[2:]]

    def dfs(i, w):
        if i >= len(w):
            return True

        for j in range(i + 1, len(w) + 1):
            substr = w[i:j]
            if substr in towels and dfs(j, w):
                return True

        return False

    ans = 0
    for word in words:
        if dfs(0, word):
            ans += 1
    return ans

def part_2_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input]

    towels = set([i.strip() for i in input[0].split(",")])
    words = [word for word in input[2:]]

    @lru_cache
    def dfs(i, w):
        if i >= len(w):
            return 1

        res = 0
        for j in range(i + 1, len(w) + 1):
            substr = w[i:j]
            if substr in towels:
                res += dfs(j, w)

        return res

    ans = 0
    for word in words:
        ans += dfs(0, word)
    return ans


# ---------------------------- SUBMIT ----------------------------

time_function(part_1_solution, "sample.txt")
time_function(part_1_solution, "full.txt")
time_function(part_2_solution, "sample.txt")
time_function(part_2_solution, "full.txt")
