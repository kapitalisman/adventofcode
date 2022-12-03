#--- Day 2: Rock Paper Scissors ---

score = 0

def process(line):
    match line:
        case "A X":
            return 3 + 1
        case "A Y":
            return 6 + 2
        case "A Z":
            return 0 + 3
        case "B X":
            return 0 + 1
        case "B Y":
            return 3 + 2
        case "B Z":
            return 6 + 3
        case "C X":
            return 6 + 1
        case "C Y":
            return 0 + 2
        case "C Z":
            return 3 + 3

f = open('./input/day-two.txt', 'r')
for line in f:
    line = line.replace('\n', '')
    if line == '':
        continue
    points = process(line)
    score += points

print(score)

#--- Part Two ---

new_score = 0

def new_process(line):
    match line:
        case "A X":
            return 0 + 3
        case "A Y":
            return 3 + 1
        case "A Z":
            return 6 + 2
        case "B X":
            return 0 + 1
        case "B Y":
            return 3 + 2
        case "B Z":
            return 6 + 3
        case "C X":
            return 0 + 2
        case "C Y":
            return 3 + 3
        case "C Z":
            return 6 + 1

f = open('./input/day-two.txt', 'r')
for line in f:
    line = line.replace('\n', '')
    if line == '':
        continue
    points = new_process(line)
    new_score += points

print(new_score)