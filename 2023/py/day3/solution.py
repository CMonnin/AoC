def neighbour_checker(gear_map: dict):
    valid_list = []
    for k, v in gear_map.items():
        if not v.isdigit():
            co_ord_list = []
            x_co_ord = k[0]
            y_co_ord = k[1]

            valid_list.append()
            print(k, v)


def part1():
    with open("test1.txt") as f:
        lines = f.readlines()
        gear_map = {}
        for y, line in enumerate(lines):
            line = line.rstrip()
            for x, c in enumerate(line):
                if c != ".":
                    gear_map.update({(x, y): c})
                    print(f"co-ord {x,y}")
                    print(f"c{c}")
        neighbour_checker(gear_map)


if __name__ == "__main__":
    part1()
