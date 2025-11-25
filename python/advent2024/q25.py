import itertools
from collections import defaultdict
from itertools import product

def parse_file(filename):
    out = []
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
        for i in range(0, len(lines), 8):
            t = (lines[i], lines[i+1], lines[i+2], lines[i+3], lines[i+4], lines[i+5], lines[i+6])
            out.append(t)
    return out

def to_locks_keys(lists):
    locks = []
    keys = []
    for grid in lists:
        vals = [0] * 5
        for row in range(1, 6):
            for col in range(0, 5):
                if grid[row][col] == '#':
                    vals[col] += 1
        if '#' in grid[0]:
            locks.append(tuple(vals))
        else:
            keys.append(tuple(vals))
    return locks, keys


def fits(lock, key):
    for i in range(len(lock)):
        if lock[i] + key[i] >= 6:
            return False
    return True

def part1(lists):
    locks, keys = to_locks_keys(lists)
    p = itertools.product(locks, keys)
    return sum(1 for pair in p if fits(*pair))

#def part2(lists):


input_data = parse_file("q25.txt")
print(input_data)
print(part1(input_data))
#print(part2(input_data))
