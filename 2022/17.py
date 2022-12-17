from collections import deque
import copy
import math
import re
import functools
import itertools
import json

from aocd import data, submit, numbers


def clamp(n, smallest, largest): return max(smallest, min(n, largest))


def intersection_is_empty(a: set, b: set):
    return a.intersection(b) == set()


jet_pattern = list(data)
mod = len(jet_pattern)

A = ['####']
B = ['.#.', '###', '.#.']
C = ['###', '..#', '..#']
D = ['#', '#', '#', '#']
E = ['##', '##']

blocks = [A, B, C, D, E]

grid = set()
for i in range(7):
    grid.add((i, 0))  # floor

for i in range(10000):
    grid.add((-1, i))  # left wall
    grid.add((7, i))  # right wall

p = 0
for k in range(2022):
    # current height
    t = max([j[1] for j in grid if 0 <= j[0] <= 6])
    # new block
    block = blocks[k % 5]
    w = len(block[0])
    h = len(block)
    x1 = 2
    y1 = t + 4

    # jet push
    jet = jet_pattern[p % mod]
    p += 1
    shift = -1 if jet == '<' else 1
    x1 += shift

    while True:
        # can move down?
        temp = set()
        for x in range(w):
            for y in range(h):
                if block[y][x] == '#':
                    temp.add((x1 + x, y1 + y - 1))
        if intersection_is_empty(grid, temp):
            # can move
            y1 -= 1

            # jet push
            jet = jet_pattern[p % mod]
            p += 1
            shift = -1 if jet == '<' else 1
            temp = set()
            for x in range(w):
                for y in range(h):
                    if block[y][x] == '#':
                        temp.add((x1 + x + shift, y1 + y))
            if intersection_is_empty(grid, temp):
                # can shift
                x1 += shift
            else:
                continue  # moving down

        else:  # block has stopped
            for x in range(w):
                for y in range(h):
                    if block[y][x] == '#':
                        pos = (x1 + x, y1 + y)
                        grid.add(pos)
            # next block
            break

t = max([j[1] for j in grid if 0 <= j[0] <= 6])
print(t)
