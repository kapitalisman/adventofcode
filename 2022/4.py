import re
from aocd import data, submit
lines = data.splitlines()


def p1(line):
    a, b, c, d = map(int, re.split(r',|-', line))
    if a <= c and d <= b:
        return True
    if c <= a and b <= d:
        return True
    return False


def p2(line):
    a, b, c, d = map(int, re.split(r',|-', line))
    if not (b < c or d < a):
        return True
    return False


def score(func):
    score = 0
    for line in lines:
        res = func(line)
        if res:
            score += 1
    return score


submit(score(p1))  # p1
submit(score(p2))  # p2
