from collections import defaultdict


def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            # Handle non-unique values by appending to a list
            if isinstance(inverted[value], list):
                inverted[value].append(key)
            else:
                inverted[value] = [inverted[value], key]
        else:
            inverted[value] = key
    return inverted


def list_to_tuples(lst, size=3):
    # Create tuples of the specified size using zip and iter
    it = iter(lst)
    return list(zip(*[it] * size))


def zip_pairs(lst):
    return list(zip(lst[:-1], lst[1:]))


def find_all_occurrences(text, pattern):
    indexes = []
    start = 0
    while start < len(text):
        index = text.find(pattern, start)
        if index == -1:
            break  # No more occurrences found
        indexes.append(index)
        start = index + len(pattern)  # Move past the current match
    return indexes


def grid_to_default_dict(grid, default):
    sg = defaultdict(lambda: default)

    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            sg[(row, col)] = grid[row][col]

    return sg


def flatten(l):
    return sum(l, [])
