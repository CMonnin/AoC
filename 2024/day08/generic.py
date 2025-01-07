from collections import defaultdict
import itertools
import math


def part1():
    co_ord_dict = defaultdict(list)
    node_dict = defaultdict(list)
    with open("test.txt") as f:
        lines = f.readlines()
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char != "." and char != "\n":
                    co_ord_dict[char].append([x, y])
        for k, v in co_ord_dict.items():
            eqn_list = []
            combos = list(itertools.combinations(v, 2))
            print(list(combos))
            for combo in combos:
                x1, y1 = combo[0]
                x2, y2 = combo[1]
                eqn_list.append(eqn_line(x1, y1, x2, y2))
                d = distance(x1, y1, x2, y2)


def eqn_line(x1, y1, x2, y2):
    m = (x2 - x1) / (y2 - y1)
    c = y1 - m * x1
    return m, c


def distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 - (y2 - y1) ** 2)
    return d


def part2():
    return


if __name__ == "__main__":
    part1()
    part2()
