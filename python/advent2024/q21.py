from collections import defaultdict
from lib.lib import flatten_list

L = '<'
R = '>'
U = '^'
D = 'v'
A = 'A'

number_grid = {
    '0': [(A, R), ('2', U)],
    A: [('0', L), ('3', U)],
    '1': [('2', R), ('4', U)],
    '2': [('1', L), ('0', D), ('3', R), ('5', U)],
    '3': [('2', L), (A, D), ('6', U)],
    '4': [('1', D), ('5', R), ('7', U)],
    '5': [('4', L), ('2', D), ('6', R), ('8', U)],
    '6': [('5', L), ('3', D), ('9', U)],
    '7': [('4', D), ('8', R)],
    '8': [('7', L), ('5', D), ('9', R)],
    '9': [('6', D), ('8', L)]
}

arrows = {
    A: [(U, L), (R, D)],
    U: [(A, R), (D, D)],
    R: [(A, U), (D, L)],
    D: [(U, U), (L, L), (R, R)],
    L: [(D, R)]
}

bfs_cache = dict()


def bfs(start, end, dct):
    queue = [(start, '')]
    results = []
    key = (start, end)
    if key in bfs_cache:
        return bfs_cache[key]
    while len(queue) > 0:
        node, path = queue.pop(0)
        if node == end:
            if len(results) == 0 or len(results[0]) == len(path):
                results.append(path)
            if len(results[0]) < len(path):
                s = sorted([(num_turns(r), r + A) for r in results])
                s = list(filter(lambda x: x[0] == s[0][0], s))
                res = [x[1] for x in s]
                bfs_cache[key] = res
                return res
        for neighbor, direction in dct[node]:
            # if neighbor not in path:
            queue.append((neighbor, path + direction))
    s = sorted([(num_turns(r), r + A) for r in results])
    s = list(filter(lambda x: x[0] == s[0][0], s))
    res = [x[1] for x in s]
    bfs_cache[key] = res
    return res


def num_turns(s):
    total = 0
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            total += 1
    return total


def num_turns2(s):
    total = 0
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            total += 1
            if s[i] == '<':
                total += 1
    return total


def solve(code, dct, cache, lenOnly=False):
    code = f"A{code}"
    results = ['']
    if code in cache:
        return cache[code]

    for i in range(len(code) - 1):
        key = (code[i], code[i + 1])
        if key in cache:
            paths = cache.get(key)
        else:
            paths = bfs(code[i], code[i + 1], dct)
        if lenOnly:
            paths = [paths[0]]
        tmp = []
        for r in results:
            for p in paths:
                tmp.append(r + p)
        results = tmp
        # cache[key] = results.copy()
    d = defaultdict(int)
    for r in results:
        d[len(r)] += 1
    cache[code] = results
    if lenOnly:
        return num_turns2(results[0])
    return results


def solve_recurse(code, dct, cache):
    if len(code) < 2:
        return []
    if code in cache:
        return cache[code]
    paths = bfs(code[0], code[1], dct)
    if len(code) > 2:
        tail = solve_recurse(code[1:], dct, cache)
        results = []
        for p in paths:
            for t in tail:
                results.append(p + t)
    else:
        results = paths
    cache[code] = results
    return results


def parse_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


def part1(input_data):
    total = 0
    cache = dict()
    len_cache = dict()
    for combo in input_data:
        s = solve(combo, number_grid, cache)
        lengths = [len(z) for z in s]
        d = defaultdict(int)
        for l in lengths:
            d[l] += 1
        # print(d)

        lens = [(t, solve(t, arrows, len_cache, True)) for t in s]
        min_len = min([l[1] for l in lens])
        s = list(filter(lambda x: x[1] == min_len, lens))
        s = [p[0] for p in s]

        s2 = flatten_list([solve(t, arrows, cache) for t in s])
        lengths = [len(s) for s in s2]
        d = defaultdict(int)
        for l in lengths:
            d[l] += 1
        # print(d)
        shortest = min(lengths)
        s2 = list(filter(lambda x: len(x) == shortest, s2))
        print(s2)

        lens = [(t, solve(t, arrows, len_cache, True)) for t in s2]
        min_len = min([l[1] for l in lens])
        s2 = list(filter(lambda x: x[1] == min_len, lens))
        s2 = [p[0] for p in s2]

        s3 = flatten_list([solve(t, arrows, cache) for t in s2])
        lengths = [len(s) for s in s3]
        d = defaultdict(int)
        for l in lengths:
            d[l] += 1
        print(d)
        shortest = min(lengths)
        result = shortest * int(combo[:-1])
        total += result
    return total


def part2(input_data):
    total = 0
    cache = dict()
    len_cache = dict()

    for combo in input_data:
        s = solve(combo, number_grid, cache)
        for i in range(2):
            print(combo, i)
            lens = [(t, solve(t, arrows, len_cache, True)) for t in s]
            min_len = min([l[1] for l in lens])
            s = list(filter(lambda x: x[1] == min_len, lens))
            s = [p[0] for p in s]

            s = flatten_list([solve_recurse(A + t, arrows, cache) for t in s])
            shortest = min([num_turns2(x) for x in s])
            s = list(filter(lambda x: num_turns2(x) == shortest, s))
            s = s[:1]
        shortest = min([len(s) for s in s])
        result = shortest * int(combo[:-1])
        total += result
    return total


input_data = parse_file("q21.txt")
print(input_data)
print(part1(input_data))
print(part2(input_data))
