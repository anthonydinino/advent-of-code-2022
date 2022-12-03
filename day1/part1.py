f = open("input.txt", "r")

currentElf = 0
maxCalories = 0
for x in f:
    if x != "\n":
        currentElf += int(x)
    else:
        if maxCalories < currentElf:
            maxCalories = currentElf
        currentElf = 0

print(maxCalories)