from pprint import pprint


def read_file(filename):
    buffer = []
    with open(filename) as f:
        line = f.readline()
        while line:
            buffer.append(list(map(lambda x: int(x), line.strip().split())))
            line = f.readline()

    return buffer


def is_all_zero(l):
    for c in l:
        if c != 0:
            return False
    return True


def calculate_ans(lines):
    ans = 0
    for line in lines:
        lists = [line]

        while not is_all_zero(lists[-1]):
            new_list = []
            for i in range(1, len(lists[-1])):
                new_list.append(lists[-1][i] - lists[-1][i - 1])
            lists.append(new_list)

        lists[-1].insert(0, 0)

        for i in range(len(lists) - 2, -1, -1):
            lists[i].insert(0, lists[i][0] - lists[i + 1][0])

        ans += lists[0][0]

    return ans


def solution(filename):
    lines = read_file(filename)
    ans = calculate_ans(lines)

    return ans


if __name__ == "__main__":
    small = "input_small.txt"
    large = "input_large.txt"

    print(solution(small))
    print(solution(large))
