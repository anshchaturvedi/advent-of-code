import collections
import pprint


def part_1_solution(file_name: str):
	input = []

	with open(file_name) as input_file:
		line = input_file.readline()
		while line:
			input.append(line.strip())
			line = input_file.readline()

	divider = input.index('')
	edges, queries = input[:divider], input[divider+1:]
	graph = collections.defaultdict(list)

	for edge in edges:
		u, v = edge.split('|')
		graph[int(u)].append(int(v))
	
	

def part_2_solution(file_name: str):
	input = []

	with open(file_name) as input_file:
		line = input_file.readline()
		while line:
			input.append(line.strip())
			line = input_file.readline()


print(part_1_solution("sample.txt"))
# print(part_1_solution("full.txt"))

# print(part_2_solution("sample.txt"))
# print(part_2_solution("full.txt"))

