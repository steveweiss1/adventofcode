import re
import copy

def parse_file(filename, num_cols):
    columns = [[] for _ in range(num_cols)]
    instructions = []

    pattern = r'move (\d+) from (\d+) to (\d+)'
    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            if line:
                if '[' in line:
                    for i in range(0, num_cols):
                        pos = 1 + i * 4
                        if pos < len(line):
                            c = line[pos]
                            if c != ' ':
                                columns[i].append(c)
                elif line.startswith('move'):
                    line = line.strip()
                    match = re.match(pattern, line)
                    if match:
                        x, y, z = map(int, match.groups())
                        instructions.append((x, y, z))

    return columns, instructions

def part1(columns, instructions):
    columns = copy.deepcopy(columns)
    for count, c_from, c_to in instructions:
        for i in range(0, count):
            box = columns[c_from-1].pop(0)
            columns[c_to-1].insert(0, box)

    first_elements = [col[0] for col in columns if col]
    return ''.join(first_elements)


def part2(columns, instructions):
    columns = copy.deepcopy(columns)
    for count, c_from, c_to in instructions:
        tmp = []
        for i in range(0, count):
            box = columns[c_from-1].pop(0)
            tmp.append(box)
        columns[c_to-1] = tmp + columns[c_to-1]

    first_elements = [col[0] for col in columns if col]
    return ''.join(first_elements)

# Example usage
filename = "q05.txt"
total_columns = 9
cols, inst = parse_file(filename, total_columns)
#  print(cols)
#  print(inst)
print(part1(cols, inst))
print(part2(cols, inst))