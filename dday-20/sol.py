from pprint import pprint
from collections import deque
import time
from colorama import Fore

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

    for key, values in config.items():
        if key not in types:
            types[key] = None
        for value in values:
            if value not in types:
                types[value] = None

    print(config)

    types[BROADCASTER] = "%"
    return config, types


def solve(config, types):
    state = {BROADCASTER: LO}

    # populate fip flops into state
    for key in config.keys():
        if key != BROADCASTER and types[key] == FLIP_FLOP:
            state[key] = LO

    # populate inverters into state
    for key, vals in config.items():
        # if key != BROADCASTER:
        for val in vals:
            if val in types and types[val] == INVERTER:
                if val not in state:
                    state[val] = {}
                state[val][key] = LO

    low_count, high_count = 0, 0
    print("state:", state)
    print("types:", types)
    print("config:", config)
    print()
    print("buttom -low-> broadcaster")

    for _ in range(1):
        low_count += 1

        queue = deque()
        for module in config[BROADCASTER]:
            queue.append((BROADCASTER, module))

        while queue:
            print(queue)
            print("state before:", state)
            from_module, to_module = queue.popleft()

            # first get the pulse type
            pulse = None
            if from_module in types:
                if types[from_module] == FLIP_FLOP:
                    pulse = state[from_module]
                elif types[from_module] == INVERTER:
                    if all(x is True for x in state[from_module].values()):
                        pulse = LO
                    else:
                        pulse = HI

            populate_queue = False

            if pulse == LO:
                low_count += 1
            else:
                high_count += 1

            print(f"{from_module} -{'high' if pulse else 'low'}-> {to_module}")
            # print("pulse type:", "HI" if pulse else "LO")

            # execute the pulse broadcast
            # if to_module in types:
            if types[to_module] == FLIP_FLOP:
                if pulse == LO:
                    state[to_module] = not state[to_module]
                    populate_queue = True

            if types[to_module] == INVERTER:
                if from_module == BROADCASTER:
                    populate_queue = True
                if state[to_module][from_module] != pulse:
                    state[to_module][from_module] = pulse
                    populate_queue = True

            print("state after:", state)
            print("populate_queue:", populate_queue)
            print()
            if populate_queue:
                if to_module in config:
                    for to_to_module in config[to_module]:
                        queue.append((to_module, to_to_module))
            else:
                if to_module in config:
                    for to_to_module in config[to_module]:
                        if types[to_to_module] is None:
                            queue.append((to_module, to_to_module))

    # print()
    print("low_count:", low_count, "high_count:", high_count)
    return low_count * high_count


def solution(filename):
    config, types = read_file(filename)
    # print("config:", config)
    # print("types:", types)
    ans = solve(config, types)
    return ans


if __name__ == "__main__":
    start_time = time.time()
    small = "input_small.txt"
    small2 = "input_small_2.txt"
    large = "input_large.txt"

    print(solution(small))
    # print(solution(small2))
    # print(solution(large))
    end_time = time.time()
    print(Fore.GREEN + f"code ran in {end_time-start_time:.5f} seconds")
