from pprint import pprint
from collections import deque
import time
from colorama import Fore


def read_file(filename, t=False):
    lines = [line.strip() for line in open(filename)]
    return [[i for i in line] for line in lines]


def find_start(graph):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == "S":
                return (i, j)

    return (-1, -1)


def on_board(x, y, rows, cols):
    return x >= 0 and x < rows and y >= 0 and y < cols


def solve(graph):
    rows, cols = len(graph), len(graph[0])
    queue = deque()

    start = find_start(graph)
    queue.append(start)

    for _ in range(64):
        visited = set()

        len_to_pop = len(queue)
        for __ in range(len_to_pop):
            x, y = queue.popleft()

            # up
            if (
                on_board(x - 1, y, rows, cols)
                and graph[x - 1][y] in (".", "S")
                and (x - 1, y) not in visited
            ):
                queue.append((x - 1, y))
                visited.add((x - 1, y))

            # down
            if (
                on_board(x + 1, y, rows, cols)
                and graph[x + 1][y] in (".", "S")
                and (x + 1, y) not in visited
            ):
                queue.append((x + 1, y))
                visited.add((x + 1, y))

            # left
            if (
                on_board(x, y - 1, rows, cols)
                and graph[x][y - 1] in (".", "S")
                and (x, y - 1) not in visited
            ):
                queue.append((x, y - 1))
                visited.add((x, y - 1))

            # right
            if (
                on_board(x, y + 1, rows, cols)
                and graph[x][y + 1] in (".", "S")
                and (x, y + 1) not in visited
            ):
                queue.append((x, y + 1))
                visited.add((x, y + 1))

    return len(visited)


def solution(filename):
    graph = read_file(filename)
    return solve(graph)


if __name__ == "__main__":
    start_time = time.time()
    small = "input_small.txt"
    large = "input_large.txt"

    print(solution(small))
    print(solution(large))
    end_time = time.time()
    print(Fore.GREEN + f"code ran in {end_time-start_time:.5f} seconds")
