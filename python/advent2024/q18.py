from collections import defaultdict
import heapq


def parse_file(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                parsed_data.append(tuple([int(x) for x in (line.split(','))]))

    return parsed_data


def dijkstra(start, end, blocks):
    # dijkstra time
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    # Dictionary to store the shortest distance to each node
    shortest_distances = defaultdict(lambda: float('inf'))
    shortest_distances[start] = 0

    # Dictionary to store the shortest path tree
    nodes_in_paths = {start}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if a shorter path to the node has already been found
        # if current_distance > shortest_distances[current_node]:
        #    continue

        # Explore neighbors
        for neighbor in [(current_node[0], current_node[1] + 1), (current_node[0], current_node[1] - 1),
                         (current_node[0] + 1, current_node[1]), (current_node[0] - 1, current_node[1])]:
            if neighbor in blocks:
                continue

            if neighbor[0] not in range(start[0], end[0] + 1) or neighbor[1] not in range(start[1], end[1] + 1):
                continue

            distance = current_distance + 1

            # If a shorter path is found
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_distances[end]


def part1(pairs, num_pairs, max_x, max_y):
    blocks = set()
    blocks.update(pairs[:num_pairs])
    return dijkstra((0, 0), (max_x, max_y), blocks)


def part2(pairs, max_x, max_y):
    blocks = set()
    for p in pairs:
        blocks.add(p)
        d = dijkstra((0, 0), (max_x, max_y), blocks)
        if d == float('inf'):
            return p
    return

# def part2(lists):

# test
input_data = parse_file("q18-dev.txt")
# print(part1(input_data, 12, 6, 6))
# print(part2(input_data,  6, 6))


input_data = parse_file("q18.txt")
print(part1(input_data, 1024, 70, 70))
print(part2(input_data,  70, 70))

# print(part2(input_data))
