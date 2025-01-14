import itertools
import re


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
    doubles =itertools.product('abcdefghijklmnopqrstuvwxyz',repeat=2)
    groups = []
    for pair in doubles:
        groups.append(pair[0]+pair[1])
    print(groups)
    middle = re.compile(r'([a-z]).\1')

    with open("test.txt") as f:
        lines = f.readlines()
        for line in lines:
            word_pair_found = False
            middle_found = False
            p = middle.match(line)
            if (p):
                middle_found = True
            for pair in groups:
                p = re.compile(pair)
                iterator = p.finditer(line)
                # need logic to check that there's no overlap 
                for match in iterator:
                    print('here') 
                    print([match.span])
                    print([match.start])
                    print([match.end])

            if word_pair_found and middle_found:
                result[line]='good'

                
    print(f"part 2 : {len(result.keys())}") 




if __name__ == "__main__":
    # print("input:")
    # part1('input.txt')
    # print("test:")
    # part1('test.txt')
    part2()
    
