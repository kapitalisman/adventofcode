import random
import copy

from aocd import data, submit, numbers
lines = data.splitlines()

valves_start = dict()
for line in lines:
    key = line.split()[1]
    rate = int(line.split('=')[1].split(';')[0])
    tunnels = [x[-2:] for x in line.split(', ')]
    closed = True
    valves_start[key] = [rate, tunnels, closed]


def monte_carlo():
    t = 1
    T = 30
    release = 0
    release_incr = 0
    valve = 'AA'
    valves = copy.deepcopy(valves_start)

    while t <= T:
        candidates = [x for x in valves[valve][1] if valves[x][0] >= 10 and valves[x][2] == True]
        if candidates:
            valve = random.choice(candidates)
        else:
            valve = random.choice(valves[valve][1])
        release += release_incr
        if t >= T:
            break
        t += 1
        if valves[valve][2] == False or valves[valve][0] == 0:
            continue  # do not open valve

        if random.choice([True, False]) or valves[valve][0] >= 10:
            release += release_incr
            t += 1
            valves[valve][2] = False
            release_incr += valves[valve][0]

    return release


p1 = 0
for _ in range(1_000_000):
    p1 = max(p1, monte_carlo())

print(p1)
