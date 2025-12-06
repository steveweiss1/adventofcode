import re

start = {'*': 1, '+': 0}
funcs = {'*': lambda x, y: x * y, '+': lambda x, y: x + y}

def part1(rows, operators):
    cols = len(rows[0])

    total = 0
    for c in range(cols):
        result = start[operators[c]]
        for row in rows:
            result = funcs[operators[c]](result, row[c])
        total += result
    return total


def next_plus_or_star(s, idx):
    m = re.search(r'[+*]', s[idx + 1:])
    return len(
        s) + 100 if m is None else idx + 1 + m.start()  # hacky but it just has to be greater than the list's length


def part2(rows, operators):
    rowlen = max([len(r) for r in rows])
    next_op_col = 0
    total = 0
    op, result = None, None
    for col in range(rowlen):
        if col == next_op_col:
            next_op_col = next_plus_or_star(operators, col)
            op = operators[col]
            result = start[op]
        number = 0
        has_numeric = False
        for row in rows:
            if col < len(row):
                c = row[col]
                if c.isnumeric():
                    has_numeric = True
                    val = int(c)
                    number = number * 10 + val
        if has_numeric:
            result = funcs[op](result, number)
        if col == next_op_col - 1 or col == rowlen - 1:
            total += result
    return total


def parse_file1(filename):
    data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines[:-1]:
            data.append(list(map(int, line.strip().split())))
        return data, lines[-1].strip().split()


def parse_file2(filename):
    with open(filename, 'r') as file:
        return file.readlines()


filename = "q6.txt"
input_data = parse_file1(filename)
print(part1(*input_data))

input_data = parse_file2(filename)
print(part2(input_data[:-1], input_data[-1]))
