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

    ans = 0
    for word in input:
        seen_vowels = 0
        bad_strings = set(["ab", "cd", "pq", "xy"])
        bad = False
        found_matching = False
        for i in range(len(word)):
            if word[i] in "aeiou":
                seen_vowels += 1
        for i in range(len(word) - 1):
            if f"{word[i]}{word[i+1]}" in bad_strings:
                bad = True
                break
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                found_matching = True
                break

        if seen_vowels >= 3 and found_matching and not bad:
            ans += 1

    return ans


def part_2_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input]

    ans = 0
    for word in input:
        pairs = defaultdict(set)
        first = False
        second = False

        for i in range(len(word) - 1):
            new_str = f"{word[i]}{word[i+1]}"
            pairs[new_str].add(i)

        for s in pairs.keys():
            if len(pairs[s]) == 2:
                a = pairs[s].pop()
                if (a + 1) not in pairs[s] and (a - 1) not in pairs[s]:
                    first = True
                    break

            if len(pairs[s]) > 2:
                first = True
                break

        for i in range(1, len(word) - 1):
            if word[i - 1] == word[i + 1]:
                second = True
                break

        if first and second:
            ans += 1

    return ans


# ---------------------------- SUBMIT ----------------------------
time_function(part_1_solution, "full.txt")
time_function(part_2_solution, "full.txt")
