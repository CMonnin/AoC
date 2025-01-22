from ast import literal_eval

def part1():
    running_count = 0
    with open("input.txt",encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            running_count+= len(line)-len(literal_eval(line))
            
    print(running_count)

def helper (line):
    return(line.replace('\\','\\\\').replace('"','\\"'))

def part2():
    running_count = 0
    with open("input.txt",encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            new_line = helper(line)
            running_count+= len(new_line)-len(line)+2
            print(new_line)
            print(len(new_line)+2)
            
    print(running_count)




if __name__ == "__main__":
    part1()
    part2()
