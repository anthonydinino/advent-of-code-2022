f = open("input.txt", "r")

currentElf = 0
elfCalories = []
for x in f:
    if x != "\n":
        currentElf += int(x)
    else:
        elfCalories.append(currentElf)
        currentElf = 0

print(sum(sorted(elfCalories, reverse=True)[0:3]))