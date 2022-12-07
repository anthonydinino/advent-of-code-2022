def main():
    f = open("/home/anthony.dinino/Work/adventOfCode2022/day7/test.txt", "r")
    cd = ""
    directoryPath = []
    currentLevel = 0
    folderStructure = {}
    storage = {}
    listing = False
    for x in f:

        # Get current directory which is end of directory path list
        if len(directoryPath) > 0:
            cd = directoryPath[len(directoryPath)- 1]
        
        # Command as a list
        comm = x.rstrip().split(" ")

        # No longer listing a file
        if comm[0] == "$":
            listing = False

        if not listing:
            if comm[0] == "$":
                if comm[1] == "cd":
                    if comm[2] == "..":
                        directoryPath.pop()
                    else:
                        directoryPath.append(comm[2])
                        currentLevel += 1
                elif comm[1] == "ls":
                    listing = True
        else:
            if comm[0] != "dir":
                storage[cd] = storage.get(cd, 0) + int(comm[0])
        print(cd)
    print(folderStructure)
    print(storage)

if __name__ == "__main__":
    main()