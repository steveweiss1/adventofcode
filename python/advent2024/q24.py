from collections import defaultdict
from copy import deepcopy
from itertools import permutations


def parse_file(filename):
    vals = dict()
    gates = dict()

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                if ':' in line:
                    l = line.split(':')
                    vals[l[0]] = int(l[1].strip())
                elif '->' in line:
                    l = line.split(' ')
                    gates[l[4]] = (l[0], l[1], l[2])
        return vals, gates


def compute(start, vals, gates):
    if start in vals:
        return vals[start]
    gate = gates[start]
    v1 = compute(gate[0], vals, gates)
    v2 = compute(gate[2], vals, gates)
    op = gate[1]
    res = ''
    if op == 'AND':
        res = v1 & v2
    elif op == 'OR':
        res = v1 | v2
    elif op == 'XOR':
        res = v1 ^ v2
    else:
        raise Exception("invalid " + op)
    vals[start] = res
    return res


def part1(vals, gates):
    result = 0
    for i in range(0, 100):
        padded = str(i).zfill(2)
        v = 'z' + padded
        if v not in gates:
            break
        bit = compute(v, vals, gates)
        bit <<= i
        result |= bit

    return result


def to_formula(i, name, gates):
    gate = gates[name]
    p1 = ''
    p2 = ''
    if gate[0][0] == 'x' or gate[0][0] == 'y':
        p1 = gate[0]
    else:
        p1 = '(' + to_formula(i, gate[0], gates) + ')'
    if gate[2][0] == 'x' or gate[2][0] == 'y':
        p2 = gate[2]
    else:
        p2 = '(' + to_formula(i, gate[2], gates) + ')'
    if len(p1) > len(p2):
        tmp = p1
        p1 = p2
        p2 = tmp
    return p1 + ' ' + gate[1] + ' ' + p2


def part2(vals, gates):
    print(expected_sum(vals, gates))
    for i in range(0, 45):
        v = to_formula(i, 'z' + str(i).zfill(2), gates)
        print(f"{str(i).zfill(2)}: {v}")

def part2a(vals, gates):
    expected = expected_sum(vals, gates)
    perms = permutations(gates.keys(), 8)
    overrides = dict()
    for perm in perms:
        for i in range(0, 8, 2):
            overrides[perm[i]] = perm[i + 1]
            overrides[perm[i + 1]] = perm[i]
        try:
            result = solve(gates, vals, overrides)
            if result == expected:
                return ','.join(sorted(perm))
        except ArithmeticError:
            pass
    return None


def toInt(prefix, vals, maxNum):
    result = 0
    for i in range(0, maxNum + 1):
        padded = str(i).zfill(2)
        v = vals[prefix + padded]
        v <<= i
        result |= v
    return result


def expected_sum(vals, gates):
    x = toInt('x', vals, 44)
    print(f"x={x}")
    y = toInt('y', vals, 44)
    print(f"y={y}")
    return x + y


input_data = parse_file("q24.txt")
# print(input_data)
print(part1(*input_data))
print(part2(*input_data))
print(','.join(sorted(['z32','grm','z10','ggn','ndw','jcb','z39','twr'])))

#z32, grm
# z10, ggn
# ndw, jcb
#z39, twr