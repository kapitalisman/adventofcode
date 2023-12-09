m = {}

for i, x in enumerate(open(0), 1):
    y = x.split(":")[1].strip()
    v, w = [list(map(int, k.split())) for k in y.split(" | ")]
    j = sum(n in v for n in w)

    m[i] = m.get(i, 1)
    for q in range(i + 1, i + j + 1):
        m[q] = m.get(q, 1) + m[i]

print(sum(m.values()))
