from collections import Counter


def part1():
    with open("input.txt") as f:
        lines = f.readlines()
        report_arr = []
        print(lines)
        for line in lines:
            report = line.split()
            print(report)
            inc = True
            dec = True
            adj = True

            for i in range(1, len(report)):
                print(f"i: {i}")
                print(f"len report:{len(report)}")
                num1 = int(report[i])
                num2 = int(report[i - 1])
                adj_number = abs(num1 - num2)
                print(f"adj_number: {adj_number}")
                inc_check = num1 - num2

                if i == 1:
                    if inc_check > 0:
                        dec = False
                        inc = True
                    if inc_check < 0:
                        inc = False
                        dec = True
                if inc_check == 0:
                    report_arr.append("unsafe")
                    break
                if inc:
                    if inc_check > 0:
                        dec = False
                        inc = True
                    if inc_check < 0:
                        inc = False
                        dec = True
                    if adj_number > 3:
                        adj = False
                    if not inc or not adj:
                        report_arr.append("unsafe")
                        break
                if dec:
                    if inc_check > 0:
                        dec = False
                        inc = True
                    if inc_check < 0:
                        inc = False
                        dec = True
                    if adj_number > 3:
                        adj = False
                    if not dec or not adj:
                        report_arr.append("unsafe")
                        break
                if i == len(report) - 1:
                    print("safe")
                    report_arr.append("safe")
    safe_count = Counter(report_arr)
    print("***********")
    print(report_arr)
    print("safe count:")
    print(safe_count["safe"])
    print("***********")


def part2():
    return


if __name__ == "__main__":
    part1()
    part2()
