from collections import defaultdict


def parse_file(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            line = line.replace(":", "")
            if line:
                parsed_data.append([int(x) for x in (line.split())])

    return parsed_data


def calc(lst, concat):
    if len(lst) < 2:
        return lst
    the_sum = lst[0] + lst[1]
    prod = lst[0] * lst[1]
    ccat = int(str(lst[0]) + str(lst[1]))
    if len(lst) == 2:
        if concat:
            return [the_sum, prod, ccat]
        else:
            return [the_sum, prod]
    l1 = [the_sum] + lst[2:]
    l2 = [prod] + lst[2:]
    l3 = []
    if concat:
        l3 = [ccat] + lst[2:]
    return calc(l1, concat) + calc(l2, concat) + calc(l3, concat)


def is_valid(the_list, concat):
    total = the_list[0]
    vals = the_list[1:]
    sums = calc(vals, concat)
    if total in sums:
        return total


def part1(lists):
    total = 0
    for l in lists:
        if is_valid(l, False):
            total += l[0]
    return total


def part2(lists):
    total = 0
    for l in lists:
        if is_valid(l, True):
            total += l[0]
    return total


input_data = parse_file("q7-dev.txt")
# print(input_data)
print(part1(input_data))
print(part2(input_data))
