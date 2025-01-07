def cuboid_calc(ln,w,h):
    surface1 = ln*w
    surface2 = w*h
    surface3 = h*ln
    extra = [surface1,surface2,surface3]
    extra.sort()
    area = (2*surface1)+(2*surface2)+(2*surface3)+extra[0]

    return area 

def ribbon_calc(ln:int, w:int, h:int):
    dimensions = [ln,w,h]
    dimensions.sort()
    ribbon_1 = (2*dimensions[0])+(2*dimensions[1])
    ribbon_2 = ln*w*h
    return ribbon_1+ribbon_2




def part1():
    with open("input.txt") as f:
        lines = f.readlines()
        result = []
        for line in lines:
            line = line.split("x")
            ln = int(line[0])
            w = int(line[1])
            h = int(line[2])
            area = cuboid_calc(ln,w,h)
            result.append(area)
    print(f"part 1: {sum(result)}")

def part2(): 
    with open("input.txt") as f:
        lines = f.readlines()
        result = []
        for line in lines:
            line = line.split("x")
            ln = int(line[0])
            w = int(line[1])
            h = int(line[2])
            length= ribbon_calc(ln,w,h)
            result.append(length)
    print(f"part 2: {sum(result)}")



if __name__ == "__main__":
    part1()
    part2()
