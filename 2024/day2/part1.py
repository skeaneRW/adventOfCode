testPath = "./testInput.txt"
inputPath = "./input.txt"
chosenPath = inputPath

def parseInput(path):
    file = open(path, "r")
    result = []
    for line in file.readlines():
        row = line.replace('\n', '').split(' ')
        result.append(list(map(int, row)))
    return result

reports = parseInput(chosenPath)

def getLevels(reports):
    result = []
    for row in reports:
        list = []
        for i in range(len(row)):
            if i != len(row) - 1:
                list.append(row[i] - row[i + 1])
        result.append(list)
    return result

levels = (getLevels(reports))

def checkSafety(levels):
    safeLevels = []
    for row in levels:
        if all(i > 0 and i <= 3 for i in row):
            safeLevels.append(row)
        elif all(i < 0 and i >= -3 for i in row):
            safeLevels.append(row)
    return safeLevels

safeLevels = checkSafety(levels)
print(len(safeLevels))