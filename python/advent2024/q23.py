import itertools
from collections import defaultdict
import string
from itertools import combinations


def parse_file(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                parsed_data.append(tuple([x for x in (line.split('-'))]))

    return parsed_data


def part1():
    results = set()
    letters = list(string.ascii_lowercase)
    for letter in letters:
        c = 't' + letter
        nodes = network[c]
        for n1, n2 in list(combinations(nodes, 2)):
            if n2 in network[n1]:
                results.add(tuple(sorted([n1, n2, c])))
    return len(results)


def largest_network(root, bsf):
    neighbors = network[root]
    for size in range(len(neighbors), bsf - 1, -1):
        for nodes in itertools.combinations(neighbors, size):
            if all(n1 in network[n2] for n1, n2 in list(combinations(nodes, 2))):
                return list(nodes) + [root]
    return []

def part2():
    letters = list(string.ascii_lowercase)
    bsf = 0
    nodes = []
    for node in network.keys():
        net = largest_network(node, bsf)
        if len(net) >= bsf:
            nodes = net
            bsf = len(net)
    return ','.join(sorted(nodes))


def make_network(pairs):
    network = defaultdict(lambda: set())
    for x, y in pairs:
        network[x].add(y)
        network[y].add(x)
    return network


input_data = parse_file("q23.txt")
# print(input_data)
network = make_network(input_data)
# print(network)
print(part1())
print(part2())

# hc,ia,kh,mw,sc,tc,ux,wd,wp,xp,yv,zx - wrong
# ez,hx,iw,jg,kf,lx,pj,pv,vv,xg,yc,yg
# cb,df,fo,ho,kk,nw,ox,pq,rt,sf,tq,wi,xz