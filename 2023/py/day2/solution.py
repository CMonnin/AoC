def checker(cube_set: dict, bag: dict) -> bool:
    for colour, num in cube_set.items():
        if num > bag.get(colour, 0):
            return False
    return True


def part1():
    with open("input.txt") as f:
        lines = f.readlines()
        id_sum = 0
        bag = {"red": 12, "green": 13, "blue": 14}
        for i, line in enumerate(lines):
            line = line.split(":")
            id = line[0]
            id = id.split()
            id = id[1]
            line = line[1]
            line = line.split(";")
            cube_list = []
            for s in line:
                s = s.replace(",", "")
                s = s.split()
                s.reverse()
                current_dict = dict(zip(s[::2], map(int, s[1::2])))
                # print(current_dict)
                cube_list.append(current_dict)
            if all(checker(cube_set, bag) for cube_set in cube_list):
                # print(f"pass on {id}")
                id_sum += int(id)
            else:
                continue
        print(f"part1: {id_sum}")


def min_number_checker(cube_list):
    min_colour_dict = {"red": 1, "green": 1, "blue": 1}

    for cube_set in cube_list:
        for colour, num in cube_set.items():
            if min_colour_dict.get(colour, 0) == 1:
                min_colour_dict.update({colour: num})
                # print("here")
                # print(f"updated {colour} to: {min_colour_dict.get(colour)}")
            if num > min_colour_dict.get(colour, 0):
                min_colour_dict.update({colour: num})
                # print(f"updated {colour} to: {min_colour_dict.get(colour)}")
    # print(min_colour_dict)
    return min_colour_dict


def part2():
    with open("input.txt") as f:
        lines = f.readlines()
        power_list = []
        for i, line in enumerate(lines):
            line = line.split(":")
            id = line[0]
            id = id.split()
            id = id[1]
            line = line[1]
            line = line.split(";")
            cube_list = []
            for s in line:
                s = s.replace(",", "")
                s = s.split()
                s.reverse()
                current_dict = dict(zip(s[::2], map(int, s[1::2])))
                # print(current_dict)
                cube_list.append(current_dict)
                # print(f"pass on {id}")
            min_dict = min_number_checker(cube_list)
            power = 1
            for v in min_dict.values():
                power = power * v
                # print(f"power{power}")
            power_list.append(power)
            # print(f"power list {power_list}")
        print(f"part2: {sum(power_list)}")


if __name__ == "__main__":
    part1()
    part2()
    # test = [{"red": 4, "green": 8}, {"red": 15, "green": 4}]
    # print(min_number_checker(test))
