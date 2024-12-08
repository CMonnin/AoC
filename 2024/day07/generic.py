from itertools import product


def part1():
    good_eqn = []
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            ans, eqn = line.split(":")
            ans = int(ans)
            eqn = eqn.split()
            eqn = [int(x) for x in eqn]
            op_array = op_combos(1, len(eqn) - 1)
            for perm in op_array:
                result = eqn[0]
                for idx, op in enumerate(perm):
                    if op == "+":
                        result += eqn[idx + 1]
                    else:
                        result *= eqn[idx + 1]
                if result == ans:
                    good_eqn.append(ans)
                    break
            print(good_eqn)
    print(sum(good_eqn))


def op_combos(p_n, number_of_operators):
    ops = []
    if p_n == 1:
        ops = ["+", "*"]
    if p_n == 2:
        ops = ["+", "*", "||"]
    return product(ops, repeat=number_of_operators)


def part2():
    good_eqn = []
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            ans, eqn = line.split(":")
            ans = int(ans)
            eqn = eqn.split()
            eqn = [int(x) for x in eqn]
            op_array = op_combos(2, len(eqn) - 1)
            for perm in op_array:
                result = eqn[0]
                for idx, op in enumerate(perm):
                    if op == "+":
                        result += eqn[idx + 1]
                    elif op == "*":
                        result *= eqn[idx + 1]
                    else:
                        result = int(str(result) + str(eqn[idx + 1]))
                if result == ans:
                    good_eqn.append(ans)
                    break
            print(good_eqn)
    print(sum(good_eqn))


if __name__ == "__main__":
    part1()
    part2()
