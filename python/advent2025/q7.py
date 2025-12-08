from collections import defaultdict, namedtuple
# from lib.lib import
import lib.parser


def part1(grid, start):
    return len(splits(grid, start[0], start[1]))


cache = {}


def splits(grid, r, c):
    key = (r, c)
    if key in cache:
        return cache[key]
    if r < 0 or r >= len(grid) or c < -1 or c >= len(grid[0]):
        return set()
    for row in range(r + 1, len(grid)):
        if grid[row][c] == '^':
            output = {(row, c)} | splits(grid, row, c - 1) | splits(grid, row, c + 1)
            cache[key] = output
            return output
    return set()


cache2 = {}

def unique_paths(grid, r, c):
    key = (r, c)
    if key in cache2:
        return cache2[key]
    if r < 0 or r >= len(grid) or c < -1 or c >= len(grid[0]):
        return 0
    for row in range(r + 1, len(grid)):
        if grid[row][c] == '^':
            left = unique_paths(grid, row, c - 1)
            right = unique_paths(grid, row, c + 1)
            output = left + right + 1
            cache2[key] = output
            return output
    return 0

def part2(grid, start):
    return unique_paths(grid, start[0], start[1]) + 1


def parse_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


grid, start = lib.parser.parse_grid_with_start("q7.txt")
# print(grid)
print(start)
print(part1(grid, start))
print(part2(grid, start))
