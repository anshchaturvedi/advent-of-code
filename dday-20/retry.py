from enum import Enum
from pprint import pprint
from collections import deque
from colorama import Fore
import time


class ModuleType(Enum):
    BROADCASTER = "broadcaster"
    FLIP_FLOP = "%"
    INVERTER = "&"


class PulseType(Enum):
    LOW = 0
    HIGH = 1


class Module:
    def __init__(self, line):
        self.dests = []
        self.name = ""
        self.type = None

        dests = list(map(lambda x: x.strip(), line[1].split(",")))

        for dest in dests:
            self.dests.append(dest)

        if line[0] == "broadcaster":
            self.name = line[0]
            self.type = ModuleType("broadcaster")
        else:
            self.name = line[0][1:]
            self.type = ModuleType(line[0][0])

        self.memory = False if self.type == ModuleType.FLIP_FLOP else {}


def read_and_parse_file(filename, t=False):
    lines = [line.strip() for line in open(filename)]

    for i in range(len(lines)):
        lines[i] = lines[i].split("->")
        for j in range(len(lines[i])):
            lines[i][j] = lines[i][j].strip()

    modules = {}

    for line in lines:
        new_module = Module(line)
        modules[new_module.name] = new_module

    for module in modules:
        for dest in modules[module].dests:
            if dest in modules and modules[dest].type == ModuleType.INVERTER:
                modules[dest].memory[module] = PulseType.LOW

    # for key, val in modules.items():
    #     print(val.name, ":  ", val.type, val.dests, val.memory)

    return modules


def solve(modules):
    low_count, high_count = 0, 0
    vg = None
    kp = None
    gc = None
    tx = None
    for i in range(100000000):
        low_count += 1
        queue = deque()

        for to_module in modules["broadcaster"].dests:
            queue.append(("broadcaster", PulseType.LOW, to_module))

        while queue:
            from_module, pulse, to_module = queue.popleft()
            # print(pulse, to_module)
            if pulse == PulseType.HIGH and from_module == "vg" and to_module == "bq":
                vg = i
            if pulse == PulseType.HIGH and from_module == "kp" and to_module == "bq":
                kp = i
            if pulse == PulseType.HIGH and from_module == "gc" and to_module == "bq":
                gc = i
            if pulse == PulseType.HIGH and from_module == "tx" and to_module == "bq":
                tx = i

            if vg and kp and gc and tx:
                return vg * kp * gc * tx

            if pulse == PulseType.LOW:
                low_count += 1
            else:
                high_count += 1
                
            if to_module not in modules:
                continue

            # flip flops are only affected when pulse is LOW
            if modules[to_module].type == ModuleType.FLIP_FLOP:
                if pulse == PulseType.LOW:
                    modules[to_module].memory = not modules[to_module].memory
                    next_pulse = PulseType.HIGH if modules[to_module].memory else PulseType.LOW
                    for to_to_module in modules[to_module].dests:
                        queue.append((to_module, next_pulse, to_to_module))

            elif modules[to_module].type == ModuleType.INVERTER:
                modules[to_module].memory[from_module] = pulse

                next_pulse = None
                if all(x == PulseType.HIGH for x in modules[to_module].memory.values()):
                    next_pulse = PulseType.LOW
                else:
                    next_pulse = PulseType.HIGH
                
                for to_to_module in modules[to_module].dests:
                    queue.append((to_module, next_pulse, to_to_module))

    # print("low_count:", low_count, "high_count:", high_count)
    # return low_count * high_count

def solution(filename):
    modules = read_and_parse_file(filename)
    ans = solve(modules)
    return ans


if __name__ == "__main__":
    start_time = time.time()
    small = "input_small.txt"
    small2 = "input_small_2.txt"
    large = "input_large.txt"

    # print(solution(small))
    # print(solution(small2))
    print(solution(large))
    end_time = time.time()
    print(Fore.GREEN + f"code ran in {end_time-start_time:.5f} seconds")
