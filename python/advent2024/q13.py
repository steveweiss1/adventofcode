from collections import defaultdict
import re
import numpy as np

part2offset = 10000000000000

class Node:
    def __init__(self, a, b, prize):
        self.a = a
        self.b = b
        self.prize = prize

    def __repr__(self):
        return f"Node(a={self.a}, b={self.b}, prize={self.prize})"

    def find(self):
        vals = set()
        for a in range(100):
            for b in range(100):
                loc = (a * self.a[0] + b * self.b[0], a * self.a[1] + b * self.b[1])
                if loc == self.prize:
                    vals.add(3 * a + b)
                if loc[0] > self.prize[0] or loc[1] > self.prize[1]:
                    break
        if len(vals) == 0:
            return 0

        return sorted(vals)[0]

    def solve(self, offset=0):
        oprize = (self.prize[0] + offset, self.prize[1] + offset)
        A = np.array([[self.a[0], self.b[0]], [self.a[1], self.b[1]]])
        B = np.array([oprize[0], oprize[1]])
        solution = np.linalg.solve(A, B)
        if np.all(np.isclose(solution, np.round(solution), 0, 0.0001)):
            # Convert to integers if close enough
            solution = np.round(solution).astype(int)

            return 3*solution[0] + solution[1]
        return 0


def truncate_to_thousandth(value):
    return int(value * 1000) / 1000

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
                matches = tuple([int(x) for x in re.findall(r'(\d+)', line)])
                if line_num == 0:
                    a = matches
                elif line_num == 1:
                    b = matches
                else:
                    prize = matches
                    n = Node(a, b, prize)
                    nodes.append(n)
            line_num += 1
            line_num %= 4
    return nodes


def part1(nodes):
    total = 0
    t2 = 0
    for n in nodes:
        x = n.find()
        y = n.solve()

        total += x
        t2 += y
    return total, t2


def part2(nodes):
    total = 0
    for n in nodes:
        x = n.solve(part2offset)

        total += x
    return total


input_data = parse_file("q13.txt")
print(part1(input_data))
print(part2(input_data))

# 161411316373072 too high
# 1545093008503 too low
# 106228669504887