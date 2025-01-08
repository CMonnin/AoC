def part1():
    result = {}
    result[0,0]= 'here' 
    with open("input.txt") as f:
        lines = f.readlines()
        i=0
        j=0
        for char in lines[0]:
            if char == "^":
                j+=1
            if char == "v":
                j-=1
            if char == "<":
                i-=1
            if char == ">":
                i+=1
            result[i,j]='here'
    print(f"part 1: {len(result)}") 

def part1_test():
    result = {}
    result[0,0]= 'here' 
    with open("test.txt") as f:
        lines = f.readlines()
        i=0
        j=0
        for char in lines[0]:
            if char == "^":
                j+=1
            if char == "v":
                j-=1
            if char == "<":
                i-=1
            if char == ">":
                i+=1
            result[i,j]='here'
    print(f"part 1 test: {len(result)}") 


def part2():

    result = {}
    result[0,0]= 'here' 
    with open("input.txt") as f:
        lines = f.readlines()
            
        i=0
        j=0
        k=0
        ln=0
        for idx, char in enumerate(lines[0]):
            if idx%2==0:
                if char == "^":
                    i+=1
                if char == "v":
                    i-=1
                if char == "<":
                    j-=1
                if char == ">":
                    j+=1
                result[i,j]='here'
                continue
            if char == "^":
                k+=1
            if char == "v":
                k-=1
            if char == "<":
                ln-=1
            if char == ">":
                ln+=1
            result[k,ln]='here'
    print(f"part 2: {len(result)}") 

def part2_test():

    result = {}
    result[0,0]= 'here' 
    with open("test.txt") as f:
        lines = f.readlines()
            
        i=0
        j=0
        k=0
        ln=0
        for idx, char in enumerate(lines[0]):
            if idx%2==0:
                if char == "^":
                    i+=1
                if char == "v":
                    i-=1
                if char == "<":
                    j-=1
                if char == ">":
                    j+=1
                result[i,j]='here'
                continue
            if char == "^":
                k+=1
            if char == "v":
                k-=1
            if char == "<":
                ln-=1
            if char == ">":
                ln+=1
            result[k,ln]='here'
    print(f"part 2 test: {len(result)}") 



if __name__ == "__main__":
    part1()
    part1_test()
    part2()
    part2_test()
