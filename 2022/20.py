import re
from collections import deque
import copy

from aocd import data, submit, numbers


def solve(p):
    key = 811589153 if p == 2 else 1
    base = [num * key for num in numbers]
    zero = (base.index(0), 0)
    file = [(idx, num) for idx, num in enumerate(base)]
    mod = len(file)

    for _ in range(10 if p == 2 else 1):
        for idx, num in enumerate(base):
            old = file.index((idx, num))
            new = (old + num) % (mod - 1)
            file.insert(new, file.pop(old))

    z = file.index(zero)
    return sum([file[(z + i * 1000) % mod][1] for i in range(1, 4)])


print(p1 := solve(1))
print(p2 := solve(2))
