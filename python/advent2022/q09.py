import math
from typing import Tuple, List


def parse_file(filename) -> List[Tuple[str, int]]:
    with open(filename, 'r') as file:
        return [(p[0], int(p[1])) for p in [line.strip().split() for line in file]]


def part1(rows: List[Tuple[str, int]]):
    seen = {(0, 0)}
    h = (0, 0)
    t = (0, 0)
    move = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
    for direction, steps in rows:
        for _ in range(steps):
            dh, dt = move[direction]
            h = (h[0] + dh, h[1] + dt)
            _r = h[0] - t[0]
            _c = h[1] - t[1]
            diag = abs(_r) > 0 and abs(_c) > 0
            if abs(_r) > 1 or abs(_c) > 1:
                t0 = t[0]
                if abs(_r) > 1 or diag:
                    t0 += 1 if _r > 0 else -1
                t1 = t[1]
                if abs(_c) > 1 or diag:
                    t1 += 1 if _c > 0 else -1
                t = (t0, t1)
                seen.add(t)
    return len(seen)

def part2(rows: List[Tuple[str, int]]):
    seen = [{(0, 0)} for _ in range(10)]
    rope = [(0, 0) for _ in range(10)]
    move = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
    for row in rows:
        for _ in range(row[1]):
            d = move[row[0]]
            h = (rope[0][0] + d[0], rope[0][1] + d[1])
            rope[0] = h
            for i in range(1, len(seen)):
                prev = rope[i-1]
                cur = rope[i]
                _r = prev[0] - cur[0]
                _c = prev[1] - cur[1]
                diag = abs(_r) > 0 and abs(_c) > 0
                if abs(_r) > 1 or abs(_c) > 1:
                    t0 = cur[0]
                    if abs(_r) > 1 or diag:
                        t0 += 1 if _r > 0 else -1
                    t1 = cur[1]
                    if abs(_c) > 1 or diag:
                        t1 += 1 if _c > 0 else -1
                    t = (t0, t1)
                    seen[i].add(t)
                    rope[i] = t
    return len(seen[-1])

# Example usage
filename = "../../input/2022/q09.txt"
parsed_list = parse_file(filename)
# print(parsed_list)
print(part1(parsed_list))
print(part2(parsed_list))
