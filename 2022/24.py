import re
import math
import itertools
from collections import deque

from aocd import data, submit, numbers

# data = '''#.######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#'''

lines = data.splitlines()


def plot(valley):
    walls, blizzards = valley

    width = max([int(wall.real) for wall in walls])
    height = max([int(wall.imag) for wall in walls])
    for y in range(height + 1):
        line = []
        for x in range(width + 1):
            if (x + y * 1j) in walls:
                line.append('#')
            elif (x + y * 1j) in {b for b, d in blizzards}:
                line.append('x')
            else:
                line.append('.')
        print(''.join(line))


walls = set()
ground = set()
blizzards = set()

for r, line in enumerate(lines):
    for c, item in enumerate(line):
        match item:
            case '#':
                walls.add(c + r * 1j)
            case '.':
                ground.add(c + r * 1j)
            case '>':
                blizzards.add((c + r * 1j, 1))
            case '<':
                blizzards.add((c + r * 1j, -1))
            case 'v':
                blizzards.add((c + r * 1j, 1j))
            case '^':
                blizzards.add((c + r * 1j, -1j))

width = max([int(wall.real) for wall in walls])
height = max([int(wall.imag) for wall in walls])

lcm = math.lcm(width - 1, height - 1)

blizzards_time = {0: blizzards}
for t in range(1, lcm):
    # all blizzards move
    blizzards_ = set()
    for b, d in blizzards:
        b += d
        if b.real == 0:
            b = width - 1 + b.imag * 1j
        elif b.real == width:
            b = 1 + b.imag * 1j
        elif b.imag == 0:
            b = b.real + (height - 1) * 1j
        elif b.imag == height:
            b = b.real + 1j
        blizzards_.add((b, d))
    blizzards = blizzards_
    blizzards_time[t] = blizzards


# start position
s = 1

# end position
e = (width - 1) + height * 1j

# directions
D = [1, -1, 1j, -1j]


def bfs_forth(T):
    global blizzards_time
    visited = [(s, T)]
    q = deque([(s, T)])
    while q:
        z, t = q.popleft()

        t += 1
        # can wait?
        if z.imag >= 0 and z not in {b for b, d in blizzards_time[t % lcm]}:
            q.append((z, t))
            visited.append((z, t % lcm))
        # can move?
        for d in D:
            z_ = z + d
            if z_ in walls or z_.imag < 0:
                continue
            if z_.imag == height:
                return t
            if (z_, t % lcm) in visited:
                continue
            if z_ in {b for b, d in blizzards_time[t % lcm]}:
                continue
            q.append((z_, t))
            visited.append((z_, t % lcm))


def bfs_back(T):
    global blizzards_time
    visited = [(e, T)]
    q = deque([(e, T)])
    while q:
        z, t = q.popleft()

        t += 1
        # can wait?
        if z.imag <= height and z not in {b for b, d in blizzards_time[t % lcm]}:
            q.append((z, t))
            visited.append((z, t % lcm))
        # can move?
        for d in D:
            z_ = z + d
            if z_ in walls or z_.imag > height:
                continue
            if z_.imag == 0:
                return t
            if (z_, t % lcm) in visited:
                continue
            if z_ in {b for b, d in blizzards_time[t % lcm]}:
                continue
            q.append((z_, t))
            visited.append((z_, t % lcm))


print(p1 := bfs_forth(0))
print(p2 := bfs_forth(bfs_back(p1)))
