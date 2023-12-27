from pprint import pprint
from collections import deque
import time
from colorama import Fore


class Brick:
    def __init__(self, start_x, start_y, start_z, end_x, end_y, end_z):
        self.start_x = start_x
        self.start_y = start_y
        self.start_z = start_z

        self.end_x = end_x
        self.end_y = end_y
        self.end_z = end_z

    def __repr__(self):
        return f"({self.start_x}, {self.start_y}, {self.start_z}) -> ({self.end_x}, {self.end_y}, {self.end_z})"


def read_file(filename, t=False):
    lines = [line.strip().split("~") for line in open(filename)]
    return lines


def create_bricks(input):
    bricks = []
    for start, end in input:
        start, end = start.split(","), end.split(",")
        new_brick = Brick(
            int(start[0]),
            int(start[1]),
            int(start[2]),
            int(end[0]),
            int(end[1]),
            int(end[2]),
        )
        bricks.append(new_brick)

    return sorted(bricks, key=lambda x: x.start_z)

    
def solve(bricks):
    changed = True

    while changed:
        pass


def solution(filename):
    input = read_file(filename)
    all_bricks = create_bricks(input)
    return solve(all_bricks)


if __name__ == "__main__":
    start_time = time.time()
    small = "input_small.txt"
    large = "input_large.txt"

    print(solution(small))
    # print(solution(large))
    end_time = time.time()
    print(Fore.GREEN + f"code ran in {end_time-start_time:.5f} seconds")
