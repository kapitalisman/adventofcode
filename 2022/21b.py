import re

from aocd import data, submit, numbers
lines = data.splitlines()

pattern = re.compile(r'\d+')


for line in lines:
    monkey, eq = line.split(': ')
    if pattern.match(eq):
        if monkey == 'humn':
            eq = 'i'
    else:
        if monkey == 'root':
            eq = eq.replace('+', '==')
        eq = eq[:4] + '()' + eq[4:] + '()'

    f = f'def {monkey}(): return {eq}'
    exec(f)


def eval_right(a):
    global i
    i = a
    return eval('jwcq()')


def goal_seek(target, precision):
    lower = 0
    upper = 10_000_000_000_000
    threshold = precision
    while abs(threshold) >= precision:
        solve = (lower + upper) // 2
        threshold = target - eval_right(solve)

        if threshold > 0:
            upper = solve
        elif threshold < 0:
            lower = solve

    return solve


left = eval('swbn()')
print(p2 := goal_seek(left, 0.01))
