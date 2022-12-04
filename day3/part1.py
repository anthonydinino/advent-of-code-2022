def main():
    f = open("input.txt", "r")
    totalSum = 0
    for x in f:
        shared = dict()
        x = x.rstrip()
        n = int(len(x)/2)
        rucksack = [x[i:i+n] for i in range(0, len(x), n)]
        for item in rucksack[0]:
            if rucksack[1].find(item) != -1:
                shared[item] = True
        totalSum += sum([getPriority(ch) for ch in shared])
    print(totalSum)
    
def getPriority(ch):
    if ch.islower():
        return ord(ch) - 96
    else:
        return ord(ch) - 38
        
if __name__ == "__main__":
    main()