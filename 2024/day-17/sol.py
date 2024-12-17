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

    def get_operand(operand):
        if operand == 4: return a
        elif operand == 5: return b
        elif operand == 6: return c
        elif operand == 7: return 7
        else: return operand

    maxxx = 1000000000000000000
    for start_a in range(maxxx):
        # if start_a % 8 != instrs[-1]: continue
        if start_a % 10000000 == 0:
            print(f"{100 * start_a / maxxx}%")
        a = start_a
        i = 0
        ans = []
        counter = 0
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
                if instrs[counter] != ans[-1]:
                    break
                counter += 1
                if counter == len(instrs):
                    print(ans)
                    return start_a
                i += 2
            elif op == 6:
                new_a = a / (2 ** x)
                b = int(new_a)
                i += 2
            elif op == 7:
                new_a = a / (2 ** x)
                c = int(new_a)
                i += 2

    return -1


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
