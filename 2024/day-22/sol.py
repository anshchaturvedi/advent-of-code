# from collections import Counter, defaultdict, deque
# from functools import lru_cache
# import heapq
from collections import defaultdict, deque
import itertools
import math
import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(ROOT_DIR)
from utils.aoc_tools import time_function, nums, dir4

sys.setrecursionlimit(15000000)


def part_1_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input]
    input = list(map(int, input))

    def transform(secret):
        new_secret = secret
        r1 = secret * 64
        new_secret = new_secret ^ r1
        new_secret = new_secret % 16777216

        r2 = int(new_secret / 32)
        new_secret = new_secret ^ r2
        new_secret = new_secret % 16777216

        r3 = new_secret * 2048
        new_secret = new_secret ^ r3
        new_secret = new_secret % 16777216

        return new_secret

    ans = 0
    for secret in input:
        cur = secret
        for _ in range(2000):
            cur = transform(cur)
        ans += cur
    return ans


def part_2_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input]
    input = list(map(int, input))

    def transform(secret):
        new_secret = secret
        r1 = secret * 64
        new_secret = new_secret ^ r1
        new_secret = new_secret % 16777216

        r2 = int(new_secret / 32)
        new_secret = new_secret ^ r2
        new_secret = new_secret % 16777216

        r3 = new_secret * 2048
        new_secret = new_secret ^ r3
        new_secret = new_secret % 16777216

        return new_secret

    prices_by_secret = defaultdict(list)
    secret_to_highest_window = defaultdict(
        lambda: defaultdict(lambda: float("-inf"))
    )  # secret -> {window -> highest_banana_score}
    ans = 0
    for secret in input:
        cur = secret
        for _ in range(2001):
            prices_by_secret[secret].append(cur % 10)
            cur = transform(cur)

        window = deque()
        for i in range(4):
            window.append(prices_by_secret[secret][i + 1] - prices_by_secret[secret][i])
        k = 4
        secret_to_highest_window[secret][tuple(window)] = max(
            prices_by_secret[secret][k], secret_to_highest_window[secret][tuple(window)]
        )
        for k in range(5, 2001):
            window.popleft()
            window.append(prices_by_secret[secret][k] - prices_by_secret[secret][k - 1])
            if tuple(window) not in secret_to_highest_window[secret]:
                secret_to_highest_window[secret][tuple(window)] = prices_by_secret[secret][k]

    all_keys = set()
    for buyer in input:
        for key in secret_to_highest_window[buyer].keys():
            all_keys.add(key)

    ans = 0
    for i, key in enumerate(list(all_keys)):
        total = 0
        for buyer in input:
            total += max(0, secret_to_highest_window[buyer][key])
        ans = max(ans, total)

    return ans


# ---------------------------- SUBMIT ----------------------------


time_function(part_1_solution, "sample.txt")
time_function(part_1_solution, "full.txt")
time_function(part_2_solution, "sample.txt")
time_function(part_2_solution, "full.txt")
