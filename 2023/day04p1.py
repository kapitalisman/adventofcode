t = 0

for x in open(0):
    y = x.split(":")[1].strip()
    v, w = [list(map(int, k.split())) for k in y.split(" | ")]
    j = sum(n in v for n in w)
    if j > 0:
        t += 2 ** (j - 1)

print(t)
