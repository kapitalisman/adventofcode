from aocd import data, submit
lines = data.splitlines()
groups = list(zip(*(iter(lines),) * 3))

def score(iter, func):
    score = 0
    for i in iter:
        score += func(i)
    return score

def val(c):
    return ord(c) - (38 if c.isupper() else 96)

def p1(line):
    comp_one = line[:len(line)//2]
    comp_two = line[len(line)//2:]
    for char in comp_one:
        if char in comp_two:
            return val(char)

def p2(group):
    badge = ''.join(set.intersection(*map(set, group)))
    return val(badge)

submit(score(lines, p1)) #p1
submit(score(groups, p2)) #p2