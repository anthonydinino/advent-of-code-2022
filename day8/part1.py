def main():
    f = open("input.txt", "r")
    trees = []
    for x in f:
        trees.append([int(tree) for tree in x.strip()])
    visible = getVisible(trees)
    print(visible)


def getVisible(trees):
    visible = 0
    for i, row in enumerate(trees):
        for j, tree in enumerate(row):
            if i == 0 or i == len(row) - 1 or j == 0 or j == len(row) - 1:
                visible += 1

            # Tree must be inside
            else:
                # check left
                leftExposed = True
                for x in range(j - 1, -1, -1):
                    if trees[i][x] >= tree:
                        leftExposed = False

                # check right
                rightExposed = True
                for x in range(j + 1, len(row)):
                    if trees[i][x] >= tree:
                        rightExposed = False

                # check up
                upExposed = True
                for y in range(i - 1, -1, -1):
                    if trees[y][j] >= tree:
                        upExposed = False

                # check down
                downExposed = True
                for y in range(i, len(trees)):
                    if trees[y][j] >= tree:
                        downExposed = False

                if leftExposed or rightExposed or upExposed or downExposed:
                    visible += 1
    return visible


if __name__ == "__main__":
    main()
