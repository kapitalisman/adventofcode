import math
from aocd import data, numbers, submit
lines = data.splitlines()

grid = [[int(x) for x in line] for line in lines]
x, y = len(grid), len(grid[0])

coords = set()

for i in range(x):
    for j in range(y):
        # edge
        if i in [0, x - 1] or j in [0, y - 1]:
            coords.add((i, j))
        # center
        tree = grid[i][j]
        # assume visible
        visible = [True, True, True, True]
        # check each direction
        for k in range(0, i):
            if grid[k][j] >= tree:
                visible[0] = False
                break
        for k in range(i + 1, x):
            if grid[k][j] >= tree:
                visible[1] = False
                break
        for k in range(0, j):
            if grid[i][k] >= tree:
                visible[2] = False
                break
        for k in range(j + 1, y):
            if grid[i][k] >= tree:
                visible[3] = False
                break
        # conclude
        if True in visible:
            coords.add((i, j))

p1 = print(len(coords))

scores = set()

for i in range(x):
    for j in range(y):
        # edge
        if i in [0, x - 1] or j in [0, y - 1]:
            continue
        # center
        tree = grid[i][j]
        # scenic score
        ss = [0, 0, 0, 0]
        # check each direction
        for k in range(1, i + 1):
            ss[0] += 1
            if grid[i - k][j] >= tree:
                break
        for k in range(i + 1, x):
            ss[1] += 1
            if grid[k][j] >= tree:
                break
        for k in range(1, j + 1):
            ss[2] += 1
            if grid[i][j - k] >= tree:
                break
        for k in range(j + 1, y):
            ss[3] += 1
            if grid[i][k] >= tree:
                break
        # conclude
        scores.add(math.prod(ss))

p2 = print(max(scores))
