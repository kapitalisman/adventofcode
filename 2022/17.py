from collections import deque
import copy
import math
import re
import functools
import itertools
import json

from aocd import data, submit, numbers

jet_pattern = [-1 if jet == '<' else 1 for jet in list(data)]

A = [0, 1, 2, 3]                     # ['####']
B = [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j]  # ['.#.', '###', '.#.']
C = [0, 1, 2, 2 + 1j, 2 + 2j]        # ['###', '..#', '..#']
D = [0, 1j, 2j, 3j]                  # ['#', '#', '#', '#']
E = [0, 1, 1j, 1 + 1j]               # ['##', '##']

blocks = [A, B, C, D, E]


def get_state(chamber):
    peaks = [0] * 7
    for cell in chamber:
        x = int(cell.real)
        y = int(cell.imag)
        peaks[x] = max(peaks[x], y)
    lowest = min(peaks)
    return tuple(peak - lowest for peak in peaks)


def height(n):
    # init
    grid = {x - 1j for x in range(7)}
    k = -1  # block count
    new_block = True
    states = {}
    delta_t = 0
    # loop
    while k < n:
        for idx, shift in enumerate(jet_pattern):
            if new_block:
                # current height
                t = int(max(j.imag for j in grid)) + 1
                k += 1
                if k == n:
                    break
                # store state of grid
                s = (idx, k % 5, get_state(grid))
                if s in states:
                    k_prev, t_prev = states[s]
                    cycle = (n - k) // (delta_k := k - k_prev)
                    delta_t = cycle * (t - t_prev)
                    k += cycle * delta_k
                    states = {}
                else:
                    states[s] = (k, t)
                # new block
                new_block = False
                block = {x + 2 + (t + 3) * 1j for x in blocks[k % 5]}

            # jet push
            shifted = {x + shift for x in block}
            if any(x.real < 0 or x.real > 6 for x in shifted) or shifted & grid:
                pass
            else:
                block = shifted
            # move down
            shifted = {x - 1j for x in block}
            if shifted & grid:
                grid |= block
                new_block = True
            else:
                block = shifted

    return t + delta_t


print(p1 := height(2022))
print(p2 := height(1000000000000))
