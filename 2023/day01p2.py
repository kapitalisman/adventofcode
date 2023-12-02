import re

t = 0

nums = "one two three four five six seven eight nine".split()

p = r"\d|" + r"|".join(nums)


def f(n):
    if n in nums:
        return str(nums.index(n) + 1)
    return str(n)


for x in open(0):
    d = re.findall("(?=(" + p + "))", x)
    t += int(f(d[0]) + f(d[-1]))

print(t)
