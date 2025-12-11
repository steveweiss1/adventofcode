from collections import defaultdict, namedtuple, deque
# from lib.lib import
import lib.parser
from scipy.optimize import linprog
import numpy as np

Row = namedtuple('Row', ['lights', 'buttons', 'joltage'])

def part1(rows):
    return sum([solve1(row) for row in rows])

def part2(rows):
    return sum([solve2(row) for row in rows])


def parse_file(filename):
    with open(filename, 'r') as file:
        rows = []
        for line in file:
            row = line.strip().split(' ')
            lights = row[0][1:-1]
            joltage = tuple(map(int, row[-1][1:-1].split(',')))
            buttons = [tuple(map(int, b[1:-1].split(','))) for b in row[1:-1]]
            rows.append(Row(lights, buttons, joltage))
        return rows

def press(lights, button):
    out = list(lights)
    for i in button:
        out[i] = '.' if out[i] == '#' else '#'
    return ''.join(out)

def solve1(row):
    d = deque()
    lights = '.' * len(row.lights)
    d.append((lights, 0, row.buttons))
    while d:
        l, turn, buttons = d.popleft()
        if l == row.lights:
            return turn
        for i, b in enumerate(buttons):
            pressed = press(l, b)
            d.append((pressed, turn+1, buttons[:i] + buttons[i+1:]))

def solve2(row):
    array = [[0] * len(row.buttons) for j in row.joltage]
    for i, button in enumerate(row.buttons):
        for b in button:
            array[b][i] = 1
    print(array)
    a = np.array(array)
    b = np.array(row.joltage)
    c = np.ones(a.shape[1])

    res = linprog(c, A_eq=a, b_eq=b, integrality=1)
    if res.success:
        solution = np.round(res.x).astype(int)
        # print("Solution:", solution)
        return sum(solution)
    else:
        print("No solution found")
        return 0


input_data = parse_file("q10.txt")
print(part1(input_data))
print(part2(input_data))
