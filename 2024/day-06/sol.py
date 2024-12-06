import pprint
import sys
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

	visited = set([x, y])

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
	ans = 0
	for row in input: ans += row.count("X")
	return ans
				


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

	def dfs(x, y, bad_x, bad_y, i, visited):
		if x < 0 or x >= rows or y < 0 or y >= cols: return 0
		if (x, y, i) in visited: return 1

		visited.add((x, y, i))
		new_x, new_y = x + dirs[i][0], y + dirs[i][1]

		if 0 <= new_x < rows and 0 <= new_y < cols and input[new_x][new_y] == "#":
			i = (i + 1) % len(dirs)
			return dfs(x, y, bad_x, bad_y, i, visited)
		elif new_x == bad_x and new_y == bad_y:
			i = (i + 1) % len(dirs)
			return dfs(x, y, bad_x, bad_y, i, visited)
		else:
			return dfs(new_x, new_y, bad_x, bad_y, i, visited)

	ans = 0
	for i in range(rows):
		for j in range(cols):
			if input[i][j] == ".":
				ans += dfs(x, y, i, j, 0, set())
	return ans	


print(part_1_solution("sample.txt"))
print(part_1_solution("full.txt"))

print(part_2_solution("sample.txt"))
print(part_2_solution("full.txt"))
