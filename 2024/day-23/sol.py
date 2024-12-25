# from collections import Counter, defaultdict, deque
# from functools import lru_cache
# import heapq
from collections import defaultdict, deque
import itertools
import math
import os
import sys
import networkx as nx

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(ROOT_DIR)
from utils.aoc_tools import time_function, nums, dir4

sys.setrecursionlimit(15000000)


def part_1_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input]

    G = nx.Graph()

    for pair in input:
        n1, n2 = pair.split("-")
        G.add_edge(n1, n2)
    
    res = nx.enumerate_all_cliques(G)
    ans = 0
    for a in res:
        if len(a) == 3 and any(x.startswith("t") for x in a):
            ans += 1
    return ans

def part_2_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input]

    G = nx.Graph()

    for pair in input:
        n1, n2 = pair.split("-")
        G.add_edge(n1, n2)
    
    res = nx.enumerate_all_cliques(G)
    max_clique_size = max(len(a) for a in res)
    res = nx.enumerate_all_cliques(G)
    for a in res:
        if len(a) == max_clique_size:
            return ",".join(sorted(a))


# ---------------------------- SUBMIT ----------------------------


time_function(part_1_solution, "sample.txt")
time_function(part_1_solution, "full.txt")
time_function(part_2_solution, "sample.txt")
time_function(part_2_solution, "full.txt")
