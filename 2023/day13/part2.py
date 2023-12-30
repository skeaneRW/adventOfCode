from functools import cache
inputPath = "2023/day13/input.txt"
testPath = "2023/day13/testInput1.txt"
debugPath = "2023/day13/debug.txt"
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
def checkGroup(group, type, lastScore = 0):
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
        for colIdx in range(len(row)):
            mirrorLen = colIdx if colIdx < midPoint else len(row) - colIdx
            leftSide, rightSide = (row[colIdx - mirrorLen:colIdx], row[colIdx:colIdx + mirrorLen][::-1])
            if colIdx > 0:
                if lastScore == 0 or colIdx != lastIndex:
                    if leftSide == rightSide:
                        rowArr.append(colIdx)
                # we need to exclude the solution to part1 with each iteration. 
                if colIdx == lastIndex and 1 <= lastScore <= 99 and type == 'row':
                    if leftSide == rightSide:
                        rowArr.append(colIdx)
                if colIdx == lastIndex and  lastScore >= 99 and type == 'col':
                    if leftSide == rightSide:
                        rowArr.append(colIdx)
        validColumns.append(rowArr)
    # the common index will be the score.
    def getScore(arr):
        score = 0
        result = set(arr[0])
        for num in arr[1:]:
            result.intersection_update(num)
        if (len(result)):
            if type == 'col':
                score = (list(result)[0])
            else:
                score = (list(result)[0] * 100)
        return score
    score = getScore(validColumns)
    return score

part1Score = []
part2Score = []

# review each grouping and check columns and rows for each grouping
# in order to retrieve the score for each group.
for groupIndex, group in enumerate(groupings):
    lastScore = 0
    if checkGroup(group, 'col') > 0:
        part1Score.append(checkGroup(group, 'col'))
        lastScore = checkGroup(group, 'col')
    # we can use the same function for checking vertically and horizontally by transposing the group.
    transposedGroup = transpose(group)
    if checkGroup(transposedGroup, 'row') > 0:
        part1Score.append(checkGroup(transposedGroup, 'row'))
        lastScore = checkGroup(transposedGroup, 'row')
    
    # once the score has been determined generate all of the alternative
    # variations from the orginal grouping. Go through each variation until
    # we have the new score.
    alternates = getAlternates(group)
    for altIdx, alternate in enumerate(alternates):
        transposedAlternate = transpose(alternate)
        colScore = checkGroup(alternate, 'col', lastScore)    
        if colScore > 0:
            part2Score.append(colScore)
            break
        rowScore = checkGroup(transposedAlternate, 'row', lastScore)
        if rowScore > 0:
            part2Score.append(rowScore)
            break

print(f'part 1 score is {sum(part1Score)}')
print(f'part 2 score is {sum(part2Score)}')
    