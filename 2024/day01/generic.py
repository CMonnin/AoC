def part1():
    left_side = []
    right_side = []
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            line = line.replace("   ", ",")
            numbers = line.split(",")
            left_side.append(numbers[0])
            right_side.append(numbers[1])

    running_total = 0
    left_side = [int(num) for num in left_side]
    right_side = [int(num) for num in right_side]
    left_side.sort()
    right_side.sort()
    for i in range(len(left_side)):
        running_total += abs((left_side[i]) - (right_side[i]))
    print(running_total)


def part2():
    left_side = []
    right_side = []
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            line = line.replace("   ", ",")
            numbers = line.split(",")
            left_side.append(numbers[0])
            right_side.append(numbers[1])

    left_side = [int(num) for num in left_side]
    right_side = [int(num) for num in right_side]
    score = 0

    for i in range(len(left_side)):
        right_count = 0
        current_number = left_side[i]
        for j in range(len(right_side)):
            if current_number == right_side[j]:
                right_count += 1
        current_score = current_number * right_count
        score += current_score
    print(score)


if __name__ == "__main__":
    part1()
    part2()
