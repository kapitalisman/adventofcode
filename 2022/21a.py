import re

from aocd import data, submit, numbers
lines = data.splitlines()

pattern = re.compile(r'\d+')


for line in lines:
    monkey, eq = line.split(': ')
    if pattern.match(eq):
        pass
    else:
        eq = eq[:4] + '()' + eq[4:] + '()'

    f = f'def {monkey}(): return {eq}'
    exec(f)


print(p1 := int(eval('root()')))
