def solution(file_name: str):
	input = []

	with open(file_name) as input_file:
		line = input_file.readline()
		while line:
			input.append(line.strip())
			line = input_file.readline()

	start = 50
	ans = 0
    
	for line in input:
		dir, num_to_move = line[0], int(line[1:])
		if dir == "L":
			new = start - num_to_move
		if dir == "R":
			new = start + num_to_move

		start = new % 100
		
		if start == 0: ans += 1
	
	return ans

print("ans: " + str(solution("sample.txt")))
print("ans: " + str(solution("full.txt")))

def solution_part2(file_name: str):
	input = []

	with open(file_name) as input_file:
		line = input_file.readline()
		while line:
			input.append(line.strip())
			line = input_file.readline()

	start = 50
	ans = 0
    
	for line in input:
		dir, num_from_line = line[0], int(line[1:])
		num_to_move, cycles = num_from_line % 100, num_from_line // 100
		ans += cycles

		if dir == "L":
			if num_to_move > start and start != 0:
				# print("got here1", start, dir, num_to_move)
				ans += 1
			new = start - num_to_move
		if dir == "R":
			if num_to_move + start > 100 and start != 0:
				# print("got here2", start, dir, num_to_move)
				ans += 1
			new = start + num_to_move

		start = new % 100
		
		if start == 0:
			# print("got here3", start, dir, num_to_move)
			ans += 1
	
	return ans

print("ans: " + str(solution_part2("sample.txt")))
print("ans: " + str(solution_part2("full.txt")))
