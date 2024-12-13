from collections import defaultdict
from lib.lib import toInt


def parse_file(filename):
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


def is_valid(pairs, num_list):
    for i in range(0, len(num_list) - 1):
        for j in range(i + 1, len(num_list)):
            if (num_list[j], num_list[i]) in pairs:
                return False
    return True


def make_valid(pairs, num_list):
    made_change = False
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(num_list) - 1):
            for j in range(i + 1, len(num_list)):
                if (num_list[j], num_list[i]) in pairs:
                    made_change = True
                    swapped = True
                    tmp = num_list[i]
                    num_list[i] = num_list[j]
                    num_list[j] = tmp
    return made_change


def part1(pairs, lists):
    total = 0
    for l in lists:
        if is_valid(pairs, l):
            total += l[int(len(l) / 2)]

    return total


def part2(pairs, lists):
    total = 0
    for l in lists:
        changed = make_valid(pairs, l)
        if changed:
            total += l[int(len(l) / 2)]

    return total


pairs, lists = parse_file("q5.txt")
print(part2(pairs, lists))
