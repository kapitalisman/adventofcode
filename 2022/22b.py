import re

from aocd import data, submit, numbers

# data = '''        ...#
#         .#..
#         #...
#         ....
# ...#.......#
# ........#...
# ..#....#....
# ..........#.
#         ...#....
#         .....#..
#         .#......
#         ......#.

# 10R5L5R10L4R5L5'''

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


def recalculate(s, d):
    # 1-3
    if s.real == 99 and 50 <= s.imag < 100 and d == 1:
        return (s.imag + 50 + 49 * 1j, -1j)
    if 100 <= s.real < 150 and s.imag == 49 and d == 1j:
        return (99 + (s.real - 50) * 1j, -1)
    # 3-4
    if s.real == 99 and 100 <= s.imag < 150 and d == 1:
        return (149 + (149 - s.imag) * 1j, -1)
    if s.real == 149 and 0 <= s.imag < 50 and d == 1:
        return (99 + (149 - s.imag) * 1j, -1)
    # 2-4
    if s.real == 49 and 150 <= s.imag < 200 and d == 1:
        return (s.imag - 100 + 149 * 1j, -1j)
    if 50 <= s.real < 100 and s.imag == 149 and d == 1j:
        return (49 + (100 + s.real) * 1j, -1)
    # 4-7
    if 0 <= s.real < 50 and s.imag == 199 and d == 1j:
        return (s.real + 100, 1j)
    if 100 <= s.real < 150 and s.imag == 0 and d == -1j:
        return (s.real - 100 + 199 * 1j, -1j)
    # 7-8
    if s.real == 0 and 150 <= s.imag < 200 and d == -1:
        return (s.imag - 100, 1j)
    if 50 <= s.real < 100 and s.imag == 0 and d == -1j:
        return ((s.real + 100) * 1j, 1)
    # 5-8
    if s.real == 0 and 100 <= s.imag < 150 and d == -1:
        return (50 + (149 - s.imag) * 1j, 1)
    if s.real == 50 and 0 <= s.imag < 50 and d == -1:
        return ((149 - s.imag) * 1j, 1)
    # 5-6
    if s.real == 50 and 50 <= s.imag < 100 and d == -1:
        return (s.imag - 50 + 100 * 1j, 1j)
    if 0 <= s.real < 50 and s.imag == 100 and d == -1j:
        return (50 + (s.real + 50) * 1j, 1)
    print(s, d)
    assert False


for number, letter in steps:
    s_ = s
    d_ = d
    i = 0
    while i < int(number):
        s_ = s_.real + d.real + (s_.imag + d.imag) * 1j
        if s_ not in field:
            # re-calculate s_ and d
            (s_, d_) = recalculate(s, d)
        if s_ in walls:
            break
        s = s_
        d = d_
        i += 1
    if letter == 'R':
        d *= 1j
    elif letter == 'L':
        d *= -1j
    else:
        facing = d.imag + 2 if (d.real < 0 or d.imag < 0) else 0
        p2 = 1000 * (s.imag + 1) + 4 * (s.real + 1) + facing

print(p2)
