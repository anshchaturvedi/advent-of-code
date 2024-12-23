# from collections import Counter, defaultdict, deque
# from functools import lru_cache
# import heapq
from collections import defaultdict, deque
import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(ROOT_DIR)
from utils.aoc_tools import time_function, nums, dir4

sys.setrecursionlimit(15000000)


def part_1_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input]
    input = [[x for x in row] for row in input]

    rows, cols = len(input), len(input[0])
    start_x, start_y = None, None

    for i in range(rows):
        for j in range(cols):
            if input[i][j] == "S":
                start_x, start_y = i, j

    queue = deque([(start_x, start_y)])
    dists = {}
    dists[(start_x, start_y)] = 0

    while queue:
        cx, cy = queue.pop()
        for dx, dy in dir4:
            nx, ny = cx + dx, cy + dy
            if (
                0 <= nx < rows
                and 0 <= ny < cols
                and input[nx][ny] != "#"
                and (nx, ny) not in dists
            ):
                dists[(nx, ny)] = dists[(cx, cy)] + 1
                queue.appendleft((nx, ny))

    count = 0
    for i in range(rows):
        for j in range(cols):
            if input[i][j] != "#":
                for dx, dy in [(2, 0), (1, 1), (0, 2), (-1, 1)]:
                    nx, ny = i + dx, j + dy
                    if nx in range(rows) and ny in range(cols) and input[nx][ny] != "#":
                        diff = abs(dists[i, j] - dists[nx, ny])
                        if diff >= 102:
                            count += 1
    return count


def part_2_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input]
    input = [[x for x in row] for row in input]

    rows, cols = len(input), len(input[0])
    start_x, start_y = None, None

    for i in range(rows):
        for j in range(cols):
            if input[i][j] == "S":
                start_x, start_y = i, j

    queue = deque([(start_x, start_y)])
    # dists = {}
    dists = [[-1 for _ in range(cols)] for _ in range(rows)]
    dists[start_x][start_y] = 0

    while queue:
        cx, cy = queue.pop()
        for dx, dy in dir4:
            nx, ny = cx + dx, cy + dy
            if (
                0 <= nx < rows
                and 0 <= ny < cols
                and input[nx][ny] != "#"
                and dists[nx][ny] == -1
            ):
                dists[nx][ny] = dists[cx][cy] + 1
                queue.appendleft((nx, ny))

    # for row in dists: print(row)
    count = 0
    for r in range(rows):
        for c in range(cols):
            if input[r][c] == "#":
                continue
            for radius in range(2, 21):
                for dr in range(radius + 1):
                    dc = radius - dr
                    for nx, ny in {
                        (r + dr, c + dc),
                        (r + dr, c - dc),
                        (r - dr, c + dc),
                        (r - dr, c - dc),
                    }:
                        if (
                            nx in range(rows)
                            and ny in range(cols)
                            and input[nx][ny] != "#"
                        ):
                            diff = dists[r][c] - dists[nx][ny]
                            if diff >= 100 + radius:
                                count += 1
    return count

# ---------------------------- SUBMIT ----------------------------


time_function(part_1_solution, "sample.txt")
time_function(part_1_solution, "full.txt")
time_function(part_2_solution, "sample.txt")
time_function(part_2_solution, "full.txt")
