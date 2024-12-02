def solution(file_name: str):
	input = []

	with open(file_name) as input_file:
		line = input_file.readline()
		while line:
			input.append(list(map(int,line.strip().split())))
			line = input_file.readline()

	ans = 0
	for report in input:
		increasing = all(report[i] < report[i+1] for i in range(len(report) - 1))
		decreasing = all(report[i] > report[i+1] for i in range(len(report) - 1))
		if not increasing and not decreasing:
			continue
		if (increasing or decreasing) and all(abs(report[i+1] - report[i]) <= 3 for i in range(len(report) - 1)):
			ans += 1
	return ans

print(solution("sample.txt"))
print(solution("full.txt"))
