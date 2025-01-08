import hashlib


def part1():
    with open("input.txt") as f:
        lines = f.readlines()
        not_found = True
        i = 0
        while not_found:
            key = str(lines[0].strip())+str(i)
            byte_key = key.encode()
            m = hashlib.md5(byte_key).hexdigest()
            if m[:5] == '00000':
                break
            i+=1
        print('ans part1')
        print(i)

def part1_test():

    with open("test.txt") as f:
        lines = f.readlines()
        not_found = True
        i = 0
        while not_found:
            key = str(lines[0].strip())+str(i)
            byte_key = key.encode()
            m = hashlib.md5(byte_key).hexdigest()
            if m[:5] == '00000':
                break
            i+=1
            print('running')
            print(i)
        print('ans part1_test')
        print(i)

def part2():
    with open("input.txt") as f:
        lines = f.readlines()
        not_found = True
        i = 0
        while not_found:
            key = str(lines[0].strip())+str(i)
            byte_key = key.encode()
            m = hashlib.md5(byte_key).hexdigest()
            if m[:6] == '000000':
                break
            i+=1
        print('ans part1')
        print(i)

def part2_test():

    result = {}
    with open("test.txt") as f:
        lines = f.readlines()
        for line in lines:
            pass
            
    print(f"part 2 test: {result}") 



if __name__ == "__main__":
    part1()
    part2()
