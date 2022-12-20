import re
from collections import deque
import copy

from aocd import data, submit, numbers


def solve(p):
    key = 811589153 if p == 2 else 1
    start = [num * key for num in numbers]
    file = [(idx, num) for idx, num in enumerate(start)]
    mod = len(file)

    for _ in range(10 if p == 2 else 1):
        for idx, num in enumerate(start):
            if num == 0:
                zero = (idx, num)
                continue
            old = file.index((idx, num))
            new = (old + num) % (mod - 1)
            file.insert(new, file.pop(old))

    z = file.index(zero)
    t = 0
    for i in [1000, 2000, 3000]:
        t += file[(z + i) % mod][1]

    return t


print(p1 := solve(1))
print(p2 := solve(2))
