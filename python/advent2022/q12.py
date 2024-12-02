from collections import deque
from typing import List, Tuple, Optional


def parse_file(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]


def next_char(c):
    if c == 'S':
        return 'a'
    if c == 'z':
        return 'E'
    return chr(ord(c) + 1)


def part1(grid: List[List[str]]):
    rows, cols = len(grid), len(grid[0])

    start = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
                break
    return bfs(grid, start)

def part2(grid: List[List[str]]):
    rows, cols = len(grid), len(grid[0])

    starts = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'a':
                starts.append((r, c))

    return min([bfs(grid, start) for start in starts])


def bfs(grid: List[List[str]], start: (int, int)):
    rows, cols = len(grid), len(grid[0])

    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start, 0)])  # (position, distance)
    visited[start[0]][start[1]] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while queue:
        (r, c), dist = queue.popleft()

        cur = grid[r][c]

        if cur == 'E':
            return dist  # Return the length of the path

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and (grid[nr][nc] in {cur, next_char(cur)} or
                                                                              cur > grid[nr][nc] > 'Z'):
                visited[nr][nc] = True
                queue.append(((nr, nc), dist + 1))


    return 99999  # Return None if the target is not found


filename = "q12.txt"
parsed_list = parse_file(filename)
print(part2(parsed_list))
