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
    dirs = []
    to_input = True

    with open(file_name) as input_file:
        line = input_file.readline()
        while line:
            a = line.strip()
            if a == "":
                to_input = False
            if to_input:
                input.append(a)
            else:
                dirs.append(a)
            line = input_file.readline()

    final = ""
    for dir in dirs:
        for c in dir:
            final += c
    input = [[i for i in row] for row in input]
    rows, cols = len(input), len(input[0])

    x, y = None, None
    for i in range(rows):
        for j in range(cols):
            if input[i][j] == "@":
                x, y = i, j

    for dir in final:
        # print(dir)
        if dir == ">":
            if y + 1 < cols:
                if input[x][y + 1] == ".":
                    input[x][y + 1], input[x][y] = input[x][y], input[x][y + 1]
                    y += 1
                elif input[x][y + 1] == "#":
                    pass
                else:
                    # go as far right as possible
                    cur_col = y + 1
                    while cur_col < cols and input[x][cur_col] == "O":
                        cur_col += 1
                    # if last point is a wall we can't do anything
                    if input[x][cur_col] != "#":
                        while cur_col > y:
                            input[x][cur_col], input[x][cur_col - 1] = (
                                input[x][cur_col - 1],
                                input[x][cur_col],
                            )
                            cur_col -= 1
                        y += 1
        elif dir == "<":
            if y - 1 > 0:
                if input[x][y - 1] == ".":
                    input[x][y - 1], input[x][y] = input[x][y], input[x][y - 1]
                    y -= 1
                elif input[x][y - 1] == "#":
                    pass
                else:
                    # go as far left as possible
                    cur_col = y - 1
                    while cur_col >= 0 and input[x][cur_col] == "O":
                        cur_col -= 1
                    # if last point is a wall we can't do anything
                    if input[x][cur_col] != "#":
                        while cur_col < y:
                            input[x][cur_col], input[x][cur_col + 1] = (
                                input[x][cur_col + 1],
                                input[x][cur_col],
                            )
                            cur_col += 1
                        y -= 1
        elif dir == "^":
            if x - 1 > 0:
                if input[x - 1][y] == ".":
                    input[x - 1][y], input[x][y] = input[x][y], input[x - 1][y]
                    x -= 1
                elif input[x - 1][y] == "#":
                    pass
                else:
                    # go as far up
                    cur_row = x - 1
                    while cur_row >= 0 and input[cur_row][y] == "O":
                        cur_row -= 1
                    # if last point is a wall we can't do anything
                    if input[cur_row][y] != "#":
                        while cur_row < x:
                            input[cur_row][y], input[cur_row + 1][y] = (
                                input[cur_row + 1][y],
                                input[cur_row][y],
                            )
                            cur_row += 1
                        x -= 1
        else:
            if x + 1 < rows:
                if input[x + 1][y] == ".":
                    input[x + 1][y], input[x][y] = input[x][y], input[x + 1][y]
                    x += 1
                elif input[x + 1][y] == "#":
                    pass
                else:
                    # go as far down
                    cur_row = x + 1
                    while cur_row < rows and input[cur_row][y] == "O":
                        cur_row += 1
                    # if last point is a wall we can't do anything
                    if input[cur_row][y] != "#":
                        while cur_row > x:
                            input[cur_row][y], input[cur_row - 1][y] = (
                                input[cur_row - 1][y],
                                input[cur_row][y],
                            )
                            cur_row -= 1
                        x += 1

    ans = 0
    for i in range(rows):
        for j in range(cols):
            if input[i][j] == "O":
                ans += 100 * i + j
    return ans

def part_2_solution(file_name: str):
    input = []
    dirs = []
    to_input = True

    with open(file_name) as input_file:
        line = input_file.readline()
        while line:
            a = line.strip()
            if a == "":
                to_input = False
            if to_input:
                input.append(a)
            else:
                dirs.append(a)
            line = input_file.readline()

    final = ""
    for dir in dirs:
        for c in dir:
            final += c
    input = [[i for i in row] for row in input]

    new_input = []
    for row in input:
        new_input.append([])
        for char in row:
            if char == "#":
                new_input[-1].append("#")
                new_input[-1].append("#")
            if char == "O":
                new_input[-1].append("[")
                new_input[-1].append("]")
            if char == ".":
                new_input[-1].append(".")
                new_input[-1].append(".")
            if char == "@":
                new_input[-1].append("@")
                new_input[-1].append(".")

    rows, cols = len(new_input), len(new_input[0])

    # for row in new_input:
    #     print("".join(row))
    # print()

    x, y = None, None
    for i in range(rows):
        for j in range(cols):
            if new_input[i][j] == "@":
                x, y = i, j
    
    mapping = {"^": (-1, 0), "v": (1, 0)}
    
    def is_move_possible(i, j, dir):
        if new_input[i][j] == "#":
            return False
        if new_input[i][j] in "[]":
            if new_input[i][j] == "]": j -= 1
            if dir in "^v":
                dx = mapping[dir][0]
                return is_move_possible(i + dx, j, dir) and is_move_possible(i + dx, j + 1, dir)
        return True
    
    def make_move(i, j, dir):
        if new_input[i][j] in "#.": return
        if new_input[i][j] == "]": j -= 1
        dx = mapping[dir][0]
        # post-order dfs, first move every thing that is above/below the current cell...
        make_move(i+dx, j, dir)
        make_move(i+dx, j+1, dir)

        # ...and then move the current cell
        new_input[i][j], new_input[i+dx][j] = new_input[i+dx][j], new_input[i][j]
        new_input[i][j+1], new_input[i+dx][j+1] = new_input[i+dx][j+1], new_input[i][j+1]

    for dir_no, dir in enumerate(final):
        if dir == ">":
            if y + 1 < cols:
                if new_input[x][y + 1] == ".":
                    new_input[x][y + 1], new_input[x][y] = new_input[x][y], new_input[x][y + 1]
                    y += 1
                elif new_input[x][y + 1] == "#":
                    pass
                else:
                    # go as far right as possible
                    cur_col = y + 1
                    while cur_col < cols and new_input[x][cur_col] in '[]':
                        cur_col += 1
                    # if last point is a wall we can't do anything
                    if new_input[x][cur_col] != "#":
                        while cur_col > y:
                            new_input[x][cur_col], new_input[x][cur_col - 1] = (
                                new_input[x][cur_col - 1],
                                new_input[x][cur_col],
                            )
                            cur_col -= 1
                        y += 1
        elif dir == "<":
            if y - 1 > 0:
                if new_input[x][y - 1] == ".":
                    new_input[x][y - 1], new_input[x][y] = new_input[x][y], new_input[x][y - 1]
                    y -= 1
                elif new_input[x][y - 1] == "#":
                    pass
                else:
                    # go as far left as possible
                    cur_col = y - 1
                    while cur_col >= 0 and new_input[x][cur_col] in "[]":
                        cur_col -= 1
                    # if last point is a wall we can't do anything
                    if new_input[x][cur_col] != "#":
                        while cur_col < y:
                            new_input[x][cur_col], new_input[x][cur_col + 1] = (
                                new_input[x][cur_col + 1],
                                new_input[x][cur_col],
                            )
                            cur_col += 1
                        y -= 1 
        else:
            dx = mapping[dir][0]
            if is_move_possible(x + dx, y, dir):
                make_move(x + dx, y, dir)
                new_input[x][y], new_input[x + dx][y] = new_input[x + dx][y], new_input[x][y]
                x += dx

    ans = 0
    for i in range(rows):
        for j in range(cols):
            if new_input[i][j] == "[":
                ans += 100 * i + j
    return ans


# ---------------------------- RUN AND SUBMIT ----------------------------


parser = argparse.ArgumentParser(description="Advent of Code Solution Script")
parser.add_argument(
    "-s", "--submit", action="store_true", help="Submit the solution to Advent of Code"
)
args = parser.parse_args()

# get_puzzle_input(suppress_logs=True)

time_function(part_1_solution, "sample.txt")
time_function(part_1_solution, "full.txt")
time_function(part_2_solution, "sample.txt")
time_function(part_2_solution, "full.txt")
