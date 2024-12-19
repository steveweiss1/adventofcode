from collections import defaultdict


def parse_file(filename):
    parsed_data = []
    directions = ''

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                if '#' in line:
                    parsed_data.append(list(line))
                elif '<' in line:
                    directions += line

    return (parsed_data, directions)


def print_grid(grid, pos):
    grid[pos[0]][pos[1]] = '@'
    for r in grid:
        print(''.join(r))
    grid[pos[0]][pos[1]] = '.'
    print('\n')


def part1(grid, directions):
    pos = ()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '@':
                pos = (r, c)
                grid[r][c] = '.'
                break
    #print_grid(grid, pos)

    for d in directions:
        dir = to_dir(d)

        can_move = False
        next_pos = (pos[0] + dir[0], pos[1] + dir[1])
        while grid[next_pos[0]][next_pos[1]] != '#':
            if grid[next_pos[0]][next_pos[1]] == '.':
                can_move = True
                break
            next_pos = (next_pos[0] + dir[0], next_pos[1] + dir[1])
        if can_move:
            # move robot
            next_pos = (pos[0] + dir[0], pos[1] + dir[1])
            g = grid[next_pos[0]][next_pos[1]]
            pos = next_pos
            grid[pos[0]][pos[1]] = '.'
            # move boxes
            while g == 'O':
                next_pos = (next_pos[0] + dir[0], next_pos[1] + dir[1])
                g = grid[next_pos[0]][next_pos[1]]
                grid[next_pos[0]][next_pos[1]] = 'O'
        #print(d)
        #print_grid(grid, pos)

    total = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'O':
                total += 100 * r + c

    return total


def transform(grid):
    grid2 = []
    for row in grid:
        row2 = []
        for c in row:
            out = []
            if c == '.':
                out = ('.', '.')
            elif c == 'O':
                out = ('[', ']')
            elif c == '#':
                out = ('#', '#')
            elif c == '@':
                out = ('@', '.')
            row2 += out
        grid2.append(row2)
    return grid2

def can_it_move(grid, pos, dir):
    c = grid[pos[0]][pos[1]]
    if c == '.':
        return True
    if c == '#':
        return False
    if c == '[':
        return can_it_move(grid, (pos[0] + dir, pos[1]), dir) and can_it_move(grid, (pos[0] + dir, pos[1] + 1), dir)
    else:
        return can_it_move(grid, (pos[0] + dir, pos[1]), dir) and can_it_move(grid, (pos[0] + dir, pos[1] - 1), dir)

def move_boxes(grid, pos, dir):
    if grid[pos[0]][pos[1]] == ']':
        move_boxes(grid, (pos[0], pos[1] - 1), dir)
        return

    if grid[pos[0]][pos[1]] != '[':
        raise Exception(pos)
    next_pos_l = (pos[0] + dir, pos[1])
    next_pos_r = (pos[0] + dir, pos[1] + 1)
    g_l = grid[next_pos_l[0]][next_pos_l[1]]
    if g_l == '[' or g_l == ']':
        move_boxes(grid, next_pos_l, dir)
    g_r = grid[next_pos_r[0]][next_pos_r[1]]
    if g_r == '[':
        move_boxes(grid, next_pos_r, dir)

    grid[next_pos_l[0]][next_pos_l[1]] = '['
    grid[next_pos_r[0]][next_pos_r[1]] = ']'
    grid[pos[0]][pos[1]] = '.'
    grid[pos[0]][pos[1]+1] = '.'


def part2(grid, directions):
    pos = ()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '@':
                pos = (r, c)
                grid[r][c] = '.'
                break
    #print_grid(grid, pos)

    for d in directions:
        dir = to_dir(d)

        can_move = False
        next_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if dir[1] == 0:
            can_move = can_it_move(grid, next_pos, dir[0])
        else:
            while grid[next_pos[0]][next_pos[1]] != '#':
                if grid[next_pos[0]][next_pos[1]] == '.':
                    can_move = True
                    break
                next_pos = (next_pos[0] + dir[0], next_pos[1] + dir[1])
        if can_move:
            # move robot
            next_pos = (pos[0] + dir[0], pos[1] + dir[1])
            g = grid[next_pos[0]][next_pos[1]]
            pos = next_pos
            # move boxes
            if g == '[' or g == ']':
                if dir[1] == 0:
                    move_boxes(grid, next_pos, dir[0])
                else:
                    grid[pos[0]][pos[1]] = '.'
                    while g == '[' or g == ']':
                        next_pos = (next_pos[0] + dir[0], next_pos[1] + dir[1])
                        next_g = grid[next_pos[0]][next_pos[1]]
                        grid[next_pos[0]][next_pos[1]] = g
                        g = next_g
        #print(d)
        #print_grid(grid, pos)

    total = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '[':
                total += 100 * r + c

    return total


def to_dir(d):
    dir = ()
    if d == '<':
        dir = (0, -1)
    elif d == '>':
        dir = (0, 1)
    elif d == '^':
        dir = (-1, 0)
    else:
        dir = (1, 0)
    return dir


filename = "q15.txt"
#input_data = parse_file(filename)
#print(input_data)
#print(part1(*input_data))
input_data = parse_file(filename)
grid2 = transform(input_data[0])
print(part2(grid2, input_data[1]))
