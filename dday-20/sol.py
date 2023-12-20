from pprint import pprint
import copy


def read_file(filename, t=False):
    lines = [line.strip() for line in open(filename)]
    return lines

def solution(filename):
    config = read_file(filename)
    pprint(config)


if __name__ == "__main__":
    small = "input_small.txt"
    small2 = "input_small2.txt"
    # large = "input_large.txt"

    print(solution(small))
    print(solution(small2))
    print(solution(large))
