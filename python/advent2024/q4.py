from collections import defaultdict


def parse_file(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                parsed_data.append(line)

    return parsed_data


row = 0
col = 0
def part1(sg):
    total = 0

    for row in range(0, height):
        for col in range(0, width):
            if sg[(row, col)] == 'X':
                # right
                if sg[(row, col+1)] == 'M' and sg[(row, col+2)] == 'A' and sg[(row, col+3)] == 'S':
                    total += 1
                # left
                if sg[(row, col-1)] == 'M' and sg[(row, col-2)] == 'A' and sg[(row, col-3)] == 'S':
                    total += 1
                # down
                if sg[(row+1, col)] == 'M' and sg[(row+2, col)] == 'A' and sg[(row+3, col)] == 'S':
                    total += 1
                # up
                if sg[(row-1, col)] == 'M' and sg[(row-2, col)] == 'A' and sg[(row-3, col)] == 'S':
                    total += 1
                # down and right
                if sg[(row+1, col+1)] == 'M' and sg[(row+2, col+2)] == 'A' and sg[(row+3, col+3)] == 'S':
                    total += 1
                # down and left
                if sg[(row+1, col-1)] == 'M' and sg[(row+2, col-2)] == 'A' and sg[(row+3, col-3)] == 'S':
                    total += 1
                # up and right
                if sg[(row-1, col+1)] == 'M' and sg[(row-2, col+2)] == 'A' and sg[(row-3, col+3)] == 'S':
                    total += 1
                # up and left
                if sg[(row-1, col-1)] == 'M' and sg[(row-2, col-2)] == 'A' and sg[(row-3, col-3)] == 'S':
                    total += 1
    return total

def part2(sg):
    total = 0

    for row in range(0, height):
        for col in range(0, width):
            if sg[(row, col)] == 'A':
                left = (sg[(row-1, col-1)] == 'M' and sg[(row+1, col+1)] == 'S') or (sg[(row-1, col-1)] == 'S' and sg[(row+1, col+1)] == 'M')
                right = (sg[(row-1, col+1)] == 'M' and sg[(row+1, col-1)] == 'S') or (sg[(row-1, col+1)] == 'S' and sg[(row+1, col-1)] == 'M')
                if left and right:
                    total += 1
    return total

grid = parse_file("q4.txt")

sg = defaultdict(lambda: 'Q')

width = len(grid[0])
height = len(grid)


for row in range(0, height):
    for col in range(0, width):
        sg[(row, col)] = grid[row][col]

print(part1(sg))
print(part2(sg))
