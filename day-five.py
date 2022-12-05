#--- Day 5: Supply Stacks ---

import re

num_of_stacks = 9
length_of_line = 35

with open('./input/day-five.txt') as f:
    crates, procedure = f.read().split("\n\n")

stacks = [[] for x in range(num_of_stacks)]

for line in crates.splitlines():
    index = 0
    for i in list(range(1, length_of_line, 4)):
        if line[i] != " ":
            stacks[index].append(line[i])
        index += 1

for stack in stacks:
    stack.pop()
    stack.reverse()

for proc in procedure.splitlines():
    num, fr, to = map(int, re.findall(r"\d+", proc))
    for j in range(num):
        stacks[to - 1].append(stacks[fr - 1].pop())

print("".join(stack[-1] for stack in stacks))

#--- Part Two ---

stacks = [[] for x in range(num_of_stacks)]

for line in crates.splitlines():
    index = 0
    for i in list(range(1, length_of_line, 4)):
        if line[i] != " ":
            stacks[index].append(line[i])
        index += 1

for stack in stacks:
    stack.pop()
    stack.reverse()

for proc in procedure.splitlines():
    num, fr, to = map(int, re.findall(r"\d+", proc))
    for j in range(num):
        stacks[to - 1].append(stacks[fr - 1].pop(j - num))

print("".join(stack[-1] for stack in stacks))