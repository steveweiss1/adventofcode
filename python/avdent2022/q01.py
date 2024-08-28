class Elf:
    def __init__(self, c_list):
        self.c_list = c_list
        self.total = sum(c_list)

    def __repr__(self):
        return f"Elf(c_list='{self.c_list}',total={self.total})"


def parse_file(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        elf = []
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                elf.append(int(line))
            else:
                parsed_data.append(Elf(elf))
                elf = []
    if elf:  # Check if there is any remaining elf data to be added
        parsed_data.append(Elf(elf))

    return parsed_data


# Example usage
filename = "q01.txt"
parsed_list = parse_file(filename)


def part1(parsed_list):
    return max(parsed_list, key=lambda x: x.total).total


def part2(parsed_list):
    sorted_list = sorted(parsed_list, key=lambda x: x.total, reverse=True)[:3]
    return sum(entry.total for entry in sorted_list)


# print(parsed_list)
print(part1(parsed_list))
print(part2(parsed_list))
