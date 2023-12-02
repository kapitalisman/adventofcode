import re

rx, gx, bx = 12, 13, 14

t = 0

for i, x in enumerate(open(0), 1):
    games = x.split(": ")[1].split("; ")
    for game in games:
        r = re.search(r"\d+(?= r)|$", game).group(0) or 0
        g = re.search(r"\d+(?= g)|$", game).group(0) or 0
        b = re.search(r"\d+(?= b)|$", game).group(0) or 0
        if int(r) > rx or int(g) > gx or int(b) > bx:
            break
    else:
        t += i

print(t)
