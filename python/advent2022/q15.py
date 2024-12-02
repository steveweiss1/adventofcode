import re


def parse_file(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                # Use a regular expression to find all occurrences of coordinates
                matches = re.findall(r'x=(-?\d+), y=(-?\d+)', line)

                # Convert the found coordinate strings to tuples of integers
                coords = [(int(x), int(y)) for x, y in matches]
                parsed_data.append(coords)

    return parsed_data


def part1(rows, row_y):
    x_vals = set()
    beacon_x_vals = set()
    for sensor, beacon in rows:
        if beacon[1] == row_y:
            beacon_x_vals.add(beacon[0])
        dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        dist_to_row = abs(row_y - sensor[1])
        max_x = dist - dist_to_row + 1
        for i in range(max_x):
            x_vals.add(sensor[0] + i)
            x_vals.add(sensor[0] - i)
    for x in beacon_x_vals:
        x_vals.remove(x)
    # print(sorted(x_vals))
    return len(x_vals)

def find_in_row(rows, row_y, limit):
    x_vals = set()
    ranges = []
    for sensor, beacon in rows:
        dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        dist_to_row = abs(row_y - sensor[1])
        max_x = dist - dist_to_row
        if max_x > 0:
            start = max(0, sensor[0] - max_x)
            end = min(limit, sensor[0] + max_x + 1)
            ranges.append((start, end))

    ranges.sort(key=lambda x: x[0])
    start = ranges[0][0]
    merged = ranges.pop(0)[1]
    if start != 0:
        print(f"start = {start}")
        return -1
    for r_start, r_end in ranges:
        if r_start > merged:
            print(f"start = {r_start} merged = {merged}")
            return 4000000 * merged + row_y
        merged = max(merged, r_end)
    return None


def part2(rows):
    limit = 4000001
    for i in range(2908370, limit):
        print(i)
        r = find_in_row(rows, i, limit)
        if r is not None:
            return r

# Example usage
filename = "q15.txt"
row = 2000000
parsed_list = parse_file(filename)
#print(parsed_list)
# print(part1(parsed_list, row))
print(part2(parsed_list))
