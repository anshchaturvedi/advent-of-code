import collections
from functools import lru_cache
import pprint
import sys
import time
sys.setrecursionlimit(15000000)

def part_1_solution(file_name: str):
	with open(file_name) as input_file:
		line = list(map(int, input_file.readline().split()))

	for _ in range(25):
		new = []
		for num in line:
			if num == 0: new.append(1)
			elif len(str(num)) % 2 == 0:
				a = str(num)
				mid = len(a) // 2
				new.append(int(a[:mid]))
				new.append(int(a[mid:]))
			else:
				new.append(num * 2024)
		line = new
	
	return len(line)

def part_2_solution(file_name: str):
	with open(file_name) as input_file:
		line = list(map(int, input_file.readline().split()))

	cur = collections.Counter(line)
	for _ in range(75):
		new = collections.Counter()
		for num in cur:
			if num == 0: new[1] = new.get(1, 0) + cur[0]
			elif len(str(num)) % 2 == 0:
				a = str(num)
				mid = len(a) // 2
				new[int(a[:mid])] = new.get(int(a[:mid]), 0) + cur[num]
				new[int(a[mid:])] = new.get(int(a[mid:]), 0) + cur[num]
			else:
				new[2024 * num] = new.get(2024 * num, 0) + cur[num]
		cur = new

	return sum(cur.values())

	
def time_function(func, *args):
	start_time = time.time()
	result = func(*args)
	end_time = time.time()
	elapsed_time = int((end_time - start_time) * 1000)  # Convert to milliseconds and cast to int
	input_type = "sample" if "sample" in args[0] else "full"
	part = "part 1" if "part_1" in func.__name__ else "part 2"
	print(f"{input_type} input {part} took {elapsed_time} milliseconds and returned {result}")


# time_function(part_1_solution, "sample.txt")
time_function(part_1_solution, "full.txt")
# time_function(part_2_solution, "sample.txt")
time_function(part_2_solution, "full.txt")
