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


H = 'h'
V = 'v'

T = 't'
B = 'b'

def process(grid, row, col, seen, val):
    if (row, col) in seen:
        return set(), set()
    if row not in range(len(grid)) or col not in range(len(grid[0])):
        return set(), set()
    if grid[row][col] != val:
        return set(), set()
    seen.add((row, col))
    points = [(row, col)]
    # per = [(row, col, row, col+1), (row, col, row+1, col), (row, col+1, row+1, col+1), (row+1, col, row+1, col+1)]
    per = [(H, row, col, col + 1, T), (H, row + 1, col, col + 1, B), (V, col, row, row + 1, T),
           (V, col + 1, row, row + 1, B)]

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for d in dirs:
        point2, per2 = process(grid, row + d[0], col + d[1], seen, val)
        points += point2
        per += per2

    return points, per


def part1(grid):
    seen = set()
    total = 0
    for row in range(len(grid)):
        for col in range(len(grid)):
            pt = (row, col)
            if pt not in seen:
                points, lines = process(grid, row, col, seen, grid[row][col])
                d = defaultdict(lambda: [])
                for l in lines:
                    d[l[:4]].append(l[4])

                perimeter = len(list(filter(lambda x: len(x) == 1, d.values())))
                area = len(points)
                # print((grid[row][col], area, sorted(lines)))
                total += perimeter * area
    return total


def get_sides(sides, sofar):
    if len(sides) <= 1:
        return sofar + len(sides)

    s1 = sides[0]
    s2 = sides[1]
    if s1[0] == s2[0] and s1[1] == s2[1] and s1[3] == s2[2] and s1[4] == s2[4]:
        s3 = (s1[0], s1[1], s1[2], s2[3], s1[4])
        return get_sides([s3] + sides[2:], sofar)
    else:
        return get_sides(sides[1:], sofar+1)


def part2(grid):
    seen = set()
    total = 0
    for row in range(len(grid)):
        for col in range(len(grid)):
            pt = (row, col)
            if pt not in seen:
                points, lines = process(grid, row, col, seen, grid[row][col])
                d = defaultdict(lambda: [])
                for l in lines:
                    d[l[:4]].append(tuple(l))

                s = {v[0] for v in d.values() if len(v) == 1}

                sides = get_sides(sorted(s), 0)

                area = len(points)
                total += sides * area
    return total


input_data = parse_file("q12.txt")
print(part1(input_data))
print(part2(input_data))

# 824242 - too low