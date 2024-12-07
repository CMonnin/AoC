from collections import defaultdict


def part1():
    with open("input.txt") as f:
        inst = f.readlines()[:1176]
        f.seek(0)
        lines = f.readlines()[1177:]
        a_dict = defaultdict(list)
        result = []

        for rule in inst:
            x, y = rule.split("|")
            a_dict[int(y)].append(int(x.strip()))

        for line in lines:
            line = line.split(",")
            line = list(map(lambda x: int(x.strip()), line))
            is_valid = True

            for count, element in enumerate(line):
                for prior_element in a_dict[element]:
                    if prior_element in line[count + 1 :]:
                        is_valid = False
                        break
                if not is_valid:
                    break

            if is_valid:
                x = len(line) // 2
                result.append(line[x])

        print("*******")
        print(sum(result))


def top_sort(arr, a_dict)

def part2():
    return


if __name__ == "__main__":
    part1()
    part2()
