from pprint import pprint
from collections import deque


def convert_hex(hex_num):
    decimal_part = int(hex_num[1:6], 16)  # convert the first 5 digits to decimal
    last_digit = hex_num[6]  # get the last digit
    return decimal_part, last_digit


def read_file(filename, t=False):
    lines = [line.strip().split(" ") for line in open(filename)]
    instrs = []
    mapping = {"0": "R", "1": "D", "2": "L", "3": "U"}

    for _, _, hex in lines:
        dist, dir = convert_hex(hex[1:8])
        dir = mapping[dir]
        instrs.append((dist, dir))
    return instrs


def solution(filename):
    instrs = read_file(filename)

    directions = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}
    x, y = 0, 0
    all_corners = []
    all_corners.append((0, 0))
    boundary_area = 0

    for dist, dir in instrs:
        dx, dy = directions[dir]
        x += dx * dist
        y += dy * dist
        boundary_area += dist
        all_corners.append((x, y))

    interior_area = 0
    for i in range(len(all_corners) - 1):
        (x1, y1), (x2, y2) = all_corners[i : i + 2]
        interior_area += x1 * y2 - x2 * y1

    return (abs(interior_area) // 2) + (boundary_area // 2) + 1

if __name__ == "__main__":
    small = "input_small.txt"
    large = "input_large.txt"

    print(solution(small))
    print(solution(large))
