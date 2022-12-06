from aocd import data, submit
elves = data.split('\n\n')

food = list(map(lambda elf: map(int, elf.split('\n')), elves))
calories = [sum(snack) for snack in food]

submit(max(calories)) #p1
submit(sum(sorted(calories, reverse=True)[:3])) #p2