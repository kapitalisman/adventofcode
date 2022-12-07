import re
from aocd import data, submit
crates, procedure = data.split('\n\n')


def init():
    stacks = [[] for x in range(9)]

    for line in crates.splitlines():
        index = 0
        for i in list(range(1, len(line), 4)):
            if line[i] != " ":
                stacks[index].append(line[i])
            index += 1

    for stack in stacks:
        stack.pop()
        stack.reverse()

    return stacks


def p(stacks, by_one=False):
    for proc in procedure.splitlines():
        num, fr, to = map(int, re.findall(r"\d+", proc))
        for j in range(num):
            stacks[to - 1].append(stacks[fr -
                                  1].pop(-1 if by_one else j - num))
    return stacks


submit("".join(stack[-1] for stack in p(init(), True)))  # p1
submit("".join(stack[-1] for stack in p(init())))  # p2
