from collections import defaultdict
import re
from lib.lib import find_all_occurrences, zip_pairs


def parse_file(filename):
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


def part2(filename):
    pattern = r'mul\((\d+),(\d+)\)'
    full_line = ''

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                full_line += line

    i_do = find_all_occurrences(full_line, 'do()')
    j_do = [(i, True) for i in i_do]
    i_dont = find_all_occurrences(full_line, 'don\'t()')
    j_dont = [(i, False) for i in i_dont]
    all_pairs = sorted(j_do + j_dont + [(0, True), (len(full_line), False)])
    sorted_segments = zip_pairs(all_pairs)
    total = 0
    for start, end in sorted_segments:
        if not start[1]:
            continue
        sub = full_line[start[0]: end[0]]
        matches = re.findall(pattern, sub)
        total += sum([int(x) * int(y) for x, y in matches])

    return total

def part1(pairs):
    return sum([int(x) * int(y) for x, y in pairs])


filename = "q3.txt"

input_data = parse_file(filename)
print(part2(filename))
part2a(filename)
