from collections import defaultdict


# parse grid
def parse_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


def grid_to_dict(grid):
    d = defaultdict(lambda: [])
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if grid[row][col] != '.':
                v = d[grid[row][col]]
                v.append((row, col))

    return d


def find_inodes(p1, p2, rows, cols):
    rdiff = p2[0] - p1[0]
    cdiff = p2[1] - p1[1]

    inode1 = (p1[0] - rdiff, p1[1] - cdiff)
    inode2 = (p2[0] + rdiff, p2[1] + cdiff)
    retval = []
    if inode1[0] in range(0, rows) and inode1[1] in range(0, cols):
        retval.append(inode1)
    if inode2[0] in range(0, rows) and inode2[1] in range(0, cols):
        retval.append(inode2)
    return retval

def find_all_inodes(p1, p2, rows, cols):
    retval = [p1, p2]

    rdiff = p2[0] - p1[0]
    cdiff = p2[1] - p1[1]

    inode = (p1[0] - rdiff, p1[1] - cdiff)
    while inode[0] in range(0, rows) and inode[1] in range(0, cols):
        retval.append(inode)
        inode = (inode[0] - rdiff, inode[1] - cdiff)

    inode = (p2[0] + rdiff, p2[1] + cdiff)
    while inode[0] in range(0, rows) and inode[1] in range(0, cols):
        retval.append(inode)
        inode = (inode[0] + rdiff, inode[1] + cdiff)

    return retval


def solve(grid, part1):
    d = grid_to_dict(grid)
    inodes = set()
    for points in d.values():
        for p1 in range(0, len(points) - 1):
            for p2 in range(p1 + 1, len(points)):
                inds = []
                if part1:
                    inds = find_inodes(points[p1], points[p2], len(grid), len(grid[0]))
                else:
                    inds = find_all_inodes(points[p1], points[p2], len(grid), len(grid[0]))
                inodes.update(inds)

    return len(inodes)

input_data = parse_file("q8.txt")
print(solve(input_data, True))
print(solve(input_data, False))
