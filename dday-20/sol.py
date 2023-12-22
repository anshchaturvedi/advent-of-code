from pprint import pprint
from collections import deque

BROADCASTER = "broadcaster"
INVERTER = "&"
FLIP_FLOP = "%"
LO = False
HI = True


def read_file(filename, t=False):
    lines = [line.strip() for line in open(filename)]

    for i in range(len(lines)):
        lines[i] = lines[i].split("->")
        for j in range(len(lines[i])):
            lines[i][j] = lines[i][j].strip()

    config = {}
    types = {}

    for line in lines:
        val = list(map(lambda x: x.strip(), line[1:]))
        if line[0] == BROADCASTER:
            config[line[0]] = val[0].split(", ")
        else:
            # pprint(line)
            module, type = line[0][1:], line[0][0]
            config[module] = line[1].split(", ")
            types[module] = type

    return config, types


# False = low, True = high
def solve(config, types):
    # pprint(config)
    # print()
    # pprint(types)
    state = {}

    # populate fip flops
    for key in config.keys():
        if key != BROADCASTER and types[key] == FLIP_FLOP:
            state[key] = LO

    # pprint(state)
    # populate inverters
    for key, vals in config.items():
        if key != BROADCASTER:
            for val in vals:
                if val in types and types[val] == INVERTER:
                    if val not in state:
                        state[val] = {}
                    state[val][key] = LO

    state[BROADCASTER] = LO
    pprint(state)

    queue = deque()
    for module in config[BROADCASTER]:
        deque.append(module)
    cur_emitted = BROADCASTER

    while queue:
        

    #     for module in modules:
    #         pulse = state[cur_emitted]
    #         if types(module) == FLIP_FLOP and pulse == LO:
    #             state[module] = not state[module]
    #         elif types(module) == INVERTER:
    #             state[module][cur_emitted] = pulse


def solution(filename):
    config, types = read_file(filename)

    ans = solve(config, types)


if __name__ == "__main__":
    small = "input_small.txt"
    small2 = "input_small_2.txt"
    large = "input_large.txt"

    print(solution(small))
    # print(solution(small2))
    # print(solution(large))
