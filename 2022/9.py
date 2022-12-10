from aocd import data, numbers, submit
lines = list(map(str, data.splitlines()))

hx, hy, tx, ty = [0] * 4
p1 = set()
moves = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

for line in lines:
    dir, n = line.split()
    n = int(n)
    x, y = moves[dir]
    for i in range(n):
        hx += x
        hy += y
        if abs(hy - ty) == 2:
            ty += (hy - ty) / 2
            tx = hx
        if abs(hx - tx) == 2:
            tx += (hx - tx) / 2
            ty = hy
        p1.add((tx, ty))

print(len(p1))

pos = [[0, 0] for _ in range(10)]
p2 = set()

for line in lines:
    dir, n = line.split()
    n = int(n)
    x, y = moves[dir]
    for i in range(n):
        # head moves first
        pos[0][0] += x
        pos[0][1] += y
        # other knots move one by one
        for j in range(1, 10):
            has_moved = False
            for k in [0, 1]:
                if abs(pos[j - 1][k] - pos[j][k]) == 2:
                    pos[j][k] += (pos[j - 1][k] - pos[j][k]) / 2
                    if abs(pos[j - 1][1 - k] - pos[j][1 - k]) == 2:
                        pos[j][1 - k] += (pos[j - 1][1 - k] - pos[j][1 - k]) / 2
                    else:
                        pos[j][1 - k] = pos[j - 1][1 - k]
                    has_moved = True
            # if the knot did not move, skip remaining knots
            if not has_moved:
                break
        # add p1 of tail
        p2.add(tuple(pos[9]))

print(len(p2))
