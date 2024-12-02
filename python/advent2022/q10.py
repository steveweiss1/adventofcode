def parse_file(filename):
    with open(filename, 'r') as file:
        return [line.strip().split() for line in file]


def part1(rows):
    special_cycles = {20, 60, 100, 140, 180, 220}

    total = 1
    total_special = 0
    cycle = 0
    for row in rows:
        cmd = row[0]
        cycle += 1
        if cycle in special_cycles:
            total_special += total * cycle
        if cmd == 'addx':
            cycle += 1
            if cycle in special_cycles:
                total_special += total * cycle
            total += int(row[1])
    return total_special


def part2(rows):
    special_cycles = {20, 60, 100, 140, 180, 220}
    grid = [['-'] * 40 for _ in range(6)]

    total = 1
    cycle = 0
    pos = 0
    for row in rows:
        cmd = row[0]
        r = cycle // 40
        c = cycle % 40
        if r == 6:
            return grid
        if c+1 in {pos, pos + 1, pos + 2}:
            # print(f"{r} {c}")
            grid[r][c] = '#'
        else:
            grid[r][c] = '.'
        cycle += 1

        if cmd == 'addx':
            r = cycle // 40
            c = cycle % 40
            if c+1 in {pos, pos + 1, pos + 2}:
                grid[r][c] = '#'
            else:
                grid[r][c] = '.'
            total += int(row[1])
            pos = total
            cycle += 1

    return grid


# Example usage
filename = "../../input/2022/q10.txt"
parsed_list = parse_file(filename)
print(part1(parsed_list))
for myrow in part2(parsed_list):
    print(''.join(myrow))
