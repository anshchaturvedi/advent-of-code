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

    import hashlib

    for i in range(100000000000):
        key = f"{input}{str(i)}"
        hash = hashlib.md5(key.encode())
        if hash.hexdigest().startswith("00000"):
            return i


def part_2_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input][0]

    import hashlib

    for i in range(100000000000):
        key = f"{input}{str(i)}"
        hash = hashlib.md5(key.encode())
        if hash.hexdigest().startswith("000000"):
            return i


# ---------------------------- SUBMIT ----------------------------
time_function(part_1_solution, "full.txt")
time_function(part_2_solution, "full.txt")
