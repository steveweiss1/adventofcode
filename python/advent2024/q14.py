from collections import defaultdict
import re
import sys
import copy

class Robot:
    def __init__(self, p, v):
        self.p = p
        self.v = v

    def move(self, width, height):
        x = self.p
        self.p = ((self.p[0] + self.v[0]) % width, (self.p[1] + self.v[1]) % height)
        # print((x, self.v, self.p))

    def __repr__(self):
        return f"R(p={self.p})"


def parse_file(filename):
    parsed_data = []

    line_num = 0
    with open(filename, 'r') as file:
        a = (0, 0)
        b = (0, 0)
        prize = (0, 0)
        nodes = []
        for line in file:
            line = line.strip()
            if line:
                matches = [int(x) for x in re.findall(r'(-?\d+)', line)]
                parsed_data.append(Robot((matches[0], matches[1]), (matches[2], matches[3])))

    return parsed_data

def part1(robots, width, height):
    for _ in range(100):
        for r in robots:
            r.move_boxes(width, height)

    d = defaultdict(int)

    for r in robots:
        if r.p[0] == int(width / 2):
            continue
        elif r.p[0] < int(width / 2):
            x = 0
        else:
            x = 1

        if r.p[1] == int(height / 2):
            continue
        elif r.p[1] < int(height / 2):
            y = 0
        else:
            y = 1

        d[(x, y)] += 1
    return d[(0, 0)] * d[(0, 1)] * d[(1, 0)] * d[(1, 1)]

def has_diag(d, width, height):
    for y in range(0, 60):
        for x in range(width - 30):
            if d[(x,y)] == 1:
                found = True
                for i in range(10):
                    if d[(x, y+i)] == 0:
                        found = False
                        break
                if found:
                    return True
    return False


def draw(i, robots, width, height):
    d = defaultdict(int)
    for r in robots:
        d[r.p] = 1

    if has_diag(d, width, height):
        print(i)
        str = ''
        for y in range(height):
            str = ''
            for x in range(width):
                if d[(x, y)] == 1:
                    str += 'X'
                else:
                    str += ' '
            print(str)
        return True
    return False


def part2(robots, width, height):
    with open("q14-out.txt", 'w') as file:
        sys.stdout = file
        for i in range(1,10000):
            for r in robots:
                r.move_boxes(width, height)
            if draw(i, robots, width, height):
                return i
    sys.stdout = sys.__stdout__


# def part2(nodes):


input_data = parse_file("q14.txt")
#cp = copy.deepcopy(input_data)
#print(part1(input_data, 101, 103))
#input_data = parse_file("q14.txt")
part2(input_data, 101, 103)

# print(part2(input_data))
