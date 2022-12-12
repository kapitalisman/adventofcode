from collections import deque
import copy
import math
import re

from aocd import data, submit
lines = data.splitlines()

# prepare grid
grid = [[ord(x) for x in line] for line in lines]

for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == ord('S'):
            sr, sc = r, c
            grid[r][c] = ord('a')
        if cell == ord('E'):
            er, ec = r, c
            grid[r][c] = ord('z')


def bsf(p1):
    visited = {(sr, sc)} if p1 else {(er, ec)}
    queue = deque()
    queue.append((next(iter(visited)), 0))
    while queue:
        (r, c), d = queue.popleft()
        for x, y in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            # check if outside the grid
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[r]):
                continue
            # check if already visited
            if (x, y) in visited:
                continue
            # check if elevation is too high
            if grid[x][y] - grid[r][c] > 1 if p1 else grid[x][y] - grid[r][c] < -1:
                continue
            # check if target has been reached
            done = x == er and y == ec if p1 else grid[x][y] == ord('a')
            if done:
                return d + 1
            # update queue
            queue.append(((x, y), d + 1))
            visited.add((x, y))


print(bsf(True))  # part 1
print(bsf(None))  # part 2
