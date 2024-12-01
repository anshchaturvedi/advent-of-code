from pprint import pprint
import re


def read_file(filename):
    string = [line.strip() for line in open(filename)]
    return string[0].split(",")


def split_string(string):
    match = re.match(r"(\w+)([-=])(\d*)", string)
    if match:
        return (
            match.group(1),
            match.group(2),
            match.group(3) if match.group(3) else None,
        )


def get_hash(string):
    start = 0
    for i in range(len(string)):
        start = (start + ord(string[i])) * 17 % 256
    return start


def populate(hashmap, string):
    first, op, end = split_string(string)
    _hash = get_hash(first)
    if op == "=":
        for i, lens in enumerate(hashmap[_hash]):
            if lens[0] == first:
                hashmap[_hash][i][1] = end
                return hashmap
        hashmap[_hash].append([first, end])
    else:
        idx = -1
        for i in range(len(hashmap[_hash])):
            if hashmap[_hash][i][0] == first:
                idx = i
                break
        if idx >= 0:
            hashmap[_hash].pop(idx)

    return hashmap


def solution(filename):
    strings = read_file(filename)

    hashmap = {}
    for i in range(256):
        hashmap[i] = []

    for string in strings:
        hashmap = populate(hashmap, string)

    ans = 0
    for key, val in hashmap.items():
        if val != []:
            for idx, value in enumerate(val):
                ans += (key + 1) * (idx + 1) * (int(value[1]))
    return ans


if __name__ == "__main__":
    small = "input_small.txt"
    large = "input_large.txt"

    print(solution(small))
    print(solution(large))
