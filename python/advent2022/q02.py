from advent2022.lib import invert_dict


def parse_file(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                parsed_data.append(line.split())

    return parsed_data


def part1(rows):
    vals_right = {'X': 1, 'Y': 2, 'Z': 3}
    win = {'X': 'C', 'Y': 'A', 'Z': 'B'}
    draw = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    def process(row):
        win_val = 0
        if row[0] == win[row[1]]:
            win_val = 6
        elif row[0] == draw[row[1]]:
            win_val = 3

        z = win_val + vals_right[row[1]]

        return z

    return sum(process(row) for row in rows)


def part2(rows):
    vals_right = {'X': 1, 'Y': 2, 'Z': 3}
    win = invert_dict({'X': 'C', 'Y': 'A', 'Z': 'B'})
    draw = invert_dict({'X': 'A', 'Y': 'B', 'Z': 'C'})
    lose = invert_dict({'X': 'B', 'Y': 'C', 'Z': 'A'})
    def process(row):
        win_val = 0
        sign = 0
        if row[1] == 'X':  # lose
            sign = lose[row[0]]
        elif row[1] == 'Y':  # draw
            win_val = 3
            sign = draw[row[0]]
        else:
            win_val = 6
            sign = win[row[0]]
        z = win_val + vals_right[sign]

        return z

    return sum(process(row) for row in rows)

# Example usage
filename = "q02.txt"
parsed_list = parse_file(filename)
print(parsed_list)
print(part1(parsed_list))
print(part2(parsed_list))


