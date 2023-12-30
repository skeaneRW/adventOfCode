from functools import cache
inputPath = "2023/day13/input.txt"
testPath = "2023/day13/testInput1.txt"
chosenPath = inputPath

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

def getAlternates(group):
    alternates = []
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
    return alternates
def transpose(group):
    transposedGroup = [[group[row][col] for row in range(len(group))] for col in range(len(group[0]))]
    transposedGroup = [''.join(row) for row in transposedGroup]
    return transposedGroup

groupings = parseInput(chosenPath)
# review columns to see if any adjacent columns mirror one another.
def checkColumns(group, lastScore = 0):
    lastIndex = None
    if lastScore > 0:
        lastIndex = lastScore 
    if lastScore > 99:
        lastIndex = lastScore / 100
    validColumns = []
    midPoint = len(group[0])/2
    #accumulate any indexes where the left side and the right side (mirrored) match
    for row in group:
        rowArr = []
        for colIdx, char in enumerate(row):
            mirrorLen = colIdx if colIdx < midPoint else len(row) - colIdx
            leftSide, rightSide = (row[colIdx - mirrorLen:colIdx], row[colIdx:colIdx + mirrorLen][::-1])
            if colIdx > 0 and colIdx != lastIndex:
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
    return score

# review rows to see if any adjacent rows mirror one another.
# we can use the same logic as we did for columns if we transpose the group.
def checkRows(group, lastScore = 0):
    targetIndex = checkColumns(group, lastScore)
    return targetIndex * 100
part1Score = []
part2Score = []

# review each grouping and check columns and rows for each grouping
# in order to retrieve the score for each group.
for groupIndex, group in enumerate(groupings):
    print(f'reviewing group # {groupIndex}')
    transposedGroup = transpose(group)
    lastScore = 0
    if checkColumns(group) != 0:
        part1Score.append(checkColumns(group))
        lastScore = checkColumns(group)
    if checkRows(transposedGroup) != 0:
        part1Score.append(checkRows(transposedGroup))
        lastScore = checkRows(transposedGroup)
    
    # once the score has been determined generate all of the alternative
    # variations from the orginal grouping. Go through each variation until
    # we have the new score.
    alternates = getAlternates(group)
    for altIdx, alternate in enumerate(alternates):
        
        targetRange = (0, 5)
        betweenCondition = targetRange[0] <= altIdx <= targetRange[1]
        if betweenCondition:
            print(f'variation # {altIdx}')
        if betweenCondition:
            for row in alternate:
                print(row)
            print('-'*20)
        transposedAlternate = transpose(alternate)
        # alternate scores shouln't be zero and shouldn't be equal to the last score.
        def isValid(type):
            if type == 'column':
                if checkColumns(alternate, lastScore) == 0 or checkColumns(alternate, lastScore) == lastScore:
                    return False
                return True
            if type == 'row':
                if checkRows(transposedAlternate, lastScore) == 0 or checkRows(transposedAlternate, lastScore) == lastScore:
                    return False
                return True
        if isValid('column'):
            part2Score.append(checkColumns(alternate, lastScore))
            break
        if isValid('row'):
            part2Score.append(checkRows(transposedAlternate, lastScore))
            break

    print(f'part 1 score is {sum(part1Score)}')
    print('len', len(part1Score), part1Score)
    print(f'part 2 score is {sum(part2Score)}')
    print('len', len(part2Score), part2Score)
    