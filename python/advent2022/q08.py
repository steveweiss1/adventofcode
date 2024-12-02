def parse_file(filename):
    with open(filename, 'r') as file:
        return [[int(char) for char in line.strip()] for line in file]


def part1(rows):
    visibles = set()
    for r in range(1, len(rows) - 1):
        height = rows[r][0]
        for c in range(1, len(rows[0]) - 1):
            if rows[r][c] > height:
                height = rows[r][c]
                visibles.add((r, c))
            if rows[r][c] == 9:
                break
        height = rows[r][-1]
        for c in range(len(rows[0]) - 2, 0, -1):
            if rows[r][c] > height:
                height = rows[r][c]
                visibles.add((r, c))
            if rows[r][c] == 9:
                break
    for c in range(1, len(rows[0]) - 1):
        height = rows[0][c]
        for r in range(1, len(rows) - 1):
            if rows[r][c] > height:
                height = rows[r][c]
                visibles.add((r, c))
            if rows[r][c] == 9:
                break
        height = rows[-1][c]
        for r in range(len(rows) - 2, 0, -1):
            if rows[r][c] > height:
                height = rows[r][c]
                visibles.add((r, c))
            if rows[r][c] == 9:
                break
    return len(visibles) + 2 * len(rows) + 2 * len(rows[0]) - 4


def part2(rows):
    bsf = 0
    for row in range(0, len(rows)):
        for col in range(0, len(rows[0])):
            total1 = 0
            for i in (range(row + 1, len(rows))):
                total1 += 1
                if rows[i][col] >= rows[row][col]:
                    break
            total2 = 0
            for i in (range(row - 1, -1, -1)):
                total2 += 1
                if rows[i][col] >= rows[row][col]:
                    break
            total3 = 0
            for i in (range(col - 1, -1, -1)):
                total3 += 1
                if rows[row][i] >= rows[row][col]:
                    break
            total4 = 0
            for i in (range(col + 1, len(rows[0]))):
                total4 += 1
                if rows[row][i] >= rows[row][col]:
                    break
            bsf = max(bsf, total1 * total2 * total3 * total4)
    return bsf


# Example usage
filename = "../../input/2022/q08.txt"
parsed_list = parse_file(filename)
# print(parsed_list)
print(part1(parsed_list))
print(part2(parsed_list))
