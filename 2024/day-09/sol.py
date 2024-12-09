import collections
import pprint
import sys
import time
sys.setrecursionlimit(15000000)


def part_1_solution(file_name: str):

	with open(file_name) as input_file:
		line = input_file.readline()
		
	line = list(map(int, line[:len(line)-1]))

	free = True
	res = []
	counter = 0
	for num in line:
		if free:
			for _ in range(num): res.append(counter)
			counter += 1
			free = not free
		else:
			for _ in range(num): res.append(".")
			free = not free

	i, j = 0, len(res) - 1
	while i < j:
		while res[i] != ".": i += 1
		while res[j] == ".": j -= 1
		res[i], res[j] = res[j], res[i]
		i += 1
		j -= 1

	for i in range(len(res)-1, -1, -1):
		if res[i] == ".": res.pop(i)

	ans = 0
	for a, b in enumerate(res):
		ans += a * b
	return ans
	
def part_2_solution(file_name: str):

	with open(file_name) as input_file:
		line = input_file.readline()
		
	line = list(map(int, line[:len(line)-1]))

	free = True
	res = []
	counter = 0
	sizes = {}
	for num in line:
		if free:
			for _ in range(num): res.append(counter)
			sizes[counter] = num
			counter += 1
			free = not free
		else:
			for _ in range(num): res.append(".")
			free = not free

	free_sizes = []
	p = 0
	inside = False
	cur = [None, None] # start, size
	while p < len(res):
		if res[p] == "." and not inside:
			inside = True
			cur[0], cur[1] = p, 1
		elif res[p] == "." and inside:
			cur[1] = cur[1] + 1
		elif res[p] != "." and inside:
			inside = False
			free_sizes.append(list(cur))
			cur = [None, None]
		p += 1
	# print(free_sizes)

	# count = 0
	ordered = sorted(sizes.keys(), reverse=True)
	for file in ordered:
		# print(f"processing {count} / {len(sizes)}")
		# count += 1
		file_size = sizes[file]

		start_index = res.index(file)
		for free_index, x in enumerate(free_sizes):
			if x == [-1, -1]: continue
			if x[1] >= file_size and x[0] < start_index:
				for i in range(start_index, start_index + file_size):
					res[i] = "."
				for ax in range(x[0], x[0] + file_size):
					res[ax] = file
				if x[1] == file_size:
					free_sizes[free_index] = [-1, -1]
				else:
					x[0] += file_size
					x[1] -= file_size
				break
				
	ans = 0
	for a, b in enumerate(res):
		if b != ".": ans += a * b
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
