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

    grid = [[False for _ in range(1000)] for _ in range(1000)]

    for line in input:
        ax, ay, bx, by = nums(line)
        instr = line.split(",")[0].split(" ")
        mode = ""
        if instr[0] == "toggle":
            mode = "toggle"
        elif instr[1] == "on":
            mode = "on"
        else:
            mode = "off"

        for x in range(ax, bx + 1):
            for y in range(ay, by + 1):
                if mode == "toggle":
                    grid[x][y] = not grid[x][y]
                elif mode == "on":
                    grid[x][y] = True
                else:
                    grid[x][y] = False

    return sum(row.count(True) for row in grid)


def part_2_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input]

    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in input:
        ax, ay, bx, by = nums(line)
        instr = line.split(",")[0].split(" ")
        mode = ""
        if instr[0] == "toggle":
            mode = "toggle"
        elif instr[1] == "on":
            mode = "on"
        else:
            mode = "off"

        for x in range(ax, bx + 1):
            for y in range(ay, by + 1):
                if mode == "toggle":
                    grid[x][y] += 2
                elif mode == "on":
                    grid[x][y] += 1
                else:
                    grid[x][y] -= 1
                    grid[x][y] = max(0, grid[x][y])

    return sum(sum(row) for row in grid)


# ---------------------------- SUBMIT ----------------------------
time_function(part_1_solution, "full.txt")
time_function(part_2_solution, "full.txt")
