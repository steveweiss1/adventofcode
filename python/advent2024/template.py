from collections import defaultdict


def parse_file(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                parsed_data.append([int(x) for x in (line.split())])

    return parsed_data


#def part1(lists):

#def part2(lists):


input_data = parse_file("q2.txt")
print(input_data)
#print(part1(input_data))
#print(part2(input_data))
