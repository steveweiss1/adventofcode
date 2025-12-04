from collections import defaultdict
import heapq

adjacents = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            # Handle non-unique values by appending to a list
            if isinstance(inverted[value], list):
                inverted[value].append(key)
            else:
                inverted[value] = [inverted[value], key]
        else:
            inverted[value] = key
    return inverted


def list_to_tuples(lst, size=3):
    # Create tuples of the specified size using zip and iter
    it = iter(lst)
    return list(zip(*[it] * size))


def zip_pairs(lst):
    return list(zip(lst[:-1], lst[1:]))


def find_all_occurrences(text, pattern):
    indexes = []
    start = 0
    while start < len(text):
        index = text.find(pattern, start)
        if index == -1:
            break  # No more occurrences found
        indexes.append(index)
        start = index + len(pattern)  # Move past the current match
    return indexes


def grid_to_default_dict(grid, default):
    sg = defaultdict(lambda: default)

    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            sg[(row, col)] = grid[row][col]

    return sg


def flatten(l):
    return sum(l, [])

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]


def dijkstra(graph, start):
    """
    Compute the shortest paths from the start node to all other nodes in the graph.
    
    Parameters:
        graph (dict): adjacency list representation, e.g.
                      {
                          'A': {'B': 1, 'C': 4},
                          'B': {'A': 1, 'C': 2, 'D': 5},
                          'C': {'A': 4, 'B': 2, 'D': 1},
                          'D': {'B': 5, 'C': 1}
                      }
        start: starting node label
        
    Returns:
        distances (dict): shortest known distance from start to each node
        previous (dict): previous node on the shortest path
    """
    # Initialize distances and previous nodes
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0

    # Priority queue: (distance, node)
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # Skip if we already found a better path
        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous
