import re
from collections import deque
import copy

from aocd import data, submit, numbers

init = numbers
length = len(init)


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
            pos = file.index((idx, num))

            new = pos + num

            if abs(new) >= length:
                new = new % (length - 1)
                file.insert(new, file.pop(pos))
                continue

            if new == 0:
                file.append(file.pop(pos))
                continue

            if new == length - 1:
                file.insert(0, file.pop(pos))
                continue

            if new < 0:
                file.insert(new, file.pop(pos))
                continue

            file.insert(new, file.pop(pos))

    index = file.index(zero)
    _, th1 = file[(index + 1000) % len(init)]
    _, th2 = file[(index + 2000) % len(init)]
    _, th3 = file[(index + 3000) % len(init)]

    return th1 + th2 + th3


print(p1 := solve(1))
print(p2 := solve(2))
