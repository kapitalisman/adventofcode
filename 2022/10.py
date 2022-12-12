from aocd import data, numbers, submit
lines = data.splitlines()

t = 0
x = 1
sig = []

for line in lines:
    t += 1
    sig.append((t, x))

    words = line.split()
    if words[0] == 'addx':
        t += 1
        sig.append((t, x))
        x += int(words[1])

t_end = [39 + 40 * i for i in range(6)]
p1 = sum(tx[0] * tx[1] for tx in sig if tx[0] in [j - 19 for j in t_end])
print(p1)

screen = []
crtline = []
for k in range(240):
    crtline.append("#") if abs(k % 40 - sig[k][1]) <= 1 else crtline.append(" ")
    if k in t_end:
        screen.append(crtline)
        crtline = []

for pixels in screen:
    print(*pixels)
