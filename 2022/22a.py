import re

from aocd import data, submit, numbers

board, steps = data.split('\n\n')
rows = board.splitlines()

tiles = set()
walls = set()

width = height = 0
for imag, row in enumerate(rows):
    for real, col in enumerate([*row]):
        width = max(width, real + 1)
        height = max(height, imag + 1)
        match col:
            case '.':
                tiles.add(real + imag * 1j)
            case '#':
                walls.add(real + imag * 1j)
            case _:
                continue

field = tiles | walls

pattern = re.compile(r'(\d+)([RL]?)')
steps = pattern.findall(steps)

# start position
s = min([tile.real for tile in tiles if tile.imag == 0j])

# start direction
d = 1

# Rotation to the right: d * 1j
# Rotation to the left: d * -1j

for number, letter in steps:
    m = width if d.imag == 0 else height
    s_ = s
    i = 0
    while i < int(number):
        s_ = (s_.real + d.real) % m + ((s_.imag + d.imag) % m) * 1j
        if s_ not in field:
            continue
        if s_ in tiles:
            s = s_
            i += 1
            continue
        if s_ in walls:
            break
    if letter == 'R':
        d *= 1j
    elif letter == 'L':
        d *= -1j
    else:
        facing = d.imag + 2 if (d.real < 0 or d.imag < 0) else 0
        p1 = 1000 * (s.imag + 1) + 4 * (s.real + 1) + facing

print(p1)
