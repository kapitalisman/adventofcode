#--- Day 1: Calorie Counting ---

with open('./input/day-one.txt') as f:
    lines = f.read()

elves = lines.split('\n\n')

def split_elves(elf):
    return filter(None, elf.split('\n'))

food = list(map(split_elves, elves))
food_snacks = [[int(snack) for snack in snacks] for snacks in food]

calories = [sum(snack) for snack in food_snacks]
print(max(calories))

#--- Part Two ---

top_three = sorted(calories, reverse=True)[:3]
print(sum(top_three))