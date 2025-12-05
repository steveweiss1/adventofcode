def part1(ranges, vals):
    total = 0
    for val in vals:
        for start, end in ranges:
            if start <= val <= end:
                total += 1
                break
    return total

def part2(ranges):
    index = 0
    while index < len(ranges) - 1:
        r1 = ranges[index]
        r2 = ranges[index+1]
        if r1[1] >= r2[0]:
            new_range = (r1[0], max(r1[1], r2[1]))
            ranges[index] = new_range
            del ranges[index+1]
        else:
            index += 1
    return sum([end - start + 1 for start, end in ranges])

def parse_file(filename):
    ranges = []
    vals = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if '-' in line:
                ranges.append(tuple(map(int,line.split('-'))))
            elif line.isnumeric():
                vals.append(int(line))
    return sorted(ranges),vals


input_data = parse_file("q5.txt")
print(part1(*input_data))
print(part2(input_data[0]))
