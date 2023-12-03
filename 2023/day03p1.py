grid = open(0).read().splitlines()
cs = set()


def f(x):
    (r, c) = x
    n = str()
    while c < len(grid[r]) and grid[r][c].isdigit():
        n += grid[r][c]
        c += 1
    return int(n)


for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch.isdigit() or ch == ".":
            continue
        for rr in [r - 1, r, r + 1]:
            for cc in [c - 1, c, c + 1]:
                if (
                    rr < 0
                    or rr >= len(grid)
                    or cc < 0
                    or cc >= len(grid[rr])
                    or not grid[rr][cc].isdigit()
                ):
                    continue
                while cc > 0 and grid[rr][cc - 1].isdigit():
                    cc -= 1
                cs.add((rr, cc))

nums = []
for x in cs:
    nums.append(f(x))

t = sum(nums)
print(t)
