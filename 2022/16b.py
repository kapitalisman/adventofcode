import random
import copy
from collections import deque

from aocd import data, submit, numbers

data = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II'''

lines = data.splitlines()

# process lines
valves = {}
tunnels = {}
for line in lines:
    valve = line.split()[1]
    flow = int(line.split('=')[1].split(';')[0])
    targets = [x[-2:] for x in line.split(', ')]
    valves[valve] = flow
    tunnels[valve] = targets

# simplify valves/tunnels system
distance = {}  # stores distance from valve with rate = 0 to every other valve with rate > 0
for valve in valves:
    # skip valves with rate > 0
    if valves[valve]:
        continue

    # add self (avoid KeyError)
    distance[valve] = {valve: 0}
    visited = {valve}

    # q stores (valve, distance)
    q = deque([(valve, 0)])
    while q:
        valv, dist = q.popleft()
        # consider all neighbors (nb)
        for nb in tunnels[valv]:
            # check if already visited
            if nb in visited:
                continue
            visited.add(nb)
            # only add neighbors with rate > 0
            if valves[nb]:
                distance[valve][nb] = dist + 1
            q.append((nb, dist + 1))

    # delete self
    del distance[valve][valve]

print(distance)
