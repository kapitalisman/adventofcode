import re

t = 0

for x in open(0):
    games = x.split(": ")[1].split("; ")
    rx, gx, bx = 0, 0, 0
    for game in games:
        r = re.search(r"\d+(?= r)|$", game).group(0) or 0
        rx = max(int(r), rx)
        g = re.search(r"\d+(?= g)|$", game).group(0) or 0
        gx = max(int(g), gx)
        b = re.search(r"\d+(?= b)|$", game).group(0) or 0
        bx = max(int(b), bx)
    power = rx * gx * bx
    t += power

print(t)
