grid = open(0).read().splitlines()
nums = []


def f(x):
    (r, c) = x
    n = str()
    while c < len(grid[r]) and grid[r][c].isdigit():
        n += grid[r][c]
        c += 1
    return int(n)


for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch != "*":
            continue
        cs = set()
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
        if len(cs) == 2:
            nums.append(f(cs.pop()) * f(cs.pop()))


t = sum(nums)
print(t)
