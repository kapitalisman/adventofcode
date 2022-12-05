#--- Day 4: Camp Cleanup ---

import re

def process(line: str) -> bool:
    min_one, max_one, min_two, max_two = map(int, re.split(',|-', line))
    if min_one <= min_two and max_two <= max_one:
        return True
    if min_two <= min_one and max_one <= max_two:
        return True
    return False

lines = 0

f = open('./input/day-four.txt', 'r')
for line in f:
    line = line.strip()
    if line == '':
        continue
    result = process(line)
    if result:
        lines += 1

print(lines)

#--- Part Two ---

def overlap(line: str) -> bool:
    min_one, max_one, min_two, max_two = map(int, re.split(r',|-', line))
    if not (max_one < min_two or max_two < min_one):
        return True
    return False

paires = 0

f = open('./input/day-four.txt', 'r')
for line in f:
    line = line.strip()
    if line == '':
        continue
    result = overlap(line)
    if result:
        paires += 1

print(paires)