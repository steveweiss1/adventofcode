from collections import defaultdict


def parse_file(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                parsed_data.append([int(x) for x in line])

    return parsed_data


cache = dict()


def dfs(grid, expected, row, col):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    if row not in range(len(grid)) or col not in range(len(grid[0])):
        return set()

    val = grid[row][col]

    if val != expected:
        return set()

    if val == 9:
        return {(row, col)}

    if (row, col) in cache:
        return cache[(row, col)]

    all_nines = set()

    for d in dirs:
        s = dfs(grid, val + 1, row + d[0], col + d[1])
        all_nines = all_nines | s

    cache[(row, col)] = all_nines
    return all_nines

def dfs2(grid, expected, row, col):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    if row not in range(len(grid)) or col not in range(len(grid[0])):
        return 0

    val = grid[row][col]

    if val != expected:
        return 0

    if val == 9:
        return 1

    if (row, col) in cache:
        return cache[(row, col)]

    paths = 0

    for d in dirs:
        paths += dfs2(grid, val + 1, row + d[0], col + d[1])

    cache[(row, col)] = paths
    return paths


def solve(grid, use1):
    cache.clear()
    total = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                if use1:
                    vals = dfs(grid, 0, row, col)
                    k = len(vals)
                else:
                    k = dfs2(grid, 0, row, col)
                total += k

    return total


# def part2(lists):


input_data = parse_file("q10.txt")
print(input_data)
#print(solve(input_data, True))
print(solve(input_data, False))
