def part1():
    result = {}
    for i in range (1000):
        for j in range (1000):
            result[i,j] ="off"
    lights_off = [key for key,val in result.items() if val == 'off']
    print(len(lights_off))

    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            action = ''
            line = line.split()
            if line[0]=='toggle':
                action = 'toggle'
                x1,y1 = line[1].split(",") 
                x2,y2 = line[3].split(',')
                x1 = int(x1)
                x2 = int(x2)
                y1 = int(y1)
                y2 = int(y2)
            else:
                action = line[1]
                x1,y1 = line[2].split(",") 
                x2,y2 = line[4].split(',')
                x1 = int(x1)
                x2 = int(x2)
                y1 = int(y1)
                y2 = int(y2)

            for i in range(x1,x2+1):
                for j in range(y1,y2+1):
                    if action=='toggle':
                        if result[i,j] != 'off':
                            result[i,j] = 'off'
                        else:
                            result[i,j] = 'on'
                    elif action=='on':
                        result[i,j]='on'
                    else :
                        result[i,j]='off'
    lights_on = [key for key,val in result.items() if val == 'on'] 
    print(f"part 1: {len(lights_on)}") 

            

def part2():
    result = {}
    for i in range (1000):
        for j in range (1000):
            result[i,j] =0
    lights_off = [key for key,val in result.items() if val == 'off']
    print(len(lights_off))

    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            action = ''
            line = line.split()
            if line[0]=='toggle':
                action = 'toggle'
                x1,y1 = line[1].split(",") 
                x2,y2 = line[3].split(',')
                x1 = int(x1)
                x2 = int(x2)
                y1 = int(y1)
                y2 = int(y2)
            else:
                action = line[1]
                x1,y1 = line[2].split(",") 
                x2,y2 = line[4].split(',')
                x1 = int(x1)
                x2 = int(x2)
                y1 = int(y1)
                y2 = int(y2)

            for i in range(x1,x2+1):
                for j in range(y1,y2+1):
                    if action=='toggle':
                        result[i,j]+=2
                    elif action=='on':
                        result[i,j]+=1
                    else:
                        if result[i,j]>0:
                            result[i,j]-=1
    running_total = 0
    for v in result.values():
        running_total+=v
    print(f"part 2: {running_total}") 



if __name__ == "__main__":
    part1()
    part2()
