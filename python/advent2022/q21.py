import sys


def parse_file(filename):
    parsed_data = {}

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                parts = line.split(':')
                val = parts[1].strip()
                if val.isdigit():
                    parsed_data[parts[0]] = int(val)
                else:
                    v = val.split()
                    parsed_data[parts[0]] = {'l': v[0], 'op': v[1], 'r': v[2]}

    return parsed_data


def compute(tree, node):
    val = tree[node]
    if isinstance(val, int):
        return val
    v1 = compute(tree, val['l'])
    v2 = compute(tree, val['r'])
    op = val['op']
    if op == '+':
        s = v1 + v2
    elif op == '-':
        s = v1 - v2
    elif op == '*':
        s = v1 * v2
    else:
        if v1 % v2 != 0:
            raise ValueError('no')
        s = v1 / v2
    tree[node] = s
    return s


def part1(tree):
    return compute(tree, 'root')


def part2(tree):
    l = tree['root']['l']
    r = tree['root']['r']
    for i in range(3378946525351, 6000000000000, 100):
        t = tree.copy()
        t['humn'] = i
        try:
            v1 = compute(t, l)
            v2 = compute(t, r)
            if v1 == v2:
                return i
            else:
                print(f'{i} {v1} {v2}')
        except ValueError:
            continue


filename = "q21.txt"
parsed_data = parse_file(filename)

# print(part1(parsed_data.copy()))
print(part2(parsed_data.copy()))
