from collections import Counter


def solution(file_name: str):
	input = []

	with open(file_name) as input_file:
		line = input_file.readline()
		while line:
			input.append(line.strip())
			line = input_file.readline()

	arr1, arr2 = [], []
	for line in input:
		splitted = line.split()
		arr1.append(int(splitted[0]))
		arr2.append(int(splitted[1]))

	right_arr_counter = Counter(arr2)
	similarity_score = 0

	for num in arr1:
		similarity_score += num * right_arr_counter.get(num, 0)

	return similarity_score
	
print(solution("sample.txt"))
print(solution("full.txt"))
