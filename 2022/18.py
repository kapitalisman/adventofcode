from collections import deque

from aocd import data, submit, numbers
lines = data.splitlines()

cubes = set()
for line in lines:
    x, y, z = list(map(int, line.split(',')))
    cubes.add((x, y, z))

D = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

# part 1: loop over all cubes and check all sides
p1 = 0
for x, y, z in cubes:
    for u, v, w in D:
        if (x + u, y + v, z + w) not in cubes:
            p1 += 1

print(p1)

# lbound and rbound of cube which fully contains the lava droplet
a = min([min(x, y, z) for (x, y, z) in cubes]) - 1
b = max([max(x, y, z) for (x, y, z) in cubes]) + 1

# part 2: simulate the water surrounding the lava droplet
p2 = 0
visited = {(a, a, a)}
water = deque(visited)
while water:
    x, y, z = water.popleft()
    for r, s, t in [(x + u, y + v, z + w) for u, v, w in D]:
        if any(q < a or q > b for q in [r, s, t]):
            continue
        if (r, s, t) in visited:
            continue
        if (r, s, t) in cubes:
            p2 += 1
            continue
        water.append((r, s, t))
        visited.add((r, s, t))

print(p2)
