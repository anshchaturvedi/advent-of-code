def solution(file_name: str):
	with open(file_name) as input_file:
		line = input_file.readline()
		line = line[0:len(line)-1]

		res = 0
		for nums in line.split(","):
			nums = nums.split("-")
			num1, num2 = int(nums[0]), int(nums[1])
			s_num1 = str(num1)

			# lower bound can't have any invalid IDs if length
			# is odd, so move to next possible base
			if len(str(num1)) % 2 != 0:
				updated_len = len(s_num1)
				num1 = 10 ** updated_len
				s_num1 = str(num1)

			# invalid IDs can only be created with an even digit count
			half = int(s_num1[:len(s_num1) // 2])
			while int(str(half) + str(half)) <= num2:
				to_add = int(str(half) + str(half))
				if num1 <= to_add: res += to_add
				half += 1
	
		return res

print("ans: " + str(solution("sample.txt")))
print("ans: " + str(solution("full.txt")))

# print("ans: " + str(solution_part2("sample.txt")))
# print("ans: " + str(solution_part2("full.txt")))
