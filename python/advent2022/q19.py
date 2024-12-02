import re
from collections import defaultdict


# Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.

class Blueprint:
    def __init__(self, id, ore_cost, clay_cost, obs_ore_cost, obs_clay_cost, geode_ore_cost, geode_obs_cost):
        self.id = id
        self.ore_cost = ore_cost
        self.clay_ore_cost = clay_cost
        self.obs_ore_cost = obs_ore_cost
        self.obs_clay_cost = obs_clay_cost
        self.geode_ore_cost = geode_ore_cost
        self.geode_obs_cost = geode_obs_cost

    def __repr__(self):
        return f"Blueprint({self.id}, {self.ore_cost}, {self.clay_ore_cost}, {self.obs_ore_cost}, {self.obs_clay_cost}, {self.geode_ore_cost}, {self.geode_obs_cost})"


def parse_file(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                # Use a regular expression to find all occurrences of coordinates
                matches = re.findall(r'(-?\d+)', line)

                # Convert the found coordinate strings to tuples of integers
                blueprint = Blueprint(int(matches[0]), int(matches[1]), int(matches[2]), int(matches[3]),
                                      int(matches[4]), int(matches[5]), int(matches[6]))
                parsed_data.append(blueprint)

    return parsed_data


cache = {}
bsf = defaultdict(lambda: 0)


def dfs(blueprint, maxSteps, step, ore_robots, clay_robots, obs_robots, geode_robots, ore, clay, obs, geodes):
    if step == maxSteps:
        return geodes

    # if bsf[step] > geodes + 1:
    #     return bsf[step]
    #
    # bsf[step] = max(bsf[step], geodes)

    key = (step, ore_robots, clay_robots, obs_robots, geode_robots, ore, clay, obs, geodes)
    if key in cache:
        return cache.get(key)

    max_geodes = 0

    # build geode
    if obs >= blueprint.geode_obs_cost and ore >= blueprint.geode_ore_cost:
        max_geodes = dfs(blueprint, maxSteps, step + 1, ore_robots, clay_robots, obs_robots, geode_robots + 1,
                         ore + ore_robots - blueprint.geode_ore_cost,
                         clay + clay_robots, obs + obs_robots - blueprint.geode_obs_cost, geodes + geode_robots)
    # build obs
    else:
        if clay >= blueprint.obs_clay_cost and ore >= blueprint.obs_ore_cost:
            max_geodes = max(max_geodes,
                             dfs(blueprint, maxSteps, step + 1, ore_robots, clay_robots, obs_robots + 1, geode_robots,
                                 ore + ore_robots - blueprint.obs_ore_cost,
                                 clay + clay_robots - blueprint.obs_clay_cost, obs + obs_robots,
                                 geodes + geode_robots))
        # clay
        if ore >= blueprint.clay_ore_cost:  # and clay < blueprint.obs_clay_cost:
            max_geodes = max(max_geodes,
                             dfs(blueprint, maxSteps, step + 1, ore_robots, clay_robots + 1, obs_robots, geode_robots,
                                 ore + ore_robots - blueprint.clay_ore_cost,
                                 clay + clay_robots, obs + obs_robots,
                                 geodes + geode_robots))
        # ore
        if ore >= blueprint.ore_cost:
            max_geodes = max(max_geodes,
                             dfs(blueprint, maxSteps, step + 1, ore_robots + 1, clay_robots, obs_robots, geode_robots,
                                 ore + ore_robots - blueprint.ore_cost,
                                 clay + clay_robots, obs + obs_robots,
                                 geodes + geode_robots))

        max_geodes = max(max_geodes,
                         dfs(blueprint, maxSteps, step + 1, ore_robots, clay_robots, obs_robots, geode_robots,
                             ore + ore_robots,
                             clay + clay_robots, obs + obs_robots,
                             geodes + geode_robots))

    # print(f'{blueprint.id} {max_geodes}')
    cache[key] = max_geodes
    return max_geodes


def part1(parsed_list):
    total = 0
    # parsed_list = [parsed_list[0]]
    for blueprint in parsed_list:
        cache.clear()
        score = dfs(blueprint, 25, 1, 1, 0, 0, 0, 0, 0, 0, 0)
        print(f'{blueprint.id} {score}')
        total += score * blueprint.id
    return total


def part2(parsed_list):
    total = 1
    parsed_list = parsed_list[:3]
    for blueprint in parsed_list:
        cache.clear()
        bsf.clear()
        score = dfs(blueprint, 33, 1, 1, 0, 0, 0, 0, 0, 0, 0)
        print(f'{blueprint.id} {score}')
        total *= score
    return total


filename = "q19.txt"
parsed_list = parse_file(filename)

print(part2(parsed_list))
