import re


def part1():
    with open("input.txt") as f:
        lines = f.readlines()
        sum = 0
        for line in lines:
            regex_search = re.findall(r"mul\((\d{1,3}\,\d{1,3})\)", line)
            converted = [[], []]
            for pairs in regex_search:
                x, y = pairs.split(",")
                converted[0].append(x)
                converted[1].append(y)
            mul = map(lambda x, y: int(x) * int(y), converted[0], converted[1])
            for i in mul:
                sum += i

        print(sum)


def part2():
    with open("input.txt") as f:
        lines = f.readlines()
        sum = 0
        state = True
        do = "do()"
        dont = "don't()"
        sum = 0
        for line in lines:
            regex_search = re.findall(
                r"(do\(\))|(don\Wt\(\))|mul\((\d{1,3})\,(\d{1,3})\)", line
            )
            for groups in regex_search:
                if do in groups:
                    state = True
                    continue
                if dont in groups:
                    state = False
                    continue
                if state:
                    x, y = groups[2], groups[3]
                    mul = int(x) * int(y)
                    sum += mul

        print(sum)


if __name__ == "__main__":
    part1()
    part2()
