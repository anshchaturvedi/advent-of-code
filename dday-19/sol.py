from pprint import pprint
from collections import deque


def read_file(filename, t=False):
    lines = [line.strip() for line in open(filename)]
    res, acc = [], []
    for line in lines:
        if line != "":
            acc.append(line)
        else:
            res.append(acc)
            acc = []
    res.append(acc)
    return res


def parse_rules(rules):
    rulebook = {}
    for rule in rules:
        start, i = [], 0
        while rule[i] != "{":
            start.append(rule[i])
            i += 1
        start = "".join(start)

        rest = rule[i + 1 : -1].split(",")
        checks = []
        for i in range(len(rest) - 1):
            check = rest[i].split(":")
            x, op, num, to = check[0][0], check[0][1], int(check[0][2:]), check[1]
            checks.append([x, op, num, to])
        checks.append(rest[-1])

        rulebook[start] = checks

    return rulebook


def parse_parts(parts):
    res = []
    for part in parts:
        acc = {}

        part = part[1:-1].split(",")
        for p in part:
            start, num = p[0], int(p[2:])
            acc[start] = num
        res.append(acc)

    return res


def solve(rulebook, parts):
    good_parts = []

    for part in parts:
        cur_workflow = "in"
        i = 0


def solution(filename):
    rules, parts = read_file(filename)
    rulebook, final_parts = parse_rules(rules), parse_parts(parts)

    return solve(rulebook, final_parts)


if __name__ == "__main__":
    small = "input_small.txt"
    large = "input_large.txt"

    print(solution(small))
    # print(solution(large))
