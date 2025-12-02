def process(pairs, part2=False):
    position = 50
    total_zero = 0
    last_was_zero = False
    for direction, clicks in pairs:
        if clicks >= 100:
            cycles = int(clicks / 100)
            if part2:
                total_zero += cycles
            clicks = clicks % 100
        if direction == 'L':
            position -= clicks
        else:
            position += clicks
        new_position = position % 100
        if new_position == 0:
            total_zero += 1
        elif part2 and new_position != position and not last_was_zero:
            total_zero += 1
        last_was_zero = (new_position == 0)
        position = new_position
    return total_zero


# L25
def parse_pairs(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            parsed_data.append(((line[0]), (int(line[1:]))))

    return parsed_data


input_data = parse_pairs("q1.txt")
# Part 1
print(process(input_data))

# Part 2
print(process(input_data, True))
