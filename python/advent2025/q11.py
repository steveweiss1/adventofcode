from collections import defaultdict


def bt(node, graph, cache, out):
    if node == out:
        return 1
    key = node
    if key in cache:
        return cache[key]
    total = 0
    for output in graph[node]:
        total += bt(output, graph, cache, out)
    cache[key] = total
    return total


def part1(lines):
    graph = {line[0]: line[1:] for line in lines}

    return bt('you', graph, {}, 'out')


def part2(lines):
    graph = defaultdict(list)
    for line in lines:
        graph[line[0]] = line[1:]
        
    to_fft = bt('svr', graph, {}, 'fft')
    to_dac = bt('fft', graph, {}, 'dac')
    to_out = bt('dac', graph, {}, 'out')

    return to_dac * to_fft * to_out

def parse_file(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            words[0] = words[0][:-1]
            lines.append(words)
    return lines


input_data = parse_file("q11.txt")
# print(input_data)
print(part1(input_data))
print(part2(input_data))
