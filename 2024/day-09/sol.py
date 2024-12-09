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

	
def part_2_solution(file_name: str):
	input = []

	with open(file_name) as input_file:
		line = input_file.readline()
		while line:
			input.append(list(line.strip()))
			line = input_file.readline()

def time_function(func, *args):
	start_time = time.time()
	result = func(*args)
	end_time = time.time()
	elapsed_time = int((end_time - start_time) * 1000)  # Convert to milliseconds and cast to int
	input_type = "sample" if "sample" in args[0] else "full"
	part = "part 1" if "part_1" in func.__name__ else "part 2"
	print(f"{input_type} input {part} took {elapsed_time} milliseconds and returned {result}")

time_function(part_1_solution, "sample.txt")
# time_function(part_1_solution, "full.txt")
# time_function(part_2_solution, "sample.txt")
# time_function(part_2_solution, "full.txt")
