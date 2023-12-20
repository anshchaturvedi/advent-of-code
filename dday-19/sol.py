from pprint import pprint
from collections import deque
import copy


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


def calculate_all_combinations(rulebook):
    ans = 0

    def dfs(cur_workflow, constraints):
        nonlocal ans
        if cur_workflow == "A":
            values = constraints.values()
            res = 1
            for low, high in values:
                res *= high - low + 1
            ans += res
            return

        if cur_workflow == "R":
            return

        for rule in rulebook[cur_workflow]:
            if len(rule) > 1:
                a, op, val, next = rule
                if op == ">":
                    tmp = constraints[a][0]
                    constraints[a][0] = val + 1
                    dfs(next, copy.deepcopy(constraints))
                    constraints[a][0] = tmp
                    constraints[a][1] = val
                else:
                    tmp = constraints[a][1]
                    constraints[a][1] = val - 1
                    dfs(next, copy.deepcopy(constraints))
                    constraints[a][1] = tmp
                    constraints[a][0] = val
            else:
                dfs(rule[0], copy.deepcopy(constraints))

    dfs("in", {i: [1, 4000] for i in ["x", "m", "a", "s"]})
    return ans


def solution(filename):
    rules, _parts = read_file(filename)
    rulebook = parse_rules(rules)
    return calculate_all_combinations(rulebook)


if __name__ == "__main__":
    small = "input_small.txt"
    large = "input_large.txt"

    print(solution(small))
    print(solution(large))
