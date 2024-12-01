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
    queue.append((start[0], start[1], 0, 0))

    for i in range(5000):
        start_time = time.time()
        visited = set()

        len_to_pop = len(queue)
        for __ in range(len_to_pop):
            x, y, board_x, board_y = queue.popleft()

            # up
            if x - 1 < 0:
                new_x = rows + (x - 1)
                if (
                    graph[new_x][y] in (".", "S")
                    and (new_x, y, board_x - 1, board_y) not in visited
                ):
                    queue.append((new_x, y, board_x - 1, board_y))
                    visited.add((new_x, y, board_x - 1, board_y))
            else:
                if (
                    graph[x - 1][y] in (".", "S")
                    and (x - 1, y, board_x, board_y) not in visited
                ):
                    queue.append((x - 1, y, board_x, board_y))
                    visited.add((x - 1, y, board_x, board_y))

            # down
            if x + 1 >= rows:
                new_x = x + 1 - rows
                if (
                    graph[new_x][y] in (".", "S")
                    and (new_x, y, board_x + 1, board_y) not in visited
                ):
                    queue.append((new_x, y, board_x + 1, board_y))
                    visited.add((new_x, y, board_x + 1, board_y))
            else:
                if (
                    graph[x + 1][y] in (".", "S")
                    and (x + 1, y, board_x, board_y) not in visited
                ):
                    queue.append((x + 1, y, board_x, board_y))
                    visited.add((x + 1, y, board_x, board_y))

            # left
            if y - 1 < 0:
                new_y = cols + (y - 1)
                if (
                    graph[x][new_y] in (".", "S")
                    and (x, new_y, board_x, board_y - 1) not in visited
                ):
                    queue.append((x, new_y, board_x, board_y - 1))
                    visited.add((x, new_y, board_x, board_y - 1))
            else:
                if (
                    graph[x][y - 1] in (".", "S")
                    and (x, y - 1, board_x, board_y) not in visited
                ):
                    queue.append((x, y - 1, board_x, board_y))
                    visited.add((x, y - 1, board_x, board_y))

            # right
            if y + 1 >= cols:
                new_y = y + 1 - cols
                if (
                    graph[x][new_y] in (".", "S")
                    and (x, new_y, board_x, board_y + 1) not in visited
                ):
                    queue.append((x, new_y, board_x, board_y + 1))
                    visited.add((x, new_y, board_x, board_y + 1))
            else:
                if (
                    graph[x][y + 1] in (".", "S")
                    and (x, y + 1, board_x, board_y) not in visited
                ):
                    queue.append((x, y + 1, board_x, board_y))
                    visited.add((x, y + 1, board_x, board_y))

        end_time = time.time()
        final_time = end_time - start_time
        print(f"iteration {i} visited {len(visited)} in {final_time:.5f} seconds")

    return len(visited)


def solution(filename):
    graph = read_file(filename)
    return solve(graph)


if __name__ == "__main__":
    start_time = time.time()
    small = "input_small.txt"
    large = "input_large.txt"

    print(solution(small))
    # print(solution(large))
    end_time = time.time()
    print(Fore.GREEN + f"code ran in {end_time-start_time:.5f} seconds")
