def solution_part_1(file_name: str):
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

def solution_part_2(file_name: str):
	input = []

	with open(file_name) as input_file:
		line = input_file.readline()
		while line:
			input.append(list(map(int,line.strip().split())))
			line = input_file.readline()

	ans = 0
	for report in input:
		increasing = all(report[i] < report[i+1] and report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
		decreasing = all(report[i] > report[i+1] and report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
		
		if increasing or decreasing: ans += 1
		else:
			for i in range(len(report)):
				new_report = [x for x in report]
				new_report.pop(i)
				new_increasing = all(new_report[i] < new_report[i+1] and new_report[i+1] - new_report[i] <= 3 for i in range(len(new_report) - 1))
				new_decreasing = all(new_report[i] > new_report[i+1] and new_report[i] - new_report[i+1] <= 3 for i in range(len(new_report) - 1))

				if new_increasing or new_decreasing:
					ans += 1
					break

	return ans

print(solution_part_1("sample.txt"))
print(solution_part_1("full.txt"))

print(solution_part_2("sample.txt"))
print(solution_part_2("full.txt"))
