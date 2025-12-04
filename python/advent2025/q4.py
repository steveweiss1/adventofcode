adjacents = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

def part1(grid):
    paper_spots = grid_to_set(grid)
    total = 0
    for r,c in paper_spots:
        if sum((a+r, b+c) in paper_spots for a, b in adjacents) < 4:
            total += 1
    return total


def grid_to_set(grid):
    paper_spots = set()
    for r, row in enumerate(grid):
        for c, val in enumerate(grid[r]):
            if val == '@':
                paper_spots.add((r, c))
    return paper_spots


def part2(grid):
    paper_spots = grid_to_set(grid)
    total = 0
    deleted = True
    while deleted:
        deleted = False
        to_delete = set()
        for r,c in paper_spots:
            if sum((a+r, b+c) in paper_spots for a, b in adjacents) < 4:
                total += 1
                deleted = True
                to_delete.add((r,c))
        for spot in to_delete:
            paper_spots.remove(spot)
    return total

def parse_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


input_data = parse_file("q4.txt")
#print(input_data)
print(part1(input_data))
print(part2(input_data))
