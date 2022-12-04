def main():
    groups = organiseIntoGroups("input.txt")

    # For every group get the their badge and it's priority value
    groupBadges = [getPriority(findBadge(group)) for group in groups]

    # Sum all priorities for answer
    print(sum(groupBadges))

def organiseIntoGroups(path):
    count = 0
    temp = []
    groups = []
    f = open(path, "r")
 
    for x in f:
        x = x.rstrip()
        temp.append(x)
        count += 1
        if count > 2:
            groups.append(temp)
            temp = []
            count = 0
    
    return groups

def findBadge(group):
    occurences = dict()

    # For each rucksack, add 1 to dictionary if there is 1 or more occurences of each item
    for rucksack in group:
        temp = dict()
        for item in rucksack:
            temp[item] = True
        for item in temp:
            occurences[item] = occurences.get(item, 0) + 1

    # If item exists in all 3 rucksacks, it's probably the badge
    for k, v in occurences.items():
        if v == 3:
            return k
    
def getPriority(ch):
    if ch.islower():
        return ord(ch) - 96
    else:
        return ord(ch) - 38
        
if __name__ == "__main__":
    main()