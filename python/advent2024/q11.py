from collections import defaultdict


def parse_file(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                return [int(x) for x in (line.split())]

    return parsed_data


def transform(v):
    if v == 0:
        return [1]
    str_v = str(v)
    if len(str_v) % 2 == 0:
        mid = int(len(str_v) / 2)
        v1 = int(str_v[:mid])
        v2 = int(str_v[mid:])
        return [v1, v2]

    return [v * 2024]


def part1(vals):
    val_list = vals
    for i in range(10):
        print(i)
        val_list_2 = []
        for v in val_list:
            val_list_2 += transform(v)
        val_list = val_list_2
        #print(val_list)
    return len(val_list)


def part2(vals):
    cache = defaultdict(int)
    for v in vals:
        cache[v] += 1

    for _ in range(75):
        new_cache = defaultdict(int)
        for k, v in cache.items():
            new_keys = transform(k)
            for key in new_keys:
                new_cache[key] += v
        cache = new_cache

    return sum(cache.values())


# def part2(lists):
#    return sum([is_gradual_for_any(l) for l in lists])


input_data = parse_file("q11.txt")
print(input_data)
print(part1(input_data))
print(part2(input_data))
