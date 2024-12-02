from collections import defaultdict


def parse_file(filename):
    with open(filename, 'r') as file:
        out = []
        for line in file:
            allpairs = []
            pairs = line.split(' -> ')
            result = [tuple(map(int, pair.split(","))) for pair in pairs]
            out.append(result)
        return out


AIR = 0
WALL = 1
SAND = 2

parsed_list = parse_file("q14.txt")
print(parsed_list)

grid = defaultdict(lambda: AIR)
for walls in parsed_list:
    for start, end in (zip(walls, walls[1:])):
        dx, dy = start[0] - end[0], start[1] - end[1]
        if dx == 0:
            miny, maxy = min(start[1], end[1]), max(start[1], end[1])
            for i in range(miny, maxy + 1):
                grid[(start[0], i)] = WALL
        else:
            minx, maxx = min(start[0], end[0]), max(start[0], end[0])
            for i in range(minx, maxx + 1):
                grid[(i, start[1])] = WALL

print(grid)


def part1(grid):
    total = 0
    direction = ([0, 1], [-1, 1], [1, 1])
    maxy = max([g[1] for g in grid])

    while True:
        posx, posy = (500, 1)
        if grid[(posx, posy)] == SAND:
            return total
        while grid[(posx, posy)] == AIR:
            stuck = True
            for dx, dy in direction:
                if grid[(posx + dx, posy + dy)] == AIR and maxy >= posy + dy:
                    #print(f"{posx}, {posy}")
                    stuck = False
                    posx += dx
                    posy += dy
                    break
            if posy >= maxy:
                return total
            if stuck:
                print(f"stuck {posx}, {posy}")
                grid[(posx, posy)] = SAND
                total += 1
                break


def part2(grid):
    total = 0
    direction = ([0, 1], [-1, 1], [1, 1])
    maxy = max([g[1] for g in grid]) + 1

    while True:
        posx, posy = (500, 0)
        if grid[(posx, posy)] == SAND:
            return total
        while grid[(posx, posy)] == AIR:
            stuck = True
            if posy != maxy:
                for dx, dy in direction:
                    if grid[(posx + dx, posy + dy)] == AIR and maxy >= posy + dy:
                        #print(f"{posx}, {posy}")
                        stuck = False
                        posx += dx
                        posy += dy
                        break
            if stuck:
                print(f"stuck {posx}, {posy}")
                grid[(posx, posy)] = SAND
                total += 1
                break


print(part2(grid))
