from pprint import pprint
from collections import deque
import time


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
        checks.append([rest[-1]])

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


def part_is_good(rulebook, part):
    cur_workflow = "in"
    while True:
        for check in rulebook[cur_workflow]:
            if len(check) > 1:  # not the last state
                start, op, val, next = check
                if op == "<":
                    if part[start] < val:
                        if next == "A":
                            return True
                        elif next == "R":
                            return False
                        else:
                            cur_workflow = next
                            break
                elif op == ">":
                    if part[start] > val:
                        if next == "A":
                            return True
                        elif next == "R":
                            return False
                        else:
                            cur_workflow = next
                            break
            else:
                # we're at the last state
                if check[0] == "A":
                    return True
                if check[0] == "R":
                    return False

                cur_workflow = check[0]
                break


def solve(rulebook, parts):
    good_parts = []

    for part in parts:
        if part_is_good(rulebook, part):
            good_parts.append(part)

    ans = 0
    for part in good_parts:
        for val in part.values():
            ans += val

    return ans


def solution(filename):
    rules, parts = read_file(filename)
    rulebook, final_parts = parse_rules(rules), parse_parts(parts)

    return solve(rulebook, final_parts)


if __name__ == "__main__":
    small = "input_small.txt"
    large = "input_large.txt"

    print(solution(small))
    print(solution(large))
