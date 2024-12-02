import ast
from functools import cmp_to_key


def parse_nested_list(s: str):
    return ast.literal_eval(s)


def parse_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


def is_valid(item1, item2):
    if item1 is None:
        return True
    if item2 is None:
        return False

    if isinstance(item1, int) and isinstance(item2, int):
        if item1 == item2:
            return None
        else:
            return item1 < item2

    if isinstance(item1, int) and isinstance(item2, list):
        return is_valid([item1], item2)

    if isinstance(item1, list) and isinstance(item2, int):
        return is_valid(item1, [item2])

    if isinstance(item1, list) and isinstance(item2, list):
        for i in range(len(item1)):
            if i >= len(item2):
                return False
            v = is_valid(item1[i], item2[i])
            if v is not None:
                return v
        if len(item2) > len(item1):
            return True
        return None

    print(f"oops {item1} {item2}")
    return None


def part1(rows):
    total = 0
    for rownum in range(0, len(rows), 3):
        list1 = parse_nested_list(rows[rownum])
        list2 = parse_nested_list(rows[rownum + 1])
        if is_valid(list1, list2):
            print(rownum // 3 + 1)
            total += (rownum // 3) + 1
    return total


def list_comparator(list1, list2):
    v = is_valid(list1[0], list2[0])
    return -1 if v is True else 1 if v is False else 0

def part2(rows):
    key_func = cmp_to_key(list_comparator)
    rows = ['[[2]]', '[[6]]'] + [r for r in rows if r.strip()]
    lists = zip([parse_nested_list(r) for r in rows], [1, 1] + [0] * (len(rows) - 2))
    sorted_lists = sorted(lists, key=key_func)
    vals = [s[1] for s in sorted_lists]
    i1 = vals.index(1) + 1
    i2 = vals.index(1, i1+1) + 1
    print(f"{i1} {i2}")
    return i1*i2


filename = "q13.txt"
parsed_list = parse_file(filename)
# print(part1(parsed_list))
print(part2(parsed_list))
