from collections import deque
from colorama import Fore
from pprint import pprint
import sys
import time


class Brick:
    def __init__(self, start_x, start_y, start_z, end_x, end_y, end_z):
        self.start_x = start_x
        self.start_y = start_y
        self.start_z = start_z

        self.end_x = end_x
        self.end_y = end_y
        self.end_z = end_z

        self.bricks_below = set()
        self.bricks_above = set()

        self.is_broken = False

    def __repr__(self):
        return f"({self.start_x}, {self.start_y}, {self.start_z}) -> ({self.end_x}, {self.end_y}, {self.end_z})"

    def set_as_broken(self):
        self.is_broken = True

    def move_down(self, amount=1):
        self.start_z -= amount
        self.end_z -= amount

    def get_coords(self):
        coords = []

        if self.start_x != self.end_x:
            for i in range(self.start_x, self.end_x + 1):
                coords.append((i, self.start_y, self.start_z))

        elif self.start_y != self.end_y:
            for i in range(self.start_y, self.end_y + 1):
                coords.append((self.start_x, i, self.start_z))

        elif self.start_z != self.end_z:
            for i in range(self.start_z, self.end_z + 1):
                coords.append((self.start_x, self.start_y, i))

        else:
            coords.append((self.start_x, self.start_y, self.start_z))

        return coords


def read_file(filename):
    return [line.strip().split("~") for line in open(filename)]


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

    return sorted(bricks, key=lambda x: min(x.start_z, x.end_z))


def determine_all_fallen_bricks(bricks):
    ans = 0

    for brick in bricks:
        queue = deque()
        queue.appendleft(brick)
        brick.set_as_broken()

        while queue:
            cur_brick = queue.pop()
            for above_brick in cur_brick.bricks_above:
                if all(
                    below_brick.is_broken for below_brick in above_brick.bricks_below
                ):
                    above_brick.set_as_broken()
                    queue.appendleft(above_brick)

        count = 0
        for x in bricks:
            count = count + 1 if x.is_broken else count
            x.is_broken = False

        ans += count - 1

    return ans


def solve(bricks):
    # first part is to get all the bricks to their final positions
    for i in range(len(bricks)):
        # if brick is at z = 1 then we can't do anything
        if bricks[i].start_z == 1:
            continue

        # get all the coordinates of bricks underneath the current one
        coords_below = set()
        for j in range(i):
            for coord in bricks[j].get_coords():
                coords_below.add(coord)

        # get all coordinates that current brick has, and check whether
        # one below (z-1) are also vacant
        while True:
            cur_coords = bricks[i].get_coords()
            good = True
            for x, y, z in cur_coords:
                new_coord = (x, y, z - 1)
                if new_coord in coords_below:
                    good = False
                    break

            if good:
                bricks[i].move_down()
                if bricks[i].start_z == 1:
                    break
            else:
                break

        # at this point, the brick should be at its final resting place

    # now we need to check what bricks are supporting what other bricks
    coords_to_bricks = {}

    for brick in bricks:
        for coord in brick.get_coords():
            coords_to_bricks[coord] = brick

    for brick in bricks:
        # all bricks that `brick` supports
        brick_coords = brick.get_coords()
        for x, y, z in brick_coords:
            new_point = (x, y, z + 1)
            if new_point in coords_to_bricks and coords_to_bricks[new_point] != brick:
                brick.bricks_above.add(coords_to_bricks[new_point])

        # all bricks that supports `brick`
        for x, y, z in brick_coords:
            new_point = (x, y, z - 1)
            if new_point in coords_to_bricks and coords_to_bricks[new_point] != brick:
                brick.bricks_below.add(coords_to_bricks[new_point])

    return determine_all_fallen_bricks(bricks)


def solution(filename):
    input = read_file(filename)
    all_bricks = create_bricks(input)
    return solve(all_bricks)


if __name__ == "__main__":
    files = ["input_small.txt"]
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        pass
    else:
        files.append("input_large.txt")

    for file in files:
        start_time = time.time()
        print(solution(file))
        end_time = time.time()
        print(
            Fore.GREEN
            + f"code ran for {file} in {end_time-start_time:.4f} seconds"
            + Fore.WHITE
        )
