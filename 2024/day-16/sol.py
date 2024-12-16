import argparse
from collections import Counter, defaultdict, deque
import heapq
import math
import os
from time import sleep
import numpy as np
import pprint
import re
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(ROOT_DIR)
from utils.aoc_tools import time_function, nums
from utils.get_input import get_puzzle_input

sys.setrecursionlimit(15000000)

def part_1_solution(file_name: str):
    input = []

    with open(file_name) as input_file:
        line = input_file.readline()
        while line:
            a = line.strip()
            input.append([i for i in a])
            line = input_file.readline()
    
    start_x, start_y = None, None
    end_x, end_y = None, None
    rows, cols = len(input), len(input[0])

    for i in range(rows):
        for j in range(cols):
            if input[i][j] == "S":
                start_x, start_y = i, j
            if input[i][j] == "E":
                end_x, end_y = i, j
    
    queue = [(0, start_x, start_y, "E")] # cur_score, i, j, dir
    distances = defaultdict(lambda: float('inf'))
    dirs = {"E": (0, 1), "W": (0, -1), "N": (1, 0), "S": (-1, 0)}
    distances[(start_x, start_y)] = 0

    def other_dirs(dir):
        if dir in "EW": return ["N", "S"]
        else: return ["E", "W"]
    
    while queue:
        cost, i, j, dir = heapq.heappop(queue)
        if i == end_x and j == end_y:
            return cost
        dx, dy = dirs[dir]
        if i + dx in range(rows) and j + dy in range(cols):
            if input[i+dx][j+dy] != "#":
                new_cost = cost + 1
                if new_cost < distances[(i+dx, j+dy)]:
                    distances[(i+dx, j+dy)] = new_cost
                    heapq.heappush(queue, (new_cost, i+dx, j+dy, dir))

        for new_dir in other_dirs(dir):
            dx, dy = dirs[new_dir]
            if input[i+dx][j+dy] != "#":
                if i + dx in range(rows) and j + dy in range(cols):
                    new_cost = cost + 1000 + 1
                    if new_cost < distances[(i+dx, j+dy)]:
                        distances[(i+dx, j+dy)] = new_cost
                        heapq.heappush(queue, (new_cost, i+dx, j+dy, new_dir))


def part_2_solution(file_name: str):
    input = []

    with open(file_name) as input_file:
        line = input_file.readline()
        while line:
            a = line.strip()
            input.append([i for i in a])
            line = input_file.readline()
    
    start_x, start_y = None, None
    end_x, end_y = None, None
    rows, cols = len(input), len(input[0])

    for i in range(rows):
        for j in range(cols):
            if input[i][j] == "S":
                start_x, start_y = i, j
            if input[i][j] == "E":
                end_x, end_y = i, j
    
    queue = [(0, start_x, start_y, "E", [])] # cur_score, i, j, dir
    distances = defaultdict(lambda: float('inf'))
    dirs = {"E": (0, 1), "W": (0, -1), "N": (1, 0), "S": (-1, 0)}
    distances[(start_x, start_y, "E")] = 0

    best = float('inf')
    map_best = defaultdict(set)

    def other_dirs(dir):
        if dir in "EW": return ["N", "S"]
        else: return ["E", "W"]
    
    while queue:
        cost, i, j, dir, visited = heapq.heappop(queue)
        if i == end_x and j == end_y:
            if cost <= best:
                best = cost
                for node in visited:
                    map_best[best].add(node)

        dx, dy = dirs[dir]
        if i + dx in range(rows) and j + dy in range(cols):
            if input[i+dx][j+dy] != "#":
                new_cost = cost + 1
                if new_cost <= distances[(i+dx, j+dy, dir)]:
                    distances[(i+dx, j+dy, dir)] = new_cost
                    heapq.heappush(queue, (new_cost, i+dx, j+dy, dir, visited + [(i, j)]))

        for new_dir in other_dirs(dir):
            dx, dy = dirs[new_dir]
            if input[i+dx][j+dy] != "#":
                if i + dx in range(rows) and j + dy in range(cols):
                    new_cost = cost + 1000 + 1
                    if new_cost <= distances[(i+dx, j+dy, dir)]:
                        distances[(i+dx, j+dy, new_dir)] = new_cost
                        heapq.heappush(queue, (new_cost, i+dx, j+dy, new_dir, visited + [(i, j)]))

    # print(best)
    # print(len(map_best[best]))
    # for x, y in map_best[best]:
    #     input[x][y] = "O"
    # for row in input: print("".join(row))

    map_best[best].add((end_x, end_y))
    return len(map_best[best])


# ---------------------------- RUN AND SUBMIT ----------------------------


parser = argparse.ArgumentParser(description="Advent of Code Solution Script")
parser.add_argument(
    "-s", "--submit", action="store_true", help="Submit the solution to Advent of Code"
)
args = parser.parse_args()

# get_puzzle_input(suppress_logs=True)

time_function(False, part_1_solution, "sample.txt")
time_function(args.submit, part_1_solution, "full.txt")
time_function(False, part_2_solution, "sample.txt")
time_function(args.submit, part_2_solution, "full.txt")
