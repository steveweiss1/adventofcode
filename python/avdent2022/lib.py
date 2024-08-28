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
