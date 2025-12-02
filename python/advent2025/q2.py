
def parse_ranges_one_line(filename):
    with open(filename, 'r') as file:
        line = file.readline().strip()
        ranges = line.split(',')
        return [tuple(map(int, r.split('-'))) for r in ranges]


def find_invalid_part_1(start, end):
    invalids = set()
    cur = start
    while cur <= end:
        cur_len = len(str(cur))
        if cur_len % 2 == 1:
            cur = pow(10, cur_len)
            cur_len += 1
        half = str(cur)[:int(cur_len / 2)]
        cur = int(half + half)
        if cur > end:
            break
        if cur >= start:
            invalids.add(cur)
        half = str(int(half) + 1)
        cur = int(half + half)
    # print(f"{start}-{end}: {invalids}")
    return invalids


def find_invalid_part_2(start, end):
    start_len = len(str(start))
    if start_len < len(str(end)):
        end1 = int('9' * start_len)
        start2 = int('1' + ('0' * start_len))
        return find_invalid_part_2(start, end1) | find_invalid_part_2(start2, end)

    invalids = set()
    max_prefix_length = int(len(str(end)) / 2) + 1
    for prefix_len in range(1, max_prefix_length):
        cur = start

        while cur <= end:
            cur_len = len(str(cur))
            prefix = str(cur)[:prefix_len]
            cur_str = prefix + prefix
            while len(cur_str) < len(str(start)):
                cur_str += prefix
            cur = int(cur_str)
            if cur > end:
                break
            if cur >= start:
                invalids.add(cur)
            prefix = str(int(prefix) + 1)

            cur_str = prefix + prefix
            while int(cur_str) < start:
                cur_str += prefix
            cur = int(cur_str)
        # print(f"{start}-{end}:({prefix_len}) {invalids}")
    return invalids


def part1(ranges):
    return sum([sum(find_invalid_part_1(s, e)) for s, e in ranges])

def part2(ranges):
    return sum([sum(find_invalid_part_2(s, e)) for s, e in ranges])

input_data = parse_ranges_one_line("q2.txt")
# print(input_data)
print(part1(input_data))
print(part2(input_data))
