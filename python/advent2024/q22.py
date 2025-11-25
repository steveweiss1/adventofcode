from collections import defaultdict


def parse_file(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]


PRUNER = 16777216


def gen_secret(start, n):
    secret = start
    results = [secret]
    for _ in range(n):
        a = secret * 64
        secret = (a ^ secret) % PRUNER
        secret = (int(secret / 32) ^ secret) % PRUNER
        secret = ((2048 * secret) ^ secret) % PRUNER
        results.append(secret)
    return results


def get_diffs(l):
    result = [(l[0] % 10, 12)]
    for i in range(1, len(l)):
        result.append((l[i] % 10, l[i] % 10 - l[i - 1] % 10))
    return result


def part1(nums):
    return sum([gen_secret(n, 2000)[-1] for n in nums])


def part2(nums):
    lists = [gen_secret(n, 2000) for n in nums]
    lists = [get_diffs(l) for l in lists]
    d = defaultdict(int)
    for l in lists:
        seen = set()
        for i in range(1, len(l) - 4):
            seq = (l[i][1], l[i+1][1], l[i+2][1], l[i+3][1])
            if seq in seen:
                continue
            seen.add(seq)
            d[seq] += l[i+3][0]
    return max(d.values())


input_data = parse_file("q22.txt")
print(input_data)

#print(part1(input_data))
print(part2(input_data))
