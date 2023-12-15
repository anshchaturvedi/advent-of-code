from pprint import pprint

def read_file(filename):
  string = [line.strip() for line in open(filename)]
  return string[0].split(',')

def get_hash(string):
  start = 0
  for i in range(len(string)):
    start += ord(string[i])
    start *= 17
    start %= 256
  return start

def solution(filename):
  strings = read_file(filename)
  ans = 0
  for string in strings:
    ans += get_hash(string)
  return ans

if __name__ == "__main__":
  small = "input_small.txt"
  large = "input_large.txt"

  print(solution(small))
  # print(solution(large))
