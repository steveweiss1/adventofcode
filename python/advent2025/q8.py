import math
from collections import defaultdict
from itertools import combinations


def process(points, num_connections=0):
    combos = combinations(points, 2)
    distances = [(distance(a, b), a, b) for a, b in combos]
    distances.sort()

    #Part1
    if num_connections > 0:
        distances = distances[:num_connections]

    point_to_network = {}
    network_to_points = defaultdict(set)
    next_network = 0
    for _, p, q in distances:
        if p not in point_to_network and q not in point_to_network:
            point_to_network[p] = next_network
            point_to_network[q] = next_network
            network_to_points[next_network] |= {p, q}
            next_network += 1
        elif p in point_to_network and q in point_to_network:
            if point_to_network[p] == point_to_network[q]:
                continue
            else:
                old_net = point_to_network[q]
                for point in network_to_points[point_to_network[q]]:
                    point_to_network[point] = point_to_network[p]
                network_to_points[point_to_network[p]] |= network_to_points[old_net]
                del network_to_points[old_net]
        elif p in point_to_network:
            point_to_network[q] = point_to_network[p]
            network_to_points[point_to_network[p]].add(q)
        else:
            point_to_network[p] = point_to_network[q]
            network_to_points[point_to_network[q]].add(p)
        # Part 2
        if (num_connections == 0 and len(network_to_points) == 1 and
                len(network_to_points[point_to_network[p]]) == len(points)):
            return p[0] * q[0]

    #Part 1
    biggest_nets = sorted(network_to_points.values(), key=lambda x: len(x), reverse=True)
    return len(biggest_nets[0]) * len(biggest_nets[1]) * len(biggest_nets[2])


def parse_file(filename):
    with open(filename, 'r') as file:
        return [tuple(map(int, (line.strip().split(',')))) for line in file]


def distance(p, q):
    return math.sqrt(pow(p[0] - q[0], 2) + pow(p[1] - q[1], 2) + pow(p[2] - q[2], 2))


input_data = parse_file("q8.txt")
# part 1
#print(process(input_data, 1000))
#part 2
print(process(input_data, ))
