def main():
    pairs = organisePairs("./input.txt")
    result = 0
    for pair in pairs:
        if set(pair[0]).issubset(pair[1]) or set(pair[1]).issubset(pair[0]):
            result += 1
    print(result)


def organisePairs(path):
    f = open(path, "r")
    tempPairs = []
    pairs = []
    for x in f:
        tempPairs.append(x.rstrip().split(','))
    for pair in tempPairs:

        # [[2,4], [6,8]]]
        pair = [allocation.split('-') for allocation in pair]

        # [[2,3,4], [6,7,8]]
        pair = [list(range(int(section[0]), int(section[1]) + 1)) for section in pair] 

        pairs.append(pair)
    return pairs


if __name__ == "__main__":
    main()