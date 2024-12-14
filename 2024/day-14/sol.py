from collections import Counter, defaultdict, deque
import heapq
import math
import pprint
import sys
import time
import re
import numpy as np

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

    rows, cols = 103, 101
    input = list(map(get_nums, input))

    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for line in input:
        robot_x_pos, robot_y_pos = line[1], line[0]
        robot_x_vel, robot_y_vel = line[3], line[2]
        robot_x_pos = (robot_x_pos + 100 * robot_x_vel) % rows
        robot_y_pos = (robot_y_pos + 100 * robot_y_vel) % cols
        grid[robot_x_pos][robot_y_pos] += 1

    c1, c2, c3, c4 = 0, 0, 0, 0
    for i in range(rows // 2):
        for j in range(cols // 2):
            c1 += grid[i][j]
            c2 += grid[i][cols - 1 - j]
            c3 += grid[rows - 1 - i][j]
            c4 += grid[rows - 1 - i][cols - 1 - j]

    return c1 * c2 * c3 * c4


def part_2_solution(file_name: str):
    input = []

    with open(file_name) as input_file:
        line = input_file.readline()
        while line:
            a = line.strip()
            input.append(a)
            line = input_file.readline()

    rows, cols = 103, 101
    input = list(map(get_nums, input))

    heap = []
    for step in range(1, rows * cols):
        grid = [["." for _ in range(cols)] for _ in range(rows)]
        if step % 1000 == 0:
            print(f"step {step} out of {rows * cols} steps")
        for line in input:
            robot_x_pos, robot_y_pos = line[1], line[0]
            robot_x_vel, robot_y_vel = line[3], line[2]
            robot_x_pos = (robot_x_pos + step * robot_x_vel) % rows
            robot_y_pos = (robot_y_pos + step * robot_y_vel) % cols
            grid[robot_x_pos][robot_y_pos] = "#"

        beside = 0
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if grid[i][j] == "#":
                    for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                        if grid[i + dx][j + dy] == "#":
                            beside += 1

        heapq.heappush(heap, (-beside, step))

    _, time = heapq.heappop(heap)

    for line in input:
        robot_x_pos, robot_y_pos = line[1], line[0]
        robot_x_vel, robot_y_vel = line[3], line[2]
        robot_x_pos = (robot_x_pos + time * robot_x_vel) % rows
        robot_y_pos = (robot_y_pos + time * robot_y_vel) % cols
        grid[robot_x_pos][robot_y_pos] = "#"

    with open("christmas_tree.txt", "w") as f:
        for row in grid:
            f.write("".join(row) + "\n")


def time_function(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    elapsed_time = int(
        (end_time - start_time) * 1000
    )  # Convert to milliseconds and cast to int
    input_type = "sample" if "sample" in args[0] else "full"
    part = "part 1" if "part_1" in func.__name__ else "part 2"
    print(
        f"{input_type} input {part} took {elapsed_time} milliseconds and returned {result}"
    )


# time_function(part_1_solution, "sample.txt")
time_function(part_1_solution, "full.txt")
# time_function(part_2_solution, "sample.txt")
time_function(part_2_solution, "full.txt")
