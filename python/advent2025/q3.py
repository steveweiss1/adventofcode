def process_bank(bank):
    max1, max2 = '0', '0'
    for i, val in enumerate(bank):
        if val > max1 and i < len(bank) - 1:
            max1 = val
            max2 = '0'
        elif val > max2:
            max2 = val
    return int(max1 + max2)


cache = {}


def process_bank_recurse(bank, n=12):
    if n == 0:
        return ''
    key = (bank, n)
    if key in cache:
        return cache[key]
    max_val = '0'
    bsf = 0
    for i, val in enumerate(bank):
        if val > max_val and i < len(bank) - n + 1:
            max_val = val
            rest = str(process_bank_recurse(bank[i + 1:], n - 1))
            total = int(max_val + rest)
            bsf = max(bsf, total)
    cache[key] = bsf
    return bsf

def process_bank_itr(bank, n=12):
    total = ''
    for i in range(n - 1, -1, -1):
        end = len(bank) - i
        max_idx, max_val = max(enumerate(bank[:end]), key=lambda x: x[1])
        # print(f"{i} {end} {max_idx} {max_val}")
        # print(bank)
        total += max_val
        bank = bank[max_idx+1:]
    return int(total)



def part1(banks):
    return sum(map(process_bank, banks))


def part2(banks):
    return sum(map(process_bank_itr, banks))


def parse(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


input_data = parse("q3.txt")
# print(input_data)
print(part1(input_data))
print(part2(input_data))

