import re
from collections import defaultdict


def parse_file(filename):
    with open(filename, 'r') as file:
        lines = [line.rstrip('\n') for line in file]
        elves = set()
        for row in range(0, len(lines)):
            for col in range(0, len(lines[0])):
                if lines[row][col] == '#':
                    elves.add((row, col))
        return elves


def part1(elves):
    dirs = [((-1, 0), (-1, -1), (-1, 1)),
            ((1, 0), (1, -1), (1, 1)),
            ((0, -1), (1, -1), (-1, -1)),
            ((0, 1), (-1, 1), (1, 1))]

    for _ in range(0, 10):
        next_move = defaultdict(lambda: [])
        next_round = set()
        for r, c in elves:
            alone = True
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i != 0 or j != 0) and (r + i, c + j) in elves:
                        alone = False
                        break
            if alone:
                next_round.add((r, c))
            else:
                can_move = False
                for d in dirs:
                    if ((r + d[0][0], c + d[0][1]) not in elves
                            and (r + d[1][0], c + d[1][1]) not in elves
                            and (r + d[2][0], c + d[2][1]) not in elves):
                        next_move[(r + d[0][0], c + d[0][1])].append((r, c))
                        can_move = True
                        break
                if not can_move:
                    next_round.add((r, c))

        if len(next_move) == 0:
            break

        for next_spot, prev_spots in next_move.items():
            if len(prev_spots) == 1:
                next_round.add(next_spot)
            else:
                next_round.update(prev_spots)
        elves = next_round
        f = dirs.pop(0)
        dirs.append(f)
        # print(sorted(elves))

    row_min = 10000
    row_max = 0
    col_min = 10000
    col_max = 0

    for r, c in elves:
        row_min = min(r, row_min)
        row_max = max(r, row_max)
        col_min = min(c, col_min)
        col_max = max(c, col_max)
    return (col_max - col_min + 1) * (row_max - row_min + 1) - len(elves)


def part2(elves):
    dirs = [((-1, 0), (-1, -1), (-1, 1)),
            ((1, 0), (1, -1), (1, 1)),
            ((0, -1), (1, -1), (-1, -1)),
            ((0, 1), (-1, 1), (1, 1))]

    moved = True
    round_num = 0

    while moved:
        round_num += 1
        next_move = defaultdict(lambda: [])
        next_round = set()
        for r, c in elves:
            alone = True
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i != 0 or j != 0) and (r + i, c + j) in elves:
                        alone = False
                        break
            if alone:
                next_round.add((r, c))
            else:
                can_move = False
                for d in dirs:
                    if ((r + d[0][0], c + d[0][1]) not in elves
                            and (r + d[1][0], c + d[1][1]) not in elves
                            and (r + d[2][0], c + d[2][1]) not in elves):
                        next_move[(r + d[0][0], c + d[0][1])].append((r, c))
                        can_move = True
                        break
                if not can_move:
                    next_round.add((r, c))

        if len(next_move) == 0:
            return round_num

        for next_spot, prev_spots in next_move.items():
            if len(prev_spots) == 1:
                next_round.add(next_spot)
            else:
                next_round.update(prev_spots)
        elves = next_round
        f = dirs.pop(0)
        dirs.append(f)
        # print(sorted(elves))

filename = 'q23.txt'
input_grid = parse_file(filename)
print(part1(input_grid.copy()))
print(part2(input_grid.copy()))
