from collections import defaultdict


def parse_file(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            return line.strip()

    return parsed_data


def to_dict(input):
    d = dict()
    id = 0
    index = 0
    is_block = True
    for i in input:
        block_len = int(i)
        if is_block:
            for k in range(block_len):
                d[index] = id
                index += 1
            id += 1
        else:
            index += block_len
        is_block = not is_block
    return d

def part1(input):
    d = to_dict(input)
    end = max(d.keys())
    left_blank = 0
    while left_blank in d:
        left_blank += 1
    right = max(d.keys())
    while left_blank <= right:
        r = d[right]
        del d[right]
        d[left_blank] = r
        while left_blank in d:
            left_blank += 1
        while right not in d:
            right -= 1

    total = 0
    for i in range(end):
        if i in d:
            total += i * d[i]

    return total

def part2(input):
    d = to_dict(input)
    end = max(d.keys())

    right2 = max(d.keys())
    while d[right2] > 0:
        right = right2
        while right-1 in d and d[right-1] == d[right2]:
            right -= 1
        right_len = right2 - right + 1

        left_blank = 0
        found = False
        while left_blank < right:
            while left_blank in d:
                left_blank += 1
            if left_blank > right:
                break
            left_blank2 = left_blank + 1
            while left_blank2 not in d:
                left_blank2 += 1
            if left_blank2 - left_blank >= right_len:
                found = True
                break
            else:
                left_blank = left_blank2

        if found:
            val = d[right]
            for i in range(right_len):
                d[left_blank + i] = val
                del d[right + i]

        right2 = right - 1
        while right2 not in d:
            right2 -= 1

    total = 0
    for i in range(end):
        if i in d:
            total += i * d[i]

    return total




input_data = parse_file("q9.txt")



print(input_data)
#print(to_array(input_data))
print(part1(input_data))
print(part2(input_data))
