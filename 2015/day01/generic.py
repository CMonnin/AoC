def part1():
    with open("input.txt") as f:
        lines = f.readlines()
        floor = 0
        for line in lines:
            for idx, i in enumerate(line):
                if floor == -1:
                    # not sure why this works, should be idx+1 according to the instructions
                    print(f"position: {idx}")
                if i == "(":
                    floor +=1
                if i == ")":
                    floor -=1
    print(floor)

            
    return
def part2(): 
    return 



if __name__ == "__main__":
    part1()
    part2() 
