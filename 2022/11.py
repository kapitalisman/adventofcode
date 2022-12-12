import copy
import math
import re

from aocd import data, numbers, submit
lines = data.splitlines()

input = data.split('\n\n')
monkeys = len(input)

start = []
newop = []
divby = []
monkt = []
monkf = []

# process input
for monkey in input:
    _, a, b, c, d, e = monkey.split('\n')
    start.append([int(s) for s in a.split(': ')[1].split(', ')])
    newop.append(eval('lambda old:' + b.split('=')[1]))
    divby.append(int(c.split()[-1]))
    monkt.append(int(d.split()[-1]))
    monkf.append(int(e.split()[-1]))

p1, p2 = [[0] * monkeys for _ in [1, 2]]

# process rounds
lcm = math.lcm(*divby)
for idx, p in enumerate([p1, p2], start=1):
    items = copy.deepcopy(start)
    for _ in range(20 if idx == 1 else 10000):
        for i in range(monkeys):
            for item in items[i]:
                item = newop[i](item) % lcm
                if idx == 1:
                    item //= 3
                j = monkt[i] if item % divby[i] == 0 else monkf[i]
                items[j].append(item)
            p[i] += len(items[i])
            items[i] = []

    p.sort()
    print(p[-1] * p[-2])
