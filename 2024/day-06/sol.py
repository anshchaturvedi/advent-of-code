import sys
import time
sys.setrecursionlimit(15000000)


def part_1_solution(file_name: str):
	input = []

	with open(file_name) as input_file:
		line = input_file.readline()
		while line:
			input.append([i for i in line.strip()])
			line = input_file.readline()
	
	dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	rows, cols = len(input), len(input[0])
	x, y = None, None

	for i in range(rows):
		for j in range(cols):
			if input[i][j] == "^": x, y = i, j

	visited = set([(x, y)])

	def dfs(x, y, i):
		if x < 0 or x >= rows or y < 0 or y >= cols: return
		visited.add((x, y))
		new_x, new_y = x + dirs[i][0], y + dirs[i][1]
		input[x][y] = "X"

		if 0 <= new_x < rows and 0 <= new_y < cols and input[new_x][new_y] == "#":
			i = (i + 1) % len(dirs)
			dfs(x, y, i)
		else:
			dfs(new_x, new_y, i)
	
	dfs(x, y, 0)
	return len(visited)


def part_2_solution(file_name: str):
	input = []

	with open(file_name) as input_file:
		line = input_file.readline()
		while line:
			input.append([i for i in line.strip()])
			line = input_file.readline()
	
	dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	rows, cols = len(input), len(input[0])
	x, y = None, None

	for i in range(rows):
		for j in range(cols):
			if input[i][j] == "^": x, y = i, j

	full_path_trace = set([(x, y)])

	def trace_initial_path(x, y, i):
		if x < 0 or x >= rows or y < 0 or y >= cols: return
		full_path_trace.add((x, y))
		new_x, new_y = x + dirs[i][0], y + dirs[i][1]

		if 0 <= new_x < rows and 0 <= new_y < cols and input[new_x][new_y] == "#":
			i = (i + 1) % len(dirs)
			trace_initial_path(x, y, i)
		else:
			trace_initial_path(new_x, new_y, i)
	
	trace_initial_path(x, y, 0)

	def dfs(x, y, i, visited):
		if x < 0 or x >= rows or y < 0 or y >= cols: return 0
		if (x, y, i) in visited: return 1

		visited.add((x, y, i))
		new_x, new_y = x + dirs[i][0], y + dirs[i][1]

		if 0 <= new_x < rows and 0 <= new_y < cols and input[new_x][new_y] == "#":
			i = (i + 1) % len(dirs)
			return dfs(x, y, i, visited)
		else:
			return dfs(new_x, new_y, i, visited)

	ans = 0
	for (i, j) in list(full_path_trace):
		if input[i][j] == ".":
			input[i][j] = "#"
			ans += dfs(x, y, 0, set())
			input[i][j] = "."
	return ans	


def time_function(func, *args):
	start_time = time.time()
	result = func(*args)
	end_time = time.time()
	input_type = "sample" if "sample" in args[0] else "full"
	part = "part 1" if "part_1" in func.__name__ else "part 2"
	print(f"{input_type} input {part} took {end_time - start_time:.3f} seconds and returned {result}")

time_function(part_1_solution, "sample.txt")
time_function(part_1_solution, "full.txt")
time_function(part_2_solution, "sample.txt")
time_function(part_2_solution, "full.txt")
