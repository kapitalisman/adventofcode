from collections import deque
import copy
import math
import re
import functools
import json
from aocd import data, submit


def cmp(left, right):
    if type(left) == int:
        if type(right) == int:
            return left - right
        return cmp([left], right)

    if type(right) == int:
        return cmp(left, [right])

    for a, b in zip(left, right):
        if res := cmp(a, b):
            return res

    return len(left) - len(right)


# part 1
pairs = map(str.splitlines, data.split("\n\n"))
p1 = 0
for idx, [left, right] in enumerate(pairs, start=1):
    if cmp(json.loads(left), json.loads(right)) < 0:
        p1 += idx

print(p1)


# part 2
dividers = ([[2]], [[6]])

# method 1
d2 = 1
d6 = 2

packets = map(json.loads, data.split())
for packet in packets:
    if cmp(packet, dividers[0]) < 0:
        d2 += 1
        d6 += 1
    elif cmp(packet, dividers[1]) < 0:
        d6 += 1

print(p2 := d2 * d6)


# method 2
packets = list(map(json.loads, data.split()))
packets.extend(dividers)
packets.sort(key=functools.cmp_to_key(cmp))
d2 = packets.index(dividers[0]) + 1
d6 = packets.index(dividers[1]) + 1

print(p2 := d2 * d6)
