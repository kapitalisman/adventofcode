x = open(0).read().split("\n\n")

seeds = list(map(int, x[0].split(":")[1].strip().split()))


def make_f(r):
    d, s, l = list(map(int, r.split()))

    def f(x):
        if s <= x < s + l:
            return x + d - s, True
        return x, False

    return f


def get_map(y):
    m = []
    for r in y:
        f = make_f(r)
        m.append(f)
    return m


maps = list(map(get_map, (e.strip().split("\n")[1:] for e in x[1:])))


def get_loc(j):
    for map in maps:
        for fn in map:
            j, k = fn(j)
            if k:
                break
    return j


locs = list(map(get_loc, seeds))
print(min(locs))
