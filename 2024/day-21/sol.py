# from collections import Counter, defaultdict, deque
# from functools import lru_cache
# import heapq
from collections import defaultdict, deque
import itertools
import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(ROOT_DIR)
from utils.aoc_tools import time_function, nums, dir4

sys.setrecursionlimit(15000000)

numeric_keypad = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}


# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

direction_keypad = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+


def should_swap(string, start, curr):
    for i in range(start, curr):
        if string[i] == string[curr]:
            return False
    return True


def get_permutations(s):
    res = []
    find_permutations(list(s), 0, len(s), res)
    return res


def find_permutations(string, index, n, res):
    if index >= n:
        res.append("".join(string))
        return

    for i in range(index, n):
        if should_swap(string, index, i):
            string[index], string[i] = string[i], string[index]
            find_permutations(string, index + 1, n, res)
            string[index], string[i] = string[i], string[index]


def part_1_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input]

    def generate_moves(moves, start=False):
        if start:
            keypad = numeric_keypad
        else:
            keypad = direction_keypad

        cx, cy = keypad["A"]
        res = []
        for c in moves:
            nx, ny = keypad[c]

            # get either up or down
            if nx > cx:
                for _ in range(nx - cx):
                    res.append("v")
            else:
                for _ in range(cx - nx):
                    res.append("^")

            # get either left or right
            if ny > cy:
                for _ in range(ny - cy):
                    res.append(">")
            else:
                for _ in range(cy - ny):
                    res.append("<")

            res.append("A")
            cx, cy = nx, ny

        print("og:", ''.join(res))
        # print("".join(res).split("A")[:-1])
        # return ["".join(res)]

        a = "".join(res).split("A")[:-1]
        all_combos = []
        def recurse(i, word):
            if i == len(a):
                all_combos.append(list(word))
                return
            all_perms = get_permutations(a[i])
            for perm in all_perms:
                # if perm == "":
                #     word.append(" ")
                # else:
                word.append(perm)
                recurse(i+1, word)
                word.pop()
        recurse(0, [])
        # print(a)
        # for ab in all_combos: print("A".join(ab))
        all_combos = ["A".join(x) for x in all_combos]
        return all_combos

    ans = 0
    for code in input:
        print(f"looking at {code}")
        res = generate_moves(code, True)
        lowest = min(map(len, res))
        possible_res = [s for s in res if len(s) == lowest]
        print(possible_res)

        res2 = []
        for r in possible_res:
            moves = generate_moves(r)
            for move in moves:
                res2.append(move)
        lowest = min(map(len, res2))
        possible_res = [s for s in res2 if len(s) == lowest]
        # for move in possible_res: print(move)
        print(possible_res[-1])
        print("og: v<<A>>^A<A>AvA<^AA>A<vAAA>^A")

        # res3 = []
        # for r in possible_res:
        #     res3.extend(generate_moves(r))
        # lowest = min(map(len, res3))
        # possible_res = [s for s in res3 if len(s) == lowest]
        # print(lowest, possible_res[0])

        # for x in res: print(x)
        # break
        # res1 = generate_moves(res)
        # res2 = generate_moves(res1)
        # res3 = generate_moves(res2)


    return ans

def part_1_solution(file_name: str):
    pass

def part_2_solution(file_name: str):
    input = open(file_name).readlines()
    input = [x.strip() for x in input]

# ---------------------------- SUBMIT ----------------------------


time_function(part_1_solution, "sample.txt")
# time_function(part_1_solution, "full.txt")
# time_function(part_2_solution, "sample.txt")
# time_function(part_2_solution, "full.txt")
