import re


def parse_file(filename):
    with open(filename, 'r') as file:
        lines = [line.rstrip('\n') for line in file]
        grid = lines[:-2]
        directions = lines[-1]
        max_width = max([len(line) for line in grid])
        grid = [line.ljust(max_width) for line in grid]

        # Use regex to find all matches of the pattern: one or more digits followed by a single letter (L or R)
        matches = re.findall(r'(\d+)([LRZ])', directions)
        # Convert matches into a list of tuples with integer and direction
        parsed_result = [(int(num), direction) for num, direction in matches]
        return (grid, parsed_result)


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def part1(grid, instructions):
    row = 0
    col = grid[0].find('.')

    direction = 0
    for moves, next_dir in instructions:
        for i in range(0, moves):
            nextrow = row + dirs[direction][0]
            nextcol = col + dirs[direction][1]
            if nextrow < 0 or nextcol < 0 or nextrow == len(grid) or nextcol == len(grid[nextrow]):
                nextpos = ' '
            else:
                nextpos = grid[nextrow][nextcol]
            if nextpos == '.':
                row += dirs[direction][0]
                col += dirs[direction][1]
            elif nextpos == '#':
                break
            elif nextpos == ' ':
                if direction == 0:  # right
                    j = 0
                    while grid[row][j] == ' ':
                        j += 1
                    if grid[row][j] == '.':
                        col = j
                    else:
                        break
                elif direction == 1:  # down
                    j = 0
                    while grid[j][col] == ' ':
                        j += 1
                    if grid[j][col] == '.':
                        row = j
                    else:
                        break
                elif direction == 2:  # left
                    j = len(grid[row]) - 1
                    while grid[row][j] == ' ':
                        j -= 1
                    if grid[row][j] == '.':
                        col = j
                    else:
                        break
                else:  # up
                    j = len(grid) - 1
                    while grid[j][col] == ' ':
                        j -= 1
                    if grid[j][col] == '.':
                        row = j
                    else:
                        break
            else:
                raise Exception("oops")
        if next_dir == 'R':
            direction = (direction + 1) % 4
        elif next_dir == 'L':
            direction = (direction - 1) % 4

    row += 1
    col += 1
    return 1000 * row + 4 * col + direction


filename = 'q22.txt'
input_grid = parse_file(filename)
print(part1(input_grid[0], input_grid[1]))
