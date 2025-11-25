from collections import defaultdict
import heapq
import copy


def parse_file(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file]
        start = None
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 'S':
                    start = (r, c)
                    break
        return grid, start


def bfs(grid, start):
    visited = {start}
    queue = [(start, [start])]
    while len(queue) > 0:
        node, path = queue.pop(0)
        if grid[node[0]][node[1]] == 'E':
            return len(path), path
        for dr, dc in dirs:
            neighbor = (node[0] + dr, node[1] + dc)
            if neighbor in visited:
                continue
            if grid[neighbor[0]][neighbor[1]] == '#':
                continue
            visited.add(neighbor)
            queue.append((neighbor, path + [neighbor]))



dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def part1(grid, start):
    result = 0
    base, path = bfs(grid, start)
    dct = defaultdict(int)
    removed = set()
    for node in path:
        for d in dirs:
            neighbor_r = node[0] + d[0]
            neighbor_c = node[1] + d[1]

            if (neighbor_r in range(1, len(grid) - 1) and neighbor_c in range(1, len(grid[0]) - 1) and
                    grid[neighbor_r][neighbor_c] == '#' and (neighbor_r, neighbor_c) not in removed):
                nr2 = neighbor_r + d[0]
                nc2 = neighbor_c + d[1]
                if grid[nr2][nc2] != '#':
                    if neighbor_c % 50 == 0:
                        print(f"removing {neighbor_r} {neighbor_c}")
                    removed.add((neighbor_r, neighbor_c))
                    cloned = copy.deepcopy(grid)
                    cloned[neighbor_r][neighbor_c] = '.'
                    shortest, _ = bfs(cloned, start)
                    if shortest < base:
                        dct[base - shortest] += 1
                    if base - shortest >= 100:
                        result += 1
    return result


def part2(grid, start):
    result = 0
    s, path = bfs(grid, start)

    for i1 in range(len(path) - 1):
        for i2 in range(i1 + 80, len(path)):
            p1 = path[i1]
            p2 = path[i2]
            dist = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
            if dist <= 20 and i2 - i1 - dist >= 100:
                result += 1
    return result


input_data = parse_file("q20.txt")
# print(input_data)
# print(part1(*input_data))
print(part2(*input_data))
