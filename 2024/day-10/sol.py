import collections
from functools import lru_cache
import pprint
import sys
import time
sys.setrecursionlimit(15000000)


def part_1_solution(file_name: str):
	input = []

	with open(file_name) as input_file:
		line = input_file.readline()
		while line:
			input.append(list(map(int, list(line.strip()))))
			line = input_file.readline()

	rows, cols = len(input), len(input[0])

	seen = set()
	def dfs(x, y, cur):
		if x < 0 or x >= rows or y < 0 or y >= cols or input[x][y] != cur: return
		
		if input[x][y] == cur:
			if cur == 9: seen.add((x, y))
			else:
				dfs(x+1, y, cur + 1)
				dfs(x-1, y, cur + 1)
				dfs(x, y-1, cur + 1)
				dfs(x, y+1, cur + 1)
		
	ans = 0
	for i in range(rows):
		for j in range(cols):
			if input[i][j] == 0:
				dfs(i, j, 0)
				ans += len(seen)
				seen = set()

	return ans


def part_2_solution(file_name: str):
	input = []

	with open(file_name) as input_file:
		line = input_file.readline()
		while line:
			input.append(list(map(int, list(line.strip()))))
			line = input_file.readline()

	rows, cols = len(input), len(input[0])

	def dfs(x, y, cur):
		if x < 0 or x >= rows or y < 0 or y >= cols or input[x][y] != cur:
			return 0
		
		if input[x][y] == cur:
			if cur == 9: return 1
			else: return (
				dfs(x+1, y, cur + 1) + 
				dfs(x-1, y, cur + 1) + 
        dfs(x, y-1, cur + 1) +
        dfs(x, y+1, cur + 1)
      )
		else: return 0
		
	ans = 0
	for i in range(rows):
		for j in range(cols):
			if input[i][j] == 0: ans += dfs(i, j, 0)

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
