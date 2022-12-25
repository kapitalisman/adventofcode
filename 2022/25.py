import re
import math
import itertools
from collections import deque

from aocd import data, submit, numbers
lines = data.splitlines()


def snafu_to_decimal(n):
    power = 1
    result = 0
    for d in reversed(n):
        d = -1 if d == '-' else -2 if d == '=' else int(d)
        result += d * power
        power *= 5
    return result


def decimal_to_snafu(n):
    result = ''
    while n > 0:
        r = n % 5
        n //= 5
        if r > 2:
            r -= 5
            n += 1
        d = '-' if r == -1 else '=' if r == -2 else str(r)
        result = d + result
    return result


p1 = 0
for number in lines:
    p1 += snafu_to_decimal(number)

print(decimal_to_snafu(p1))
