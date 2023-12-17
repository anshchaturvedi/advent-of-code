from pprint import pprint
from collections import defaultdict
import heapq


def read_file(filename, t=False):
    lines = [line.strip() for line in open(filename)]
    if not t:
        return [[int(i) for i in line] for line in lines]
    else:
        return [[i for i in line] for line in lines]


def is_valid(x, y, rows, cols):
    return x >= 0 and x < rows and y >= 0 and y < cols


def get_dir(dx, dy):
    if dx == 1 and dy == 0:
        return "right"
    if dx == -1 and dy == 0:
        return "left"
    if dx == 0 and dy == 1:
        return "down"
    if dx == 0 and dy == -1:
        return "up"


def get_acceptable_dirs(path):
    if len(path) < 3:
        return None

    (a, a_dir), (b, b_dir), (c, c_dir) = path[-3], path[-2], path[-1]

    # if the same row
    if a[0] == b[0] == c[0]:
        if c[1] - b[1] == b[1] - a[1]:
            if a_dir == b_dir == c_dir:
                # cannot go left/right
                return "up, down"

    # if the same column
    if a[1] == b[1] == c[1]:
        if c[0] - b[0] == b[0] - a[0]:
            if a_dir == b_dir == c_dir:
                # cannot go up/down
                return "left, right"

    return "up, down, left, right"


def solve(graph):
    rows, cols = len(graph), len(graph[0])
    visited = set()
    parents_map = {}
    pq = []
    node_costs = defaultdict(lambda: float("inf"))
    node_costs[(0, 0)] = 0
    # entry in pq is (cost, node, node_path)
    heapq.heappush(pq, (0, (0, 0), [((0, 0), "right")]))

    while len(pq) > 0:
        _, (x, y), path = heapq.heappop(pq)
        visited.add((x, y))

        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, rows, cols):
                if (new_x, new_y) in visited:
                    continue

                acceptable_dirs = get_acceptable_dirs(path)

                if acceptable_dirs == "left, right" and dx in [1, -1]:
                    continue
                elif acceptable_dirs == "up, down" and dy in [-1, 1]:
                    continue
                else:
                    cur_dir = get_dir(dx, dy)

                    new_cost = node_costs[(x, y)] + graph[new_x][new_y]
                    if node_costs[(new_x, new_y)] > new_cost:
                        parents_map[(new_x, new_y)] = (x, y)
                        node_costs[(new_x, new_y)] = new_cost
                        new_path = path + [((new_x, new_y), cur_dir)]
                        heapq.heappush(pq, (new_cost, (new_x, new_y), new_path))

    return node_costs, parents_map


def solution(filename):
    board = read_file(filename)
    rows, cols = len(board), len(board[0])
    a, b = solve(board)
    pprint(a[(rows - 1, cols - 1)])
    path = []
    print(rows, cols)
    start = (rows - 1, cols - 1)
    while start in b:
        path.insert(0, b[start])
        start = b[start]
    path.insert(0, (rows - 1, cols - 1))

    new_board = [["." for _ in range(cols)] for _ in range(rows)]
    for x, y in path:
        new_board[x][y] = "#"
    for line in new_board:
        pprint(line)

    new_board = read_file("input_exp.txt", True)
    for r in range(rows):
        for c in range(cols):
            if not new_board[r][c].isdigit():
                new_board[r][c] = "#"
            else:
                new_board[r][c] = "."
    new_board[0][0] = "#"

    print()
    for line in new_board:
        pprint(line)
    new_board = [["." for _ in range(cols)] for _ in range(rows)]

    # print(path)


if __name__ == "__main__":
    small = "input_small.txt"
    large = "input_large.txt"

    print(solution(small))
    # print(solution(large))
