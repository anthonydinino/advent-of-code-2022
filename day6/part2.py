def main():
    f = open("input.txt", "r")
    message = f.read()
    print(findFirstUniqueValue(message, 14))

def findFirstUniqueValue(message, length):
    for i in range(length-1, len(message)):
        testString = ""
        for j in range(length):
            testString += message[i-length+1+j]
        if len(set(testString)) == length:
            return i + 1

if __name__ == "__main__":
    main()