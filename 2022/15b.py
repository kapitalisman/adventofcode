from collections import deque
import copy
import math
import re
import functools
import json

from aocd import data, submit, numbers
lines = data.splitlines()

pattern = re.compile(r'-?\d+')
input = [list(map(int, pattern.findall(line))) for line in lines]


bound = 4_000_000
p2 = -1

for y in range(bound + 1):
    if p2 >= 0:
        break
    intervals = []
    for x1, y1, x2, y2 in input:
        d = abs(y1 - y2) + abs(x1 - x2)
        if (dx := d - abs(y1 - y)) < 0:
            continue
        intervals.append((x1 - dx, x1 + dx))
    intervals.sort()

    combined = []
    for lo, hi in intervals:
        if not combined:
            combined.append([lo, hi])
            continue
        lo_prev, hi_prev = combined[-1]
        if lo > hi_prev + 1:
            combined.append([lo, hi])
            continue
        combined[-1] = [lo_prev, max(hi, hi_prev)]

    x = 0
    for lo, hi in combined:
        if x > hi:
            continue
        if x < lo:
            p2 = x * 4_000_000 + y
            break
        if (x := hi + 1) > bound:
            break

print(p2)
