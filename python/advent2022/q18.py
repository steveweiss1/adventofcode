def parse_file(filename):
    with open(filename, 'r') as file:
        lines = [line.split(',') for line in file]
        return [(int(line[0]), int(line[1]), int(line[2])) for line in lines]


X = 0
Y = 1
Z = 2


def part1(cubes):
    s = process_sides(cubes)
    return len(s)




def process_sides(cubes):
    sides = []
    for x, y, z in cubes:
        sides.append(((x, y, z), Z))
        sides.append(((x, y, z + 1), Z))
        sides.append(((x, y, z), Y))
        sides.append(((x, y + 1, z), Y))
        sides.append(((x, y, z), X))
        sides.append(((x + 1, y, z), X))
    s = set()
    for side in sides:
        if side in s:
            s.remove(side)
        else:
            s.add(side)
    return s


filename = "q18-dev.txt"
parsed_list = parse_file(filename)

print(part1(parsed_list))
