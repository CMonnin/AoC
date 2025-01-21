import functools
import operator

bitwise_operators = {
    "AND": operator.and_,  
    "LSHIFT": operator.lshift, 
    "RSHIFT": operator.rshift,
    "NOT": operator.invert,
    "OR": operator.or_,
    "ID": lambda x: x
}
wires = {}

def part1():
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines: 
            line = line.strip().split()
            match line:
                case x, "->", y:
                    wires[y] = (bitwise_operators['ID'], x) 
                case *x, op, z, "->", y:
                    wires[y] = (bitwise_operators[op], *x, z)

    @functools.cache
    def solve_wire(w):
        if isinstance(w, int) or w[0].isdigit():
            return int(w) & 0xFFFF
        
        wire_data = wires[w]
        operation = wire_data[0]
        args = wire_data[1:]
        
        solved_args = []
        for arg in args:
            solved_value = solve_wire(arg)
            solved_args.append(solved_value)
        
        result = operation(*solved_args)
        
        final_result = result & 0xFFFF
        
        return final_result

    return solve_wire("a")

print(part1())

def part2():
    result = {}
    with open("input.txt") as f:
        lines = f.readlines()
        lines = f.readlines()
        for line in lines: 
            line = line.strip().split()
            match line:
                case x, "->", y:
                    wires[y] = (bitwise_operators['ID'], x) 
                case *x, op, z, "->", y:
                    wires[y] = (bitwise_operators[op], *x, z)

    @functools.cache
    def solve_wire(w):
        if isinstance(w, int) or w[0].isdigit():
            return int(w) & 0xFFFF
        
        wire_data = wires[w]
        operation = wire_data[0]
        args = wire_data[1:]
        
        solved_args = []
        for arg in args:
            solved_value = solve_wire(arg)
            solved_args.append(solved_value)
        
        result = operation(*solved_args)

        if w == 'b':
            final_result = 3176 
        else:
            final_result = result & 0xFFFF
        
        return final_result

    return solve_wire("a")


print(part2())

if __name__ == "__main__":
    part1()
    part2()
