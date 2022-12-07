from aocd import data, submit


def p(n):
    buffer = []

    for chr in data:
        buffer.append(ord(chr))

    for i in range(len(buffer)):
        set = {int(j) for j in buffer[i:i+n]}
        if len(set) == n:
            return i + n


submit(p(4))
submit(p(14))
