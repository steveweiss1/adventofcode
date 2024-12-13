from collections import defaultdict


def parse_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


start_row = 0
start_col = 0

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def part1(grid):
    seen = set()
    seen.add((start_row, start_col))
    dir = 0
    row = start_row
    col = start_col
    while 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        next_row = row + dirs[dir][0]
        next_col = col + dirs[dir][1]
        if not (0 <= next_row < len(grid) and 0 <= next_col < len(grid[0])):
            return len(seen)
        if grid[next_row][next_col] != '#':
            row = next_row
            col = next_col
            seen.add((row, col))
        else:
            dir = (dir + 1) % 4

    return len(seen)


def is_loop(grid, r, c):
    seen = set()
    dir = 0
    row = start_row
    col = start_col
    while 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        next_row = row + dirs[dir][0]
        next_col = col + dirs[dir][1]
        if (next_row, next_col, dir) in seen:
            return True
        if not (0 <= next_row < len(grid) and 0 <= next_col < len(grid[0])):
            return False
        if grid[next_row][next_col] != '#' and (next_row != r or next_col != c):
            row = next_row
            col = next_col
            seen.add((row, col, dir))
        else:
            dir = (dir + 1) % 4

    return False


def part2(grid):
    loops = 0
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if grid[row][col] == '.':
                loops += is_loop(grid, row, col)

    return loops


input_data = parse_file("q6.txt")

for row in range(0, len(input_data)):
    try:
        ind = input_data[row].index('^')
        start_row = row
        start_col = ind
        break
    except ValueError:
        ind = -1

print(part1(input_data))
print(part2(input_data))
