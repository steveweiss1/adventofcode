import matplotlib.pyplot as plt
import numpy as np

adjacents = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

# 1. Setup the figure ONCE
plt.ion() # Turn on interactive mode
fig, ax = plt.subplots()
scat = ax.scatter([], []) # Initialize empty scatter plot

# Set fixed limits so axes don't jump around
ax.set_xlim(0, 300)
ax.set_ylim(0, 300)

def part1(grid):
    paper_spots = grid_to_set(grid)
    total = 0
    for r,c in paper_spots:
        if sum((a+r, b+c) in paper_spots for a, b in adjacents) < 4:
            total += 1
    return total


def grid_to_set(grid):
    paper_spots = set()
    for r, row in enumerate(grid):
        for c, val in enumerate(grid[r]):
            if val == '@':
                paper_spots.add((r, c))
    return paper_spots


def part2(grid):
    paper_spots = grid_to_set(grid)
    total = 0
    to_delete = None
    while to_delete is None or len(to_delete) > 0:
        scat.set_offsets(list(paper_spots))
        fig.canvas.draw_idle()
        plt.pause(0.1) # Pause for 0.1 seconds to allow the plot to render
        to_delete = set()
        for r,c in paper_spots:
            if sum((a+r, b+c) in paper_spots for a, b in adjacents) < 4:
                to_delete.add((r,c))
        total += len(to_delete)
        paper_spots -= to_delete
    return total

def parse_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


input_data = parse_file("q4.txt")
#print(input_data)
#print(part1(input_data))
print(part2(input_data))
plt.ioff()
plt.show()