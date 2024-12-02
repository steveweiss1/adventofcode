from collections import defaultdict


def parse_file(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                parsed_data.append([int(x) for x in (line.split())])

    return parsed_data


def is_gradual(vals):
    if vals == sorted(vals) or vals == sorted(vals, reverse=True):
        pairs = list(zip(vals[:-1], vals[1:]))
        for p in pairs:
            if p[0] == p[1]:
                return 0
            if abs(p[0] - p[1]) > 3:
                return 0
        return 1
    return 0


def is_gradual_for_any(vals):
    if is_gradual(vals):
        return True
    for i in range(0, len(vals)):
        v = vals.copy()
        v.pop(i)
        if is_gradual(v):
            return True
    return False

def part1(lists):
    return sum([is_gradual(l) for l in lists])

def part2(lists):
    return sum([is_gradual_for_any(l) for l in lists])


input_data = parse_file("q2.txt")
print(part1(input_data))
print(part2(input_data))
