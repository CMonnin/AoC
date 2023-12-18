import numpy as np


def part1():
    with open("input.txt") as f:
        result = 1
        lines = f.readlines()
        time_list = []
        distance_list = []
        for i, line in enumerate(lines):
            line = line.split(":")
            line = line[1]
            line = line.split()
            if i == 0:
                for time in line:
                    time_list.append(int(time))
            if i == 1:
                for distance in line:
                    distance_list.append(int(distance))
        print(time_list, distance_list)

        for i, time_element in enumerate(time_list):
            j = 0
            for speed in range(time_element):
                time_left = time_element - speed
                distance_travelled = time_left * speed
                if distance_travelled > distance_list[i]:
                    j += 1
            result *= j

        print(result)


def part2():
    with open("input.txt") as f:
        result = 1
        lines = f.readlines()
        time_list = []
        distance_list = []
        for i, line in enumerate(lines):
            line = line.split(":")
            line = line[1]
            line = line.split()
            if i == 0:
                big_time = ""
                for time in line:
                    big_time += time
                time_list.append(int(big_time))
            if i == 1:
                big_distance = ""
                for distance in line:
                    big_distance += distance
                distance_list.append(int(big_distance))
        print(time_list, distance_list)

        for i, time_element in enumerate(time_list):
            j = 0
            for speed in range(time_element):
                time_left = time_element - speed
                distance_travelled = time_left * speed
                if distance_travelled > distance_list[i]:
                    j += 1
            result *= j

        print(result)


if __name__ == "__main__":
    part1()
    part2()
