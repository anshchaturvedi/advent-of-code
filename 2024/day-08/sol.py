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

	antennas = collections.defaultdict(list)
	for i in range(rows):
		for j in range(cols):
			if input[i][j] != ".":
				antennas[input[i][j]].append((i, j))
	res = set()

	for points in antennas.values():
		points.sort()
		n = len(points)
		for i in range(n):
			for j in range(i+1, n):
				rise = abs(points[j][0] - points[i][0])
				run = abs(points[j][1] - points[i][1])
				if points[i][1] <= points[j][1]:
					res.add((points[i][0] - rise, points[i][1] - run))
					res.add((points[j][0] + rise, points[j][1] + run))

				else:
					res.add((points[j][0] + rise, points[j][1] - run))
					res.add((points[i][0] - rise, points[i][1] + run))
	ans = 0
	for i, j in res:
		if i in range(rows) and j in range(cols): ans += 1
	return ans
	
def part_2_solution(file_name: str):
	input = []

	with open(file_name) as input_file:
		line = input_file.readline()
		while line:
			input.append(list(line.strip()))
			line = input_file.readline()

	rows, cols = len(input), len(input[0])

	antennas = collections.defaultdict(list)
	for i in range(rows):
		for j in range(cols):
			if input[i][j] != ".":
				antennas[input[i][j]].append((i, j))
	res = set()

	for points in antennas.values():
		points.sort()
		n = len(points)
		for i in range(n):
			for j in range(i+1, n):
				rise = abs(points[j][0] - points[i][0])
				run = abs(points[j][1] - points[i][1])
				if points[i][1] <= points[j][1]:
					for k in range(1, 100):
						res.add((points[i][0] - (rise * k), points[i][1] - (run * k)))
						res.add((points[j][0] + (rise * k), points[j][1] + (run * k)))

				else:
					for k in range(1, 100):
						res.add((points[j][0] + (rise * k), points[j][1] - (run * k)))
						res.add((points[i][0] - (rise * k), points[i][1] + (run * k)))
	ans = 0
	for i, j in res:
		if i in range(rows) and j in range(cols):
			if input[i][j] == ".": input[i][j] = "#"
	for row in input:
		for a in row:
			if a != ".": ans += 1
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
