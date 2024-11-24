def part1():
    digit_list = []
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            for c in line:
                if c.isdigit():
                    first_digit_as_str = c
                    break
            for c in reversed(line):
                if c.isdigit():
                    last_digit_as_str = c
                    break

            digit = int(first_digit_as_str + last_digit_as_str)
            digit_list.append(digit)

    running_sum = 0
    for digit in digit_list:
        running_sum += digit

    print(f"part1 soln: {running_sum}")


def replacer(line):
    line = line.replace("zero", "zero0zero")
    line = line.replace("one", "one1one")
    line = line.replace("two", "two2two")
    line = line.replace("three", "three3three")
    line = line.replace("four", "four4four")
    line = line.replace("five", "five5five")
    line = line.replace("six", "six6six")
    line = line.replace("seven", "seven7seven")
    line = line.replace("eight", "eight8eight")
    line = line.replace("nine", "nine9nine")
    return line


def part2():
    replaced_line_list = []
    digit_list = []

    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            replaced_line_list.append(replacer(line))

    for line in replaced_line_list:
        for c in line:
            try:
                can_convert = int(c)
                first_digit_as_str = c
                break
            except ValueError:
                continue
        for c in reversed(line):
            try:
                can_convert = int(c)
                last_digit_as_str = c
                break
            except ValueError:
                continue

        digit = int(first_digit_as_str + last_digit_as_str)
        digit_list.append(digit)

    running_sum = 0
    for digit in digit_list:
        running_sum += digit
    print(f"part2 soln: {running_sum}")


if __name__ == "__main__":
    part2()
