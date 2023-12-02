def read_input(filename):
  buffer = []
  with open(filename) as f:
      line = f.readline()
      while line:
          buffer.append(line.strip())
          line = f.readline()

  return buffer

# part 1
def solution():
  input = read_input('input.txt')
  
  nums = []
  for line in input:
    nums_for_line = []
    for char in line:
      if char.isdigit():
        nums_for_line.append(char)

    if len(nums_for_line) == 1:
      nums.append(nums_for_line[0] * 2)
    else:
      nums.append(nums_for_line[0] + nums_for_line[-1])

  ans = 0
  for num in nums:
    num = int(num)
    ans += num

  return ans

# part 2
def solution2():
  input = read_input('input_large.txt')

  def get_lo_and_hi_number(line):
    mapping = {
      '1': "one",
      '2': "two",
      '3': "three",
      '4': "four",
      '5': "five",
      '6': "six",
      '7': "seven",
      '8': "eight",
      '9': "nine"
    }
    info = {}

    for number in mapping.values():
      res = [i for i in range(len(line)) if line.startswith(number, i)]
      info[number] = res

    for idx, char in enumerate(line):
      if char.isdigit():
        info[mapping[char]].append(idx)

    mini, min_val = "", len(line) + 1
    maxi, max_val = "", -1

    for key, vals in info.items():
      for val in vals:
        if val > max_val: 
          maxi = key
          max_val = val

        if val < min_val: 
          mini = key
          min_val = val

    reversed_mapping = dict((v, k) for k, v in mapping.items())
    return [reversed_mapping[mini], reversed_mapping[maxi]]
  
  nums = []
  for line in input:
    nums_for_line = get_lo_and_hi_number(line)

    if len(nums_for_line) == 1:
      nums.append(nums_for_line[0] * 2)
    else:
      nums.append(nums_for_line[0] + nums_for_line[-1])

  ans = 0
  for num in nums: ans += int(num)
  return ans

print(solution2())
