import re
import itertools

from aocd import data, submit, numbers
rows = data.splitlines()


def plot(elves):
    all_x = [int(elf.real) for elf in elves]
    all_y = [int(elf.imag) for elf in elves]
    min_x, max_x, min_y, max_y = min(all_x), max(all_x), min(all_y), max(all_y)
    for y in range(min_y, max_y + 1):
        line = []
        for x in range(min_x, max_x + 1):
            if (x + y * 1j) in elves:
                line.append('#')
            else:
                line.append('.')
        print(''.join(line))


elves = set()

for imag, row in enumerate(rows):
    for real, col in enumerate([*row]):
        if col == '#':
            elves.add(real + imag * 1j)


N = {-1 - 1j, -1j, 1 - 1j}
S = {-1 + 1j, 1j, 1 + 1j}
W = {-1 + 1j, -1, -1 - 1j}
E = {1 + 1j, 1, 1 - 1j}
A = N | S | W | E

compass = [(N, -1j), (S, 1j), (W, -1), (E, 1)]

i = 0
r = 0
while True:

    elves_ = set()
    elves__ = set()

    for elf in elves:
        # if all around is empty: don't move
        if not {elf + d for d in A} & elves:
            elves_.add(elf)
            continue

        # otherwise
        move = False
        for j in range(4):
            if not {elf + d for d in compass[(i + j) % 4][0]} & elves:
                move = True
                elves__.add((elf, elf + compass[(i + j) % 4][1]))
                break

        # if all directions are non-empty: don't move
        if not move:
            elves_.add(elf)

    # each elf moves (or not)
    proposals = [new for old, new in elves__]
    for old, new in elves__:
        if proposals.count(new) == 1:
            elves_.add(new)
        else:
            elves_.add(old)

    # next round
    if elves == elves_:
        print(p2 := r + 1)
        break
    elves = elves_
    i += 1
    r += 1
    if r == 10:
        all_x = [int(elf.real) for elf in elves]
        all_y = [int(elf.imag) for elf in elves]
        min_x, max_x, min_y, max_y = min(all_x), max(all_x), min(all_y), max(all_y)
        squares = (max_x - min_x + 1) * (max_y - min_y + 1)
        print(p1 := squares - len(elves))
