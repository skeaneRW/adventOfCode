from functools import cache
inputPath = "2023/day13/input.txt"
testPath = "2023/day13/testInput1.txt"
chosenPath = testPath

def parseInput(path):
    result = []
    arr = []    
    file = open(chosenPath, 'r')
    for line in file.readlines():
        line = line.replace('\n','')
        arr.append(line)
        if len(line) == 0:
            arr = [x for x in arr if x != '']
            result.append(arr)
            arr = []
    result.append(arr)
    return result

groupings = parseInput(chosenPath)
alternates = []
# review columns to see if any adjacent columns mirror one another.
def checkColumns(group, setAlternates):
    validColumns = []
    midPoint = len(group[0])/2
    #accumulate any indexes where the left side and the right side (mirrored) match
    for row in group:
        rowArr = []
        for colIdx, char in enumerate(row):
            mirrorLen = colIdx if colIdx < midPoint else len(row) - colIdx
            leftSide, rightSide = (row[colIdx - mirrorLen:colIdx], row[colIdx:colIdx + mirrorLen][::-1])
            if colIdx > 0:
                if leftSide == rightSide:
                    rowArr.append(colIdx)
        validColumns.append(rowArr)
    # the common index will be the score.
    def getScore(arr):
        result = set(arr[0])
        for num in arr[1:]:
            result.intersection_update(num)
        if (len(result)):
            return (list(result)[0])
        else:
            return 0
    score = getScore(validColumns)
    def getAlternates(group):
        groupCopy = group[:]
        for rowIdx, row in enumerate(groupCopy):
            for colIdx in range(len(row)):
                char = group[rowIdx][colIdx]
                oppositeChar = '.' if char == '#' else '#'
                string_list = list(groupCopy[rowIdx])
                string_list[colIdx] = oppositeChar
                newString = ''.join(string_list)
                groupCopy[rowIdx] = newString
                alternates.append(groupCopy)
                groupCopy = group[:]
    if setAlternates:            
        getAlternates(group)
    return score

# review rows to see if any adjacent rows mirror one another.
# we can use the same logic as we did for columns if we transpose the group.
def checkRows(group):
    transposedGroup = [[group[row][col] for row in range(len(group))] for col in range(len(group[0]))]
    transposedGroup = [''.join(row) for row in transposedGroup]
    targetIndex = checkColumns(transposedGroup)
    return targetIndex * 100
score = 0
for groupIndex, group in enumerate(groupings):
    print(f'reviewing group # {groupIndex}')
    score += checkColumns(group, True)
    for altIdx, alternate in enumerate(alternates):
        if altIdx < 5:
            print(f'alternate index {altIdx}')
            print(group)
            for row in alternate:
                print((' '*10),row)
            altResult = (checkColumns(alternate, False))
            print(altResult)
    #score += checkRows(group)
    print(f'score is {score}')

    