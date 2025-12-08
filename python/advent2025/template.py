from collections import defaultdict, namedtuple
# from lib.lib import
import lib.parser


# def part1(lists):

# def part2(lists):

def parse_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


input_data = parse_file("q1.txt")
print(input_data)
# print(part1(input_data))
# print(part2(input_data))
