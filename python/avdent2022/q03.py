from avdent2022.lib import list_to_tuples


def parse_file(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                parsed_data.append(line)

    return parsed_data


def val(c):
    if 'A' <= c[0] <= 'Z':
        return (ord(c[0]) - ord('A')) + 27
    else:
        return ord(c[0]) - ord('a') + 1

def process_row1(row):
    def split_string(s):
        # Calculate the middle index
        mid = len(s) // 2

        # Return the first half and second half
        return s[:mid], s[mid:]

    first, second = split_string(row)
    common = list(set(first).intersection(set(second)))
    vals = map(val, common)
    return max(vals)

def process_tuple2(trio):
    common = list(set(trio[0]).intersection(set(trio[1])).intersection(set(trio[2])))
    if len(common) > 1:
        print(f"oops {trio} {common}")
    return val(common[0])

def part1(rows):
    p = list(map(process_row1, rows))
    return sum(p)

def part2(rows):
    tuples = list_to_tuples(rows)
    p = list(map(process_tuple2, tuples))
    return sum(p)

# Example usage
filename = "q03.txt"
parsed_list = parse_file(filename)
print(parsed_list)
print(part1(parsed_list))
print(part2(parsed_list))
