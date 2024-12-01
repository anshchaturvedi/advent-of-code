from pprint import pprint
import math
import timeit


def read_file(filename):
    buffer = []
    with open(filename) as f:
        line = f.readline()
        while line:
            buffer.append(line.strip())
            line = f.readline()

    acc, result = [], []
    for line in buffer:
        if line != "":
            acc.append(line)
        else:
            result.append(acc)
            acc = []

    result.append(acc)
    return result


def check_coords(coords, is_rows=False):
    idxs_to_check = []
    for i, row1 in coords.items():
        for j, row2 in coords.items():
            if i != j and i < j:
                diff = None
                if len(row1) > len(row2):
                    diff = list(set(row1) - set(row2))
                else:
                    diff = list(set(row2) - set(row1))

                if (
                    len(diff) == 1
                    and (i + j) % 2 != 0
                    and abs(len(row1) - len(row2)) == 1
                ):
                    idxs_to_check.append(
                        (math.floor((i + j) / 2), math.ceil((i + j) / 2))
                    )

    for top, bottom in idxs_to_check:
        topp, bottomm = top, bottom
        valid = True
        changed_once = False
        while top >= 0 and bottom < len(coords):
            if coords[top] != coords[bottom]:
                if not changed_once:
                    changed_once = True
                else:
                    valid = False
                    break
            top -= 1
            bottom += 1

        if valid:
            return 100 * bottomm if is_rows else bottomm

    return None


def solve(pattern):
    # first check rows
    row_coords = {}
    for r, row in enumerate(pattern):
        row_coords[r] = []
        for c, elem in enumerate(row):
            if elem == "#":
                row_coords[r].append(c)

    row_ans = check_coords(row_coords, True)
    if row_ans:
        return row_ans

    # check cols
    col_coords = {}
    for c in range(len(pattern[0])):
        col = [pattern[i][c] for i in range(len(pattern))]
        col_coords[c] = []
        for r, elem in enumerate(col):
            if elem == "#":
                col_coords[c].append(r)

    col_ans = check_coords(col_coords)
    if col_ans:
        return col_ans

    return "IF YOU GOT HERE SOMETHINGS BROKEN"


def solution(filename):
    patterns = read_file(filename)

    ans = 0
    for pattern in patterns:
        ans += solve(pattern)
    return ans


if __name__ == "__main__":
    small = "input_small.txt"
    large = "input_large.txt"

    print(solution(small))
    print(solution(large))
