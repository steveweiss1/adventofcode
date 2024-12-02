import re


class Range:
    def __init__(self, start, end):
        self.start = int(start)
        self.end = int(end)

    def __repr__(self):
        return f"Range(start={self.start}, end={self.end})"


def parse_file(filename):
    parsed_data = []

    pattern = r'(\d+)-(\d+),(\d+)-(\d+)'
    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            match = re.match(pattern, line)
            if match:
                # Split the line by spaces
                start1, end1, start2, end2 = match.groups()

                # Create Range objects and append to the list
                range1 = Range(start1, end1)
                range2 = Range(start2, end2)
                parsed_data.append((range1, range2))

    return parsed_data


def range_consumes(rangepair):
    r1, r2 = rangepair
    # Check if r1 consumes r2 or r2 consumes r1
    return (r1.start <= r2.start and r1.end >= r2.end) or (r2.start <= r1.start and r2.end >= r1.end)

def ranges_intersect(rangepair):
    r1, r2 = rangepair
    # Check if the ranges intersect
    return r1.start <= r2.end and r2.start <= r1.end


def part1(ranges):
    p = list(filter(range_consumes, ranges))
    return len(p)

def part2(ranges):
    p = list(filter(ranges_intersect, ranges))
    return len(p)

# Example usage
filename = "q04.txt"
parsed_list = parse_file(filename)
print(parsed_list)
print(part1(parsed_list))
print(part2(parsed_list))
