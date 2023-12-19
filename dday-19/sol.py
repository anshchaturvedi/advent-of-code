from pprint import pprint
from collections import deque

def read_file(filename, t=False):
    lines = [line.strip().split(" ") for line in open(filename)]
    return lines


def solution(filename):
    lines = read_file(filename)

if __name__ == "__main__":
    small = "input_small.txt"
    large = "input_large.txt"

    print(solution(small))
    print(solution(large))
