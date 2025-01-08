
def part1(file):
    result = {}
    with open(file) as f:
        lines = f.readlines()
        vowels = ['a','e','i','o','u']
        bad_substrings = ['ab','cd','pq','xy']
        for line in lines:
            line = line.strip() 
            good_substring = False
            v_count = 0
            contains_bad = False
            for sub in bad_substrings:
                if sub in line:
                    contains_bad = True
            if contains_bad:
                continue 
            for idx,char in enumerate(line):
                if char in vowels:
                    v_count +=1
                if idx != 0:
                    if char == line[idx-1]:
                        good_substring=True
            if  v_count >= 3 and good_substring:
                    result[line] = 'good'
    print(list(result))
    print(f"part 1 : {len(result.keys())}") 

def part2():
    result = {}
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            pass
            
    print(f"part 2: {result}") 

def part2_test():

    result = {}
    with open("test.txt") as f:
        lines = f.readlines()
        for line in lines:
            pass
            
    print(f"part 2 test: {result}") 



if __name__ == "__main__":
    print("input:")
    part1('input.txt')
    print("test:")
    part1('test.txt')
    part2()
