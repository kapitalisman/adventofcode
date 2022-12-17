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


intervals = []
beacons = set()
y = 2_000_000

for x1, y1, x2, y2 in input:
    d = abs(y1 - y2) + abs(x1 - x2)
    if (dx := d - abs(y1 - y)) < 0:
        continue
    intervals.append((x1 - dx, x1 + dx))
    if y2 == y:
        beacons.add(x2)
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

p1 = sum([hi - lo + 1 for lo, hi in combined]) - len(beacons)
print(p1)
