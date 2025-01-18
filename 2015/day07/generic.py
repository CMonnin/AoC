def line_solver(lines_to_process):
    for line in lines_to_process:
        try:
            pass
        except Exception as e:
            raise e

def source_nodes(lines_to_process):
    result_dict ={}
    for line in lines_to_process:
        line = line.strip()
        line = line.split()
        if len(line) == 3:
            result_dict[line[2]] = int(line[0])
    return result_dict


def part1():
    result = {}
    bitwise_operators = [
        "AND",  
        "LSHIFT",
        "RSHIFT",
        "NOT",
        "OR"
    ]
    solved = {}
    has_value_dict = {}
    with open("input.txt") as f:
        lines = f.readlines()
        lines_to_process =[]
        # give all source nodes
        result = source_nodes(lines)
        if len(lines) == 0:



        for line in lines:
            line = line.strip()
            line = line.split()

            if len(line) == 3:
                result[line[2]] = int(line[0])
            else:
                lines_to_process.append(line)
                continue
        for line in lines_to_process:
            try:
                result[]
            except Exception as e:
                raise e




            try:
                solved[line[-1]]
                continue
            except KeyError:
               pass
            if not line[0].isdigit():
                try:
                        solved[line[0]]
                except KeyError:
                    pass
                try:
                        solved[line[]]
                except KeyError:
                    pass

            if solved[line[-1]]:
                pass

            else:
                for command in bitwise_operators:
                    if command in line:
                        if command == 'AND':
                            x = result[line[0]] 
                            y = result[line[2]]
                            current_result=x & y
                            result[line[4]] = current_result& 0xFFFF 
                        if command == "LSHIFT":
                            x = result[line[0]] 
                            y = int(line[2])
                            current_result=x << y
                            result[line[4]]  = current_result& 0xFFFF 
                        if command == "RSHIFT":
                            x = result[line[0]] 
                            y = int(line[2])
                            current_result = x >> y
                            result[line[4]]  = current_result& 0xFFFF 
                        if command == "OR":
                            x = result[line[0]] 
                            y = result[line[2]]
                            current_result= x | y
                            result[line[4]]   = current_result& 0xFFFF 
                        if command == "NOT":
                            x = result[line[1]] 
                            result[line[3]] = ~x & 0xFFFF

            
    print(f"part 1: {result.items()}") 
    print(f"{result['a']}")


def part2():
    result = {}
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            pass
            
    print(f"part 2: {result}") 



if __name__ == "__main__":
    part1()
    part2()
