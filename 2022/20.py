import re
from collections import deque
import copy

from aocd import data, submit, numbers

init = numbers
mod = len(init) - 1


def solve(p):
    key = 1 if p == 1 else 811589153
    start = [num * key for num in init]
    file = [(idx, num * key) for idx, num in enumerate(init)]

    t = 1 if p == 1 else 10
    for _ in range(t):
        for idx, num in enumerate(start):
            # don't move zero, but store for later use
            if num == 0:
                zero = (idx, num)
                continue

            # get index of current number to move
            old = file.index((idx, num))

            # get index of oldition to move to
            new = old + num

            # if new is front move to the end
            if new == 0:
                file.append(file.pop(old))
                continue

            file.insert(new % mod, file.pop(old))

    index = file.index(zero)
    ans = 0
    for i in [1000, 2000, 3000]:
        ans += file[(index + i) % len(init)][1]

    return ans


print(p1 := solve(1))
print(p2 := solve(2))
