# from collections import Counter, defaultdict, deque
# from functools import lru_cache
# import heapq
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

    nodes = {}
    i = 0
    while input[i] != "":
        node_name = input[i].split(":")[0]
        node_value = nums(input[i])[-1]
        nodes[node_name] = node_value
        i += 1

    # bfw: 1
    # bqk: 1
    # djm: 1
    # ffh: 0
    # fgs: 1
    # frj: 1
    # fst: 1
    # gnj: 1
    # hwm: 1
    # kjc: 0
    # kpj: 1
    # kwq: 0
    # mjb: 1
    # nrd: 1
    # ntg: 0
    # pbm: 1
    # psh: 1
    # qhw: 1
    # rvg: 0
    # tgd: 0
    # tnw: 1
    # vdt: 1
    # wpb: 0
    # z00: 0
    # z01: 0
    # z02: 0
    # z03: 1
    # z04: 0
    # z05: 1
    # z06: 1
    # z07: 1
    # z08: 1
    # z09: 1
    # z10: 1
    # z11: 0
    # z12: 0

    i += 1
    queue = deque([])
    while i < len(input):
        from_node1, op, from_node2, _, to_node = input[i].split(" ")

        if from_node1 not in nodes:
            nodes[from_node1] = None
        if from_node2 not in nodes:
            nodes[from_node2] = None
        if to_node not in nodes:
            nodes[to_node] = None

        queue.appendleft((from_node1, from_node2, op, to_node))
        i += 1

    def perform_op(from1, from2, op):
        if op == "AND":
            return 1 if (nodes[from1] == 1 and nodes[from2] == 1) else 0
        if op == "OR":
            return 1 if (nodes[from1] == 1 or nodes[from2] == 1) else 0
        if op == "XOR":
            return 1 if (nodes[from1] != nodes[from2]) else 0

        assert False, "should not be getting here!"

    while queue:
        from1, from2, op, to = queue.pop()
        if nodes[from1] is None or nodes[from2] is None:
            queue.appendleft((from1, from2, op, to))
            continue
        if nodes[to] is None:
            nodes[to] = perform_op(from1, from2, op)

    i = 0
    res = []
    while f"z{i:02d}" in nodes:
        res.append(str(nodes[f"z{i:02d}"]))
        i += 1
    return int("".join(reversed(res)), 2)


def part_2_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input]


# ---------------------------- SUBMIT ----------------------------


time_function(part_1_solution, "sample.txt")
time_function(part_1_solution, "full.txt")
# time_function(part_2_solution, "sample.txt")
# time_function(part_2_solution, "full.txt")
