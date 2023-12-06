def valid_populator(gear_map: dict):
    valid_dict = {}
    for k, v in gear_map.items():
        if not v.isdigit():
            print(k, v)
            co_ord_list = []
            x_y_co_ord = [k[0], k[1]]
            surrounding_area = [
                [-1, -1],
                [-1, 0],
                [0, -1],
                [0, 0],
                [1, 0],
                [0, 1],
                [1, 1],
                [-1, 1],
                [1, -1],
            ]
            for co_ord in surrounding_area:
                co_ord_list.append([a + b for a, b in zip(x_y_co_ord, co_ord)])
            for valid_co_cord in co_ord_list:
                if not valid_dict.get(tuple(valid_co_cord)):
                    valid_dict.update({tuple(valid_co_cord): "valid"})
    return valid_dict


# i want to keep adding to a list of numbers until it's done then i want to conncat
# them together and check if any of there locations is valid. if yes add to a sum
def part1():
    with open("input.txt") as f:
        lines = f.readlines()
        gear_map = {}
        gear_sum = 0
        for y, line in enumerate(lines):
            line = line.rstrip()
            for x, c in enumerate(line):
                if c != ".":
                    gear_map.update({(x, y): c})
        #           print(f"co-ord {x,y}")
        #            print(f"c{c}")
        # print(f" GEAR MAP  {gear_map}")
        valid_dict = valid_populator(gear_map)

        print(valid_dict)
        for y, line in enumerate(lines):
            number_list = ["0"]
            running_co_ord_list = []
            line = line.rstrip()
            for x, c in enumerate(line):
                if c.isdigit():
                    number_list.append(c)
                    running_co_ord_list.append((x, y))
                if not c.isdigit() or x == len(line) - 1:
                    actual_number = "0"
                    for e in number_list:
                        actual_number += e
                    actual_number = int(actual_number)
                    if any(x_y in valid_dict for x_y in running_co_ord_list):
                        gear_sum += actual_number
                        print(actual_number)
                    number_list = ["0"]
                    running_co_ord_list.clear()

    print(gear_sum)


if __name__ == "__main__":
    part1()
