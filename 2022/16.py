from collections import deque

from aocd import data, submit, numbers
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
distance = {}
for valve in valves:
    # skip valves with rate > 0
    if valve != 'AA' and not valves[valve]:
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


bits = {valve: idx for idx, valve in enumerate({valve: dist for valve, dist in distance.items() if valve != 'AA'})}


def explore_paths(valve, time, open):
    state = (valve, time, open)
    if state in states:
        return states[state]

    release = 0
    for nb, d in distance[valve].items():
        bit = 1 << bits[nb]
        # if valve is already open
        if open & bit:
            continue
        # if there is no time left
        time_remaining = time - d
        if time_remaining <= 1:
            continue
        # open the valve
        time_remaining -= 1
        # keep exploring
        release = max(release, explore_paths(nb, time_remaining, open | bit) + valves[nb] * time_remaining)

    states[state] = release
    return release


states = {}
print(p1 := explore_paths('AA', 30, 0))


states = {}
m = (1 << len(bits))

p2 = 0
for i in range(m // 2):
    p2 = max(p2, explore_paths('AA', 26, i) + explore_paths('AA', 26, m - i - 1))

print(p2)
