import collections
import pprint
import sys
import time
sys.setrecursionlimit(15000000)


def part_1_solution(file_name: str):
    input = []

    with open(file_name) as input_file:
        line = input_file.readline()
        while line:
            input.append(list(line.strip()))
            line = input_file.readline()

    rows, cols = len(input), len(input[0])

    visited = set()

    def dfs(x, y, c, counter):
        if x < 0 or x >= rows or y < 0 or y >= rows or input[x][y] != c:
            return 0
        if (x, y) in visited:
            return 0

        visited.add((x, y))
        input[x][y] = counter

        ans = 1
        ans += dfs(x + 1, y, c, counter)
        ans += dfs(x - 1, y, c, counter)
        ans += dfs(x, y + 1, c, counter)
        ans += dfs(x, y - 1, c, counter)
        return ans

    letter_to_size = {}
    counter = 0
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                res = dfs(i, j, input[i][j], counter)
                letter_to_size[counter] = res
                counter += 1

    ans = 0
    for i in range(0, counter):
        perimeter = 0
        for row in input:
            inside = False
            for x in range(len(row)):
                if row[x] == i:
                    if not inside:
                        perimeter += 1
                        inside = True
                elif row[x] != i and inside:
                    perimeter += 1
                    inside = False
            if inside:
                perimeter += 1

        for col in range(cols):
            entire_col = [input[i][col] for i in range(rows - 1, -1, -1)]
            inside = False
            for x in range(len(entire_col)):
                if entire_col[x] == i:
                    if not inside:
                        perimeter += 1
                        inside = True
                elif entire_col[x] != i and inside:
                    perimeter += 1
                    inside = False
            if inside:
                perimeter += 1

        ans += letter_to_size[i] * perimeter
    return ans


def part_2_solution(file_name: str):
    input = []

    with open(file_name) as input_file:
        line = input_file.readline()
        while line:
            input.append(list(line.strip()))
            line = input_file.readline()

    rows, cols = len(input), len(input[0])

    visited = set()

    def dfs(x, y, c, counter):
        if x < 0 or x >= rows or y < 0 or y >= rows or input[x][y] != c:
            return 0
        if (x, y) in visited:
            return 0

        visited.add((x, y))
        input[x][y] = counter

        ans = 1
        ans += dfs(x + 1, y, c, counter)
        ans += dfs(x - 1, y, c, counter)
        ans += dfs(x, y + 1, c, counter)
        ans += dfs(x, y - 1, c, counter)
        return ans

    letter_to_size = {}
    counter = 0
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                res = dfs(i, j, input[i][j], counter)
                letter_to_size[counter] = res
                counter += 1

    ans = 0
    for i in range(0, counter):
        sides = 0
        same_cols_start = set()
        same_cols_end = set()
        for row_index, row in enumerate(input):
            inside = False
            for x in range(len(row)):
                if row[x] == i:
                    if not inside:
                        if (row_index - 1, x) not in same_cols_start:
                            sides += 1
                        same_cols_start.add((row_index, x))
                        inside = True
                elif row[x] != i and inside:
                    if (row_index - 1, x - 1) not in same_cols_end:
                        sides += 1
                    same_cols_end.add((row_index, x - 1))
                    inside = False
            if inside:
                same_cols_end.add((row_index, x))
            if inside and (row_index - 1, x) not in same_cols_end:
                sides += 1

        same_rows_start = set()
        same_rows_end = set()
        for col in range(cols):
            entire_col = [input[i][col] for i in range(rows - 1, -1, -1)]
            inside = False
            for x in range(len(entire_col)):
                if entire_col[x] == i:
                    if not inside:
                        if (col - 1, x) not in same_rows_start:
                            sides += 1
                        same_rows_start.add((col, x))
                        inside = True
                elif entire_col[x] != i and inside:
                    if (col - 1, x - 1) not in same_rows_end:
                        sides += 1
                    same_rows_end.add((col, x - 1))
                    inside = False
            if inside:
                same_rows_end.add((col, x))
            if inside and (col - 1, x) not in same_rows_end:
                sides += 1

        ans += letter_to_size[i] * sides
    return ans


def time_function(func, *args):
	start_time = time.time()
	result = func(*args)
	end_time = time.time()
	elapsed_time = int((end_time - start_time) * 1000)  # Convert to milliseconds and cast to int
	input_type = "sample" if "sample" in args[0] else "full"
	part = "part 1" if "part_1" in func.__name__ else "part 2"
	print(f"{input_type} input {part} took {elapsed_time} milliseconds and returned {result}")

time_function(part_1_solution, "sample.txt")
time_function(part_1_solution, "full.txt")
time_function(part_2_solution, "sample.txt")
time_function(part_2_solution, "full.txt")
