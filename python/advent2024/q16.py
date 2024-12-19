from collections import defaultdict
import heapq


def parse_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dijkstra(grid, start, end, start_direction=(0, 1)):
    # dijkstra time
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, start_direction))

    # Dictionary to store the shortest distance to each node
    shortest_distances = defaultdict(lambda: float('inf'))
    shortest_distances[(start, (0, 1))] = 0

    # Dictionary to store the shortest path tree
    previous_nodes = defaultdict(lambda: {})
    nodes_in_paths = {start}

    while priority_queue:
        current_distance, current_node, dir = heapq.heappop(priority_queue)

        # Skip if a shorter path to the node has already been found
        # if current_distance > shortest_distances[current_node]:
        #    continue

        # Explore neighbors
        for neighbor in [(current_node[0], current_node[1] + 1), (current_node[0], current_node[1] - 1),
                         (current_node[0] + 1, current_node[1]), (current_node[0] - 1, current_node[1])]:
            if grid[neighbor[0]][neighbor[1]] == '#':
                continue

            distance = current_distance + 1

            new_dir = (neighbor[0] - current_node[0], neighbor[1] - current_node[1])
            if (new_dir[0] + dir[0], new_dir[1] + dir[1]) == (0, 0):
                continue

            changed = new_dir != dir
            if changed:
                distance += 1000

            # If a shorter path is found
            if distance < shortest_distances[(neighbor, new_dir)]:
                shortest_distances[(neighbor, new_dir)] = distance
                previous_nodes[neighbor][new_dir] = (current_node, changed)
                heapq.heappush(priority_queue, (distance, neighbor, new_dir))

    queue = [end]

    while len(queue) > 0:
        # print(queue)
        node = queue.pop(0)

        nodes_in_paths.add(node)
        distances = sorted([(shortest_distances[(node, d)], d) for d in dirs])
        # print(f"{node} -> {previous_nodes[node]}")
        if node != start:
            if len(previous_nodes[node]) == 0:
                return 0, (), {}
            queue.append(previous_nodes[node][distances[0][1]][0])

    results = sorted([(shortest_distances[(end, d)], d) for d in dirs])
    return results[0][0], results[0][1], nodes_in_paths


def part1(grid):
    start = ()
    end = ()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'S':
                start = (row, col)
            elif grid[row][col] == 'E':
                end = (row, col)

    return dijkstra(grid, start, end)[0]


input_data = parse_file("q16.txt")
# print(input_data)
# print(dijkstra(input_data))
print(part1(input_data))

# 94448 - too high
# 84448 - too low
# 93448 - too low
# 94447 - wrong
# 93449 - wrong
# 94436 - right

# 469 too low
# 470 - too low
# 540 - too high
# 490 - wrong
# 516 wrong
# 517- wrong
