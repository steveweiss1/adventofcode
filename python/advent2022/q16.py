def parse_valve_info(s: str):
    # Split the string into parts
    parts = s.split(';')

    # Extract the current valve and flow rate from the first part
    first_part = parts[0].split()
    current_valve = first_part[1]  # 'AA'
    flow_rate = int(first_part[4].split('=')[1])  # 0

    # Extract the other valves from the second part
    second_part = parts[1].replace('tunnels lead to valves', '').replace('tunnel leads to valve', '').strip()
    other_valves = [valve.strip() for valve in second_part.split(',')]  # ['DD', 'II', 'BB']

    return current_valve, flow_rate, other_valves


def parse_file(filename):
    with open(filename, 'r') as file:
        l = [parse_valve_info(line.strip()) for line in file]
        return {t[0]: (t[1], set(t[2])) for t in l}


cache = {}


def bfs(valves, start, time, open_so_far, total_so_far):
    osf = sum([valves[o][0] for o in open_so_far])
    if time == 29:
        return osf + total_so_far
    if time > 29:
        return -1

    key = (start, time, total_so_far, " ".join(open_so_far))
    if key in cache:
        return cache[key]

    rate, paths = valves[start]
    max_open = 0
    if start not in open_so_far and rate > 0:
        open_so_far.add(start)
        osf2 = sum([valves[o][0] for o in open_so_far])
        max_open = max([dfs(valves, p, time + 2, open_so_far, total_so_far + osf + osf2) for p in paths])
        open_so_far.remove(start)
    max_no_open = max([dfs(valves, p, time + 1, open_so_far, total_so_far + osf) for p in paths])
    return max(max_open, max_no_open)

cache = {}


def dfs1(valves, start, time, open_so_far, total_so_far):
    if time == 30:
        return total_so_far

    key = (start, time, total_so_far, " ".join(open_so_far))
    if key in cache:
        return cache[key]

    all_to_open = [key for key, value in valves.items() if value[0] > 0]
    osf = sum([valves[o][0] for o in open_so_far])
    if len(all_to_open) == len(open_so_far):
        return total_so_far + osf * (30 - time)

    rate, paths = valves[start]

    if start not in open_so_far and rate > 0:
        open_so_far.add(start)
        max_open = dfs1(valves, start, time + 1, open_so_far, total_so_far + osf)
        open_so_far.remove(start)
        cache[key] = max_open
        return max_open
    else:
        m = max([dfs1(valves, p, time + 1, open_so_far, total_so_far + osf) for p in paths])
        cache[key] = m
        return m


def dfs1(valves, start, estart, time, open_so_far, total_so_far):
    if time == 26:
        return total_so_far

    key = (start, estart, time, total_so_far, " ".join(open_so_far))
    if key in cache:
        return cache[key]

    all_to_open = [key for key, value in valves.items() if value[0] > 0]
    osf = sum([valves[o][0] for o in open_so_far])
    if len(all_to_open) == len(open_so_far):
        return total_so_far + osf * (26 - time)

    rate, paths = valves[start]
    erate, epaths = values[estart]

    if start not in open_so_far and rate > 0:
        open_so_far.add(start)
        max_open = max([dfs1(valves, start, p, time + 1, open_so_far, total_so_far + osf) for p in paths])
        open_so_far.remove(start)
        cache[key] = max_open
        return max_open
    else:
        m = max([dfs1(valves, p, time + 1, open_so_far, total_so_far + osf) for p in paths])
        cache[key] = m
        return m

def part1(valves):
    open_so_far = set()
    time = 0
    start = 'AA'
    return dfs1(valves, start, start, time, open_so_far, 0)


# Example usage
filename = "q16-dev.txt"
parsed_map = parse_file(filename)
print(parsed_map)
print(part1(parsed_map))
