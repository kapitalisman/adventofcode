from collections import deque
import copy
import math
import re
import functools
import json

from aocd import data, submit
lines = data.splitlines()

rock = set()
for line in lines:
    nodes = line.split(' -> ')
    for pair in zip(nodes, nodes[1:]):
        x1, y1 = map(int, pair[0].split(','))
        x2, y2 = map(int, pair[1].split(','))

        xi = 1 if x2 > x1 else -1
        yi = 1 if y2 > y1 else -1

        for x in range(x1, x2 + xi, xi):
            for y in range(y1, y2 + yi, yi):
                rock.add(complex(x, y))

ymax = max([z.imag for z in rock])


def sim(p1):
    t = 0
    sand = copy.deepcopy(rock)
    while (u := complex(500, 0)) not in sand:
        while True:
            if u.imag == ymax + 1:
                if p1:
                    return t
                break
            if (v := complex(u.real, u.imag + 1)) not in sand:
                u = v
                continue
            if (v := complex(u.real - 1, u.imag + 1)) not in sand:
                u = v
                continue
            if (v := complex(u.real + 1, u.imag + 1)) not in sand:
                u = v
                continue
            break
        sand.add(u)
        t += 1
    return t


print(p1 := sim(True))  # part 1
print(p2 := sim(None))  # part 2
