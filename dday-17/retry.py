from pprint import pprint
import collections
from enum import Enum
import heapq


def read_file(filename, t=False):
    lines = [line.strip() for line in open(filename)]
    return [[int(i) for i in line] for line in lines]


def is_valid(x, y, rows, cols):
    return x >= 0 and x < rows and y >= 0 and y < cols


class Dir(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


dir_mapping = {Dir.UP: (1, 0), Dir.DOWN: (-1, 0), Dir.LEFT: (0, -1), Dir.RIGHT: (0, 1)}


def get_dirs_from_current_path(path):
    if len(path) < 3:
        return [Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT]

    (a, a_dir), (b, b_dir), (c, c_dir) = path[-3], path[-2], path[-1]

    # if the same row
    if a[0] == b[0] == c[0]:
        if c[1] - b[1] == b[1] - a[1]:
            if a_dir == b_dir == c_dir:
                # cannot go left/right
                return [Dir.UP, Dir.DOWN]

    # if the same column
    if a[1] == b[1] == c[1]:
        if c[0] - b[0] == b[0] - a[0]:
            if a_dir == b_dir == c_dir:
                # cannot go up/down
                return [Dir.LEFT, Dir.RIGHT]

    return [Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT]

def solve(graph):
    ans = []
    rows, cols = len(graph), len(graph[0])

    parents_map = {}

    visited = set()
    queue = []
    node_costs = collections.defaultdict(lambda: float("inf"))
    node_costs[(0, 0)] = 0

    start = (0, (0, 0), [((0, 0), Dir.RIGHT)])
    heapq.heappush(queue, start)

    while queue:
        _, point, path = heapq.heappop(queue)
        acceptable_dirs = get_dirs_from_current_path(path)
        visited.add(point)

        for dir in acceptable_dirs:
            new_point = (point[0] + dir_mapping[dir][0], point[1] + dir_mapping[dir][1])
            if is_valid(new_point[0], new_point[1], rows, cols) and new_point not in visited:
                visited.add(new_point)

                new_cost = node_costs[point] + graph[new_point[0]][new_point[1]]
                if node_costs[(new_point[0], new_point[1])] > new_cost:
                    node_costs[(new_point[0], new_point[1])] = new_cost
                    parents_map[new_point] = point
                    new_path = path + [(new_point, dir)]
                    heapq.heappush(queue, (new_cost, new_point, new_path))

    path = []
    start = (rows-1, cols-1)
    while start != (0, 0):
        path.insert(0, parents_map[start])
        start = parents_map[start]
    pprint(path)
    start = (rows-1, cols-1)
    pprint(node_costs[start])

    new_board = [["." for _ in range(cols)] for _ in range(rows)]
    for x, y in path:
        new_board[x][y] = "#"
    for line in new_board:
        pprint(line)

def solution(filename):
    graph = read_file(filename)
    solve(graph)


if __name__ == "__main__":
    small = "input_small.txt"
    large = "input_large.txt"

    print(solution(small))
    # print(solution(large))
