from collections import deque
import copy
import math
import re
import functools

from aocd import data, submit
pairs = data.split('\n\n')


def compare(l, r):
    if len(l) == 0 and len(r) != 0:
        return True
    if len(r) == 0 and len(l) != 0:
        return False
    for i in range(len(l)):
        if i >= len(r):
            return False
        if isinstance(l[i], list) and isinstance(r[i], list):
            result = compare(l[i], r[i])
            if result is None:
                continue
            return result
        if isinstance(l[i], int) and isinstance(r[i], list):
            result = compare([l[i]], r[i])
            if result is None:
                continue
            return result
        if isinstance(l[i], list) and isinstance(r[i], int):
            result = compare(l[i], [r[i]])
            if result is None:
                continue
            return result
        if isinstance(l[i], int) and isinstance(r[i], int):
            if l[i] < r[i]:
                return True
            if l[i] > r[i]:
                return False
            continue
    if len(r) > len(l):
        return True


results = []
for idx, pair in enumerate(pairs):
    l, r = pair.splitlines()
    l = eval(l)
    r = eval(r)
    result = compare(l, r)
    results.append((idx + 1, result))

print(sum(x[0] for x in results if x[1] == True))

# part 2
packets = [[[2]], [[6]]]
for pair in pairs:
    l, r = pair.splitlines()
    packets.append(eval(l))
    packets.append(eval(r))


def rang(a, b):
    result = compare(a, b)
    return -1 if result else 1


sorted_packets = sorted(packets, key=functools.cmp_to_key(rang))

key = 1
for loc, packet in enumerate(sorted_packets):
    if packet == [[2]] or packet == [[6]]:
        key *= (loc + 1)

print(key)
