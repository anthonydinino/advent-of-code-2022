def main():
    f = open("input.txt", "r")
    totalPoints = 0
    for x in f:
        round = x.strip().split(" ")
        round = changeOutcome(round)
        totalPoints += decisionPoints(round) + outcomePoints(round)
    print(totalPoints)

def changeOutcome(round):
    if round[1] == "X":
        return tryToLose(round)
    if round[1] == "Y":
        return tryToDraw(round)
    if round[1] == "Z":
        return tryToWin(round)

def tryToDraw(round):
    opponent = round[0]
    if opponent == "A":
        return [opponent, "X"]
    elif opponent == "B":
        return [opponent, "Y"]
    elif opponent == "C":
        return [opponent, "Z"]

def tryToLose(round):
    opponent = round[0]
    if opponent == "A":
        return [opponent, "Z"]
    elif opponent == "B":
        return [opponent, "X"]
    elif opponent == "C":
        return [opponent, "Y"]

def tryToWin(round):
    opponent = round[0]
    if opponent == "A":
        return [opponent, "Y"]
    elif opponent == "B":
        return [opponent, "Z"]
    elif opponent == "C":
        return [opponent, "X"]


def decisionPoints(round):
    player = round[1]

    if player == "X":
        return 1
    elif player == "Y":
        return 2
    else:
        return 3

def outcomePoints(round):
    opponent = round[0]
    player = round[1]

    if opponent == "A" and player == "X":
        return 3
    elif opponent == "B" and player == "Y":
        return 3
    elif opponent == "C" and player == "Z":
        return 3
    elif opponent == "A" and player == "Y":
        return 6
    elif opponent == "B" and player == "Z":
        return 6
    elif opponent == "C" and player == "X":
        return 6
    elif opponent == "A" and player == "Z":
        return 0
    elif opponent == "B" and player == "X":
        return 0
    elif opponent == "C" and player == "Y":
        return 0
    else:
        return "invalid"    

if __name__ == "__main__":
    main()