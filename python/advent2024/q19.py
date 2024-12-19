from collections import defaultdict


def parse_file(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]

    colors = set(lines[0].split(','))
    return colors, lines[2:]


cache = dict()


def is_valid(s, colors):
    if s in colors:
        return True
    if s in cache:
        return cache[s]
    for i in range(1, len(s)):
        if s[:i] in colors and is_valid(s[i:], colors):
            cache[s] = True
            return True
    cache[s] = False
    return False


ncache = dict()


def num_valid(s, colors):
    if not is_valid(s, colors):
        return 0
    if s in ncache:
        return ncache[s]
    total = 0
    if s in colors:
        total = 1
    for i in range(1, len(s)):
        if s[:i] in colors:
            total += num_valid(s[i:], colors)
    ncache[s] = total
    return total


def part1(colors, lines):
    return sum([is_valid(line, colors) for line in lines])


def part2(colors, lines):
    return sum([num_valid(line, colors) for line in lines])


input_data = parse_file("q19.txt")
print(input_data)
print(part1(*input_data))
print(part2(*input_data))
