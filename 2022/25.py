import re
import math
import itertools
from collections import deque

from aocd import data, submit, numbers
lines = data.splitlines()


def decimal(n):
    power = 1
    res = 0
    for d in reversed(n):
        d = -1 if d == '-' else -2 if d == '=' else int(d)
        res += d * power
        power *= 5
    return res


def base_five(n):
    res = ''
    quotient = n
    while quotient > 0:
        remainder = quotient % 5
        quotient //= 5
        res = str(remainder) + res
    return res


p1 = 0
for number in lines:
    p1 += decimal(number)

print(p1)  # 35951702021395
print(base_five(p1))  # 14203013041204141040 -> 2-21=02=1-121-2-11-0
