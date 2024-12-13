from collections import Counter, defaultdict, deque
import math
import pprint
import sys
import time
import re
import numpy as np

sys.setrecursionlimit(15000000)

def get_nums(x):
    pattern = r"\d+"
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
            if a != "":
                input.append(a)
            line = input_file.readline()

    claws = []
    for i in range(0, len(input) - 1, 3):
        claws.append([input[i], input[i + 1], input[i + 2]])

    ans = 0
    for claw in claws:
        a, b, prize = claw
        c1, c2 = get_nums(a)
        d1, d2 = get_nums(b)
        px, py = get_nums(prize)

        a = np.array([[c1, d1], [c2, d2]])
        b = np.array([px, py])
        sol = np.linalg.solve(a, b)
        x, y = round(sol[0]), round(sol[1])

        if c1 * x + d1 * y == px and c2 * x + d2 * y == py:
            ans += (3 * x) + y

    return ans


def part_2_solution(file_name: str):
    input = []

    with open(file_name) as input_file:
        line = input_file.readline()
        while line:
            a = line.strip()
            if a != "":
                input.append(a)
            line = input_file.readline()

    claws = []
    for i in range(0, len(input) - 1, 3):
        claws.append([input[i], input[i + 1], input[i + 2]])

    ans = 0
    for claw in claws:
        a, b, prize = claw
        a, b, prize = claw
        c1, c2 = get_nums(a)
        d1, d2 = get_nums(b)
        px, py = get_nums(prize)
        px += 10000000000000
        py += 10000000000000

        a = np.array([[c1, d1], [c2, d2]])
        b = np.array([px, py])
        sol = np.linalg.solve(a, b)
        x, y = round(sol[0]), round(sol[1])

        if c1 * x + d1 * y == px and c2 * x + d2 * y == py:
            ans += (3 * x) + y

    return ans


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


time_function(part_1_solution, "sample.txt")
time_function(part_1_solution, "full.txt")
time_function(part_2_solution, "sample.txt")
time_function(part_2_solution, "full.txt")
