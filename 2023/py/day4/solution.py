def part1():
    digit_list = []
    with open("input.txt") as f:
        lines = f.readlines()
        running_sum = 0
        for line in lines:
            count = 0
            card_score = 0
            line = line.split(":")
            line = line[1]
            line = line.split("|")
            print(line[0])
            print(line[1])
            targets = line[0].split()
            values = line[1].split()
            targets_set = {x for x in targets}
            values_set = {x for x in values}
            winners = targets_set.intersection(values_set)
            print(winners)
            for i in winners:
                count += 1
            if not count == 0:
                card_score = 2 ** (count - 1)
            running_sum += card_score

    print(running_sum)


def part2():
    with open("input.txt") as f:
        lines = f.readlines()
        running_sum = 0
        for line in lines:
            count = 0
            card_score = 0
            line = line.split(":")
            line = line[1]
            line = line.split("|")
            print(line[0])
            print(line[1])
            targets = line[0].split()
            values = line[1].split()
            targets_set = {x for x in targets}
            values_set = {x for x in values}
            winners = targets_set.intersection(values_set)


if __name__ == "__main__":
    part1()
