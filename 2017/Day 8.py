f = open("Day 8.txt").readlines()
mainDict = {}

def action(action, num, happening):
    if not happening:
        return 0
    elif action == "inc":
        return num
    elif action == "dec":
        return -num

for line in f:
    newLine = line.strip("\n").split(" ")
    if newLine[0] not in mainDict:
        mainDict[newLine[0]] = 0
    

highestEver = 0

for line in f:
    newLine = line.split(" ")

    if newLine[5] == ">":
        mainDict[newLine[0]] += action(newLine[1], int(newLine[2]), mainDict[newLine[4]] > int(newLine[6]))

    elif newLine[5] == "<":
        mainDict[newLine[0]] += action(newLine[1], int(newLine[2]), mainDict[newLine[4]] < int(newLine[6]))

    elif newLine[5] == ">=":
        mainDict[newLine[0]] += action(newLine[1], int(newLine[2]), mainDict[newLine[4]] >= int(newLine[6]))

    elif newLine[5] == "<=":
        mainDict[newLine[0]] += action(newLine[1], int(newLine[2]), mainDict[newLine[4]] <= int(newLine[6]))

    elif newLine[5] == "==":
        mainDict[newLine[0]] += action(newLine[1], int(newLine[2]), mainDict[newLine[4]] == int(newLine[6]))

    elif newLine[5] == "!=":
        mainDict[newLine[0]] += action(newLine[1], int(newLine[2]), mainDict[newLine[4]] != int(newLine[6]))

    highestEver = mainDict[newLine[0]] if mainDict[newLine[0]] > highestEver else highestEver

print(mainDict[max(mainDict, key=mainDict.get)])
print(highestEver)