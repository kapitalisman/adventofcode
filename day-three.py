#--- Day 3: Rucksack Reorganization ---

total = 0

def process(line: str) -> int:
    compartment_one = line[:len(line)//2]
    compartment_two = line[len(line)//2:]
    for char in compartment_one:
        if char in compartment_two:
            offset = 38 if char.isupper() else 96
            return ord(char) - offset

f = open('./input/day-three.txt', 'r')
for line in f:
    line = line.replace('\n', '')
    if line == '':
        continue
    prio = process(line)
    total += prio

print(total)

#--- Part Two ---

with open('./input/day-three.txt') as f:
    lines = [line.rstrip() for line in f]

groups = zip(*(iter(lines),) * 3)

total = 0

def find_badge(group: tuple[str]) -> str:
    return ''.join(set.intersection(*map(set, group)))

for group in groups:
    badge: str = find_badge(group)
    offset = 38 if badge.isupper() else 96
    prio = ord(badge) - offset
    total += prio

print(total)