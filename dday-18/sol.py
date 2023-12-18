from pprint import pprint
from collections import deque

# import heapq


def read_file(filename, t=False):
    lines = [line.strip().split(" ") for line in open(filename)]
    return lines


def solution(filename):
    instrs = read_file(filename)

    directions = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}
    x, y = 0, 0
    visited = set()
    visited.add((0, 0))

    for dir, dist, _ in instrs:
        dx, dy = directions[dir]
        for i in range(int(dist)):
            x += dx
            y += dy
            visited.add((x, y))

    queue = deque()
    x, y = min(visited)
    queue.appendleft((x + 1, y + 1))

    while queue:
        x, y = queue.pop()
        for dx, dy in directions.values():
            if (x + dx, y + dy) not in visited:
                new_point = (x+dx, y+dy)
                queue.appendleft(new_point)
                visited.add(new_point)

    return len(visited)


if __name__ == "__main__":
    small = "input_small.txt"
    large = "input_large.txt"

    print(solution(small))
    print(solution(large))
