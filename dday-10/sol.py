from pprint import pprint


def read_file(filename):
    buffer = []
    with open(filename) as f:
        line = f.readline()
        while line:
            buffer.append([c for c in line.strip()])
            line = f.readline()

    return buffer


def find_start(graph):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == "S":
                return i, j

    raise Exception("could not find start position 'S'")


def is_on_board(x, y, rows, cols):
    return not (x >= rows or x < 0 or y >= cols or y < 0)


def mapping(cur_point, direction):
    if direction == "up":
        if cur_point in ["F", "7", "-"]:
            return []
        else:
            return ["|", "F", "7"]

    if direction == "down":
        if cur_point in ["L", "J", "-"]:
            return []
        else:
            return ["|", "L", "J"]

    if direction == "left":
        if cur_point in ["F", "L", "|"]:
            return []
        else:
            return ["F", "L", "-"]

    if direction == "right":
        if cur_point in ["J", "7", "|"]:
            return []
        else:
            return ["J", "7", "-"]


def get_path_set(graph):
    x, y = find_start(graph)
    rows, cols = len(graph), len(graph[0])
    first_time = True
    seen = set()

    while first_time or graph[x][y] != "S":
        if graph[x][y] == "S":
            if first_time:
                first_time = False
            else:
                break

        # up
        if (
            is_on_board(x - 1, y, rows, cols)
            and graph[x - 1][y] in mapping(graph[x][y], "up")
            and (x - 1, y) not in seen
        ):
            seen.add((x - 1, y))
            x -= 1

        # down
        elif (
            is_on_board(x + 1, y, rows, cols)
            and graph[x + 1][y] in mapping(graph[x][y], "down")
            and (x + 1, y) not in seen
        ):
            seen.add((x + 1, y))
            x += 1

        # left
        elif (
            is_on_board(x, y - 1, rows, cols)
            and graph[x][y - 1] in mapping(graph[x][y], "left")
            and (x, y - 1) not in seen
        ):
            seen.add((x, y - 1))
            y -= 1

        # right
        elif (
            is_on_board(x, y + 1, rows, cols)
            and graph[x][y + 1] in mapping(graph[x][y], "right")
            and (x, y + 1) not in seen
        ):
            seen.add((x, y + 1))
            y += 1

        else:
            break

    return seen


def find_s_replacement(graph):
    (x, y) = find_start(graph)
    rows, cols = len(graph), len(graph[0])

    valid_neighbours = []

    # down
    if is_on_board(x + 1, y, rows, cols) and graph[x + 1][y] in ["L", "J", "|"]:
        valid_neighbours.append("down")
    # up
    if is_on_board(x - 1, y, rows, cols) and graph[x - 1][y] in ["7", "F", "|"]:
        valid_neighbours.append("up")
    # left
    if is_on_board(x, y - 1, rows, cols) and graph[x][y - 1] in ["F", "L", "-"]:
        valid_neighbours.append("left")
    # right
    if is_on_board(x, y + 1, rows, cols) and graph[x][y + 1] in ["7", "J", "-"]:
        valid_neighbours.append("right")

    valid_neighbours.sort()

    if valid_neighbours == ["down", "up"]:
        return "|"
    if valid_neighbours == ["left", "right"]:
        return "-"
    if valid_neighbours == ["down", "right"]:
        return "F"
    if valid_neighbours == ["down", "left"]:
        return "7"
    if valid_neighbours == ["left", "up"]:
        return "J"
    if valid_neighbours == ["right", "up"]:
        return "L"


def get_area_inside_path(graph, path_set):
    pipe = find_s_replacement(graph)
    (x, y) = find_start(graph)
    path_set.add((x, y))
    graph[x][y] = pipe
    rows, cols = len(graph), len(graph[0])
    area = 0

    for x in range(rows):
        is_outside = True
        for y in range(cols):
            coord = (x, y)
            if coord not in path_set:
                if not is_outside:
                    area += 1
            else:
                # coordinate is part of path, so we flip flag
                if graph[x][y] in ["|", "F", "7"]:
                    is_outside = not is_outside

    return area


def solution(filename):
    graph = read_file(filename)
    path_set = get_path_set(graph)
    return get_area_inside_path(graph, path_set)


if __name__ == "__main__":
    small = "input_small.txt"
    large = "input_large.txt"

    print(solution(small))
    print(solution(large))
