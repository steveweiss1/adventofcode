from collections import defaultdict

def parse_file(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                parsed_data.append(line.split())

    return parsed_data

def part2(pairs):
    pairs2 = [p[1] for p in pairs]
    p2count = defaultdict(lambda: 0)
    for p in pairs2:
        p2count[p] += 1
    total = 0
    for p, _ in pairs:
        total += int(p) * p2count[p]
    return total


input_data = parse_file("q1.txt")
print(part2(input_data))