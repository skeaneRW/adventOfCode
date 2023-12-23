
inputPath = "2023/day11/input.txt"
testPath = "2023/day11/testInput1.txt"
chosenPath = inputPath

def parseInput (path):
    print('parsing input')
    result = []
    file = open(path, 'r')
    for line in file:
        line = list(line.replace('\n',''))
        result.append(line)
    return result

def getExpandingColumns(grid):
    print('inserting columns')
    goodColumns = []
    for rowIndex, row in enumerate(grid):
        currentRow = rowIndex
        for colIndex, char in enumerate(row):
            if currentRow == 0:
                if char == '#':
                    goodColumns.append('#')
                else:
                    goodColumns.append(colIndex)
            else:
                if char == '#' or goodColumns[colIndex] == '#':
                    goodColumns[colIndex] = '#'
                else:
                    goodColumns[colIndex] = colIndex
    expandingColumns = [x for x in goodColumns if x != '#']
    return(expandingColumns)

def getExpandingRows(grid):
    print('identify expanding rows')
    expandingRows = []
    for index,row in enumerate(grid):
        if len([x for x in row if x == '#']) == 0:
            expandingRows.append(index)
    return expandingRows
            

def replaceHash(grid):
    print('replacing hashes')
    hashCount = 0
    for row in grid:
        for index, char in enumerate(row):
            if char == '#':
                row[index] = str(hashCount)
                hashCount = hashCount + 1

def getPairings(grid):
    print('getting pairings')
    gridCopy = grid.copy()
    for index, line in enumerate(gridCopy):
        gridCopy[index] = [x for x in line if x != '.']
    hashNums = [int(x) for x in sum(gridCopy, [])]
    pairings = []
    for numA in hashNums:
        for numB in hashNums:
            if numA != numB:
                nums = sorted([numA, numB])
                if not pairings.__contains__(nums):
                    pairings.append(nums)
    # cleanPairings = []
    # [cleanPairings.append(x) for x in pairings if not cleanPairings.__contains__(x)]
    print('pairings complete')
    return(pairings)
    
def pairingsToCoord(pairings, expansionSize):
    if expansionSize > 1:
        expansionSize = expansionSize - 1
    print('converting pairings to coordinates')
    definedCoords = []
    def getCoord(num):
        
        existingCoord = [x for index, x in enumerate(definedCoords) if x['num'] == num]
        if len(existingCoord) > 0:
            return(existingCoord[0]['coord'])
        
        for rowIndex, row in enumerate(grid):
            rowModifier = 0
            for expandedRow in expandingRows:
                if range(0, rowIndex).__contains__(expandedRow):
                    rowModifier = rowModifier + 1 
            rowInsertions = rowModifier * expansionSize
            for colIndex, char in enumerate(row):
                colModifier = 0
                if char == str(num):
                    for expandedColumn in expandingColumns:
                        if range(0, colIndex).__contains__(expandedColumn):
                            colModifier = colModifier + 1
                    colInsertions = colModifier * expansionSize     
                    coord = (rowIndex + rowInsertions, colIndex + colInsertions)
                    definedCoords.append({'num': num, 'coord':coord})
                    return (coord)
    result = []
    for pair in pairings:
        result.append([getCoord(pair[0]), getCoord(pair[1])])
    return(result)
        
def getDistances(coords):
    print('calculating distances')
    def getDistance(set):
        x = sorted([set[0][0], set[1][0]])
        y = sorted([set[0][1], set[1][1]])
        distance = ((x[1] - x[0]) + (y[1] - y[0]))
        return distance
    
    distances = []
    for set in coords:
        print(set)
        dist = getDistance(set)
        distances.append(dist)
    return distances

grid = parseInput(chosenPath)
expandingColumns = getExpandingColumns(grid)
expandingRows = getExpandingRows(grid)
replaceHash(grid)
pairings = getPairings(grid)
coords = pairingsToCoord(pairings, 1000000)
'''
on test:
1 =     374       374         off by 0
10 =    1030      1112        off by 82
100 =   8410      8492        off by 82
'''
distances = getDistances(coords)
print(sum(distances))

def visualize(grid):
    for row in grid:
        print(''.join(row))

visualize(grid)