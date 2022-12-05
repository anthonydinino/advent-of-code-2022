import re

def main():
    stacks = [
        ['Z', 'T', 'F', 'R', 'W', 'J', 'G'],
        ['G', 'W', 'M'],
        ['J', 'N', 'H', 'G'],
        ['J', 'R', 'C', 'N', 'W'],
        ['W', 'F', 'S', 'B', 'G', 'Q', 'V', 'M'],
        ['S', 'R', 'T', 'D', 'V', 'W', 'C'],
        ['H', 'B', 'N', 'C', 'D', 'Z', 'G', 'V'],
        ['S', 'J', 'N', 'M', 'G', 'C'],
        ['G', 'P', 'N', 'W', 'C', 'J', 'D', 'L'],
    ]

    moves = organiseMoves("input.txt")
    
    # Execute move set
    for move in moves:
        stacks = moveCrate(stacks, move[0], move[1], move[2])

    # Print answer
    for stack in stacks:
        print(stack[len(stack)-1], end='')
    print()


def organiseMoves(path):
    tempMoves = []
    moves = []
    f = open(path, "r")

    # Look for all lines that start with move and have digits
    for x in f:
        if x.startswith("move"):
            tempMoves.append(re.findall("\d+", x))
    
    # Cast all move instructions into an integer
    for move in tempMoves:
        moves.append([int(num) for num in move])

    return moves
                

def moveCrate(stacks, quantity, fromStack, toStack):
    # Get the last quantity of elements
    cratesToMove = stacks[fromStack-1][-quantity:]

    # Remove those elements from the stack
    stacks[fromStack-1] = stacks[fromStack-1][:-quantity]

    # Add correct crates to the toStack
    for crate in cratesToMove:
        stacks[toStack-1].append(crate)
   
    return stacks

if __name__ == "__main__":
    main()