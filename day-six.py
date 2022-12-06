#--- Day 6: Tuning Trouble ---

with open('./input/day-six.txt') as f:
    line = f.readline()

def solve(n):
    buffer = []

    for chr in line:
        buffer.append(ord(chr))

    for i in range(len(buffer)):
        set = {int(j) for j in buffer[i:i+n]}
        if len(set) == n:
            print(i + n)
            break

solve(n = 4)

#--- Part Two ---

solve(n = 14)