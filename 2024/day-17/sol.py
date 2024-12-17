import argparse
from collections import Counter, defaultdict, deque
import heapq
import math
import os
from time import sleep
import time
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
    input = open(file_name).readlines()
    input = [x.strip() for x in input]

    a = nums(input[0])[0]
    b = nums(input[1])[0]
    c = nums(input[2])[0]
    instrs = nums(input[4])

    def get_operand(operand):
        if operand == 4: return a
        elif operand == 5: return b
        elif operand == 6: return c
        elif operand == 7: return 7
        else: return operand

    i = 0
    ans = []

    while i < len(instrs):
        op, operand = instrs[i], instrs[i+1]
        x = get_operand(operand)
        if op == 0:
            new_a = a / (2 ** x)
            a = int(new_a)
            i += 2
        elif op == 1:
            b = b ^ operand
            i += 2
        elif op == 2:
            b = x % 8
            i += 2
        elif op == 3:
            if a == 0:
                i += 2
            else:
                i = operand
        elif op == 4:
            b = b ^ c
            i += 2
        elif op == 5:
            ans.append(x % 8)
            i += 2
        elif op == 6:
            new_a = a / (2 ** x)
            b = int(new_a)
            i += 2
        elif op == 7:
            new_a = a / (2 ** x)
            c = int(new_a)
            i += 2

    return ",".join(list(map(str, ans)))
    

def part_2_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input]

    a = nums(input[0])[0]
    b = nums(input[1])[0]
    c = nums(input[2])[0]
    instrs = nums(input[4])

    def simulate(start_a_value):
        def get_operand(operand):
            if operand == 4: return reg_a
            elif operand == 5: return reg_b
            elif operand == 6: return reg_c
            elif operand == 7: return 7
            else: return operand

        reg_a = start_a_value
        reg_b = b
        reg_c = c
        i = 0
        ans = []

        while i < len(instrs):
            op, operand = instrs[i], instrs[i+1]
            x = get_operand(operand)
            if op == 0:
                reg_a = int(reg_a / (2 ** x))
                i += 2
            elif op == 1:
                reg_b = reg_b ^ operand
                i += 2
            elif op == 2:
                reg_b = x % 8
                i += 2
            elif op == 3:
                if reg_a == 0:
                    i += 2
                else:
                    i = operand
            elif op == 4:
                reg_b = reg_b ^ reg_c
                i += 2
            elif op == 5:
                ans.append(x % 8)
                i += 2
            elif op == 6:
                new_a = reg_a / (2 ** x)
                reg_b = int(new_a)
                i += 2
            elif op == 7:
                new_a = reg_a / (2 ** x)
                reg_c = int(new_a)
                i += 2

        return ans

    possibilities = {0: [x for x in range(8)]}
    for exponent in range(1, len(instrs)):
        possibilities[exponent] = []
        for p in possibilities[exponent - 1]:
            for q in range(8):
                if p != 0:
                    a = 8 * p + q
                    out = simulate(a)
                    l = len(out)
                    if out == instrs[len(instrs) - l:]:
                        possibilities[exponent].append(a)
                    if out == instrs:
                        return a

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
