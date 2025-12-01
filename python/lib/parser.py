import re
from collections import namedtuple

# 1 2
def parse_int_pairs(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                parsed_data.append([int(x) for x in (line.split())])

    return parsed_data

# mul(826,659)
def parse_mul_regex(filename):
    parsed_data = []
    pattern = r'mul\((\d+),(\d+)\)'

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                matches = re.findall(pattern, line)
                parsed_data += matches

    return parsed_data

def parse_lines(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def parse_tuples_and_lists(filename):
    pairs = set()
    lists = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                if '|' in line:
                    l = tuple(map(int, line.split("|")))
                    pairs.add(l)
                else:
                    l = list(map(int, line.split(',')))
                    lists.append(l)

    return pairs, lists

# 61750: 3 3 1 736 12
def parse_ints_strip_colon(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            line = line.replace(":", "")
            if line:
                parsed_data.append([int(x) for x in (line.split())])

    return parsed_data

# Button A: X+47, Y+79
# Button B: X+84, Y+16
# Prize: X=7244, Y=1660
# Node should be a namedtuple or class
def parse_three_line_groups(filename, Node):
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


def parse_grid_and_directions(filename):
    grid = []
    directions = ''

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                if '#' in line:
                    grid.append(list(line))
                elif '<' in line:
                    directions += line

    return (grid, directions)

def parse_grid_with_start(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file]
        start = None
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 'S':
                    start = (r, c)
                    break
        return grid, start

# L25
def parse_pairs(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                direction = line[0]
                num = int(line[1:])
                parsed_data.append((direction, num))

    return parsed_data