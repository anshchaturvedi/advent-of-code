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


def part_2_solution(file_name: str):
    input = []

    with open(file_name) as input_file:
        line = input_file.readline()
        while line:
            a = line.strip()
            input.append(a)
            line = input_file.readline()


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

time_function(False, part_1_solution, "sample.txt")
time_function(args.submit, part_1_solution, "full.txt")
time_function(False, part_2_solution, "sample.txt")
time_function(args.submit, part_2_solution, "full.txt")
