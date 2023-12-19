
import sys
sys.setrecursionlimit(5000)

inputPath = "2023/day10/input.txt"
testPath = "2023/day10/testInput2.txt"
chosenPath = inputPath


directions = [
    dict([('symbol','|'),('up',True),('right',False),('down',True),('left',False),]),
    dict([('symbol','-'),('up',False),('right',True),('down',False),('left',True),]),
    dict([('symbol','L'),('up',True),('right',True),('down',False),('left',False),]),
    dict([('symbol','J'),('up',True),('right',False),('down',False),('left',True),]),
    dict([('symbol','7'),('up',False),('right',False),('down',True),('left',True),]),
    dict([('symbol','F'),('up',False),('right',True),('down',True),('left',False),]),
    dict([('symbol','.'),('up',False),('right',False),('down',False),('left',False),]),
    dict([('symbol','S'),('up',False),('right',False),('down',False),('left',False),])
]

def parseInput(path):
    result = []
    file = open(path, 'r')
    for index, line in enumerate(file.readlines()):
        line = line.replace('\n', '')
        line = [char for char in line]
        lineLen = len(line) -1
        lineWid = index
        result.append(line)

    return [result, lineLen, lineWid]

def getStartingPosition(grid):
    for index, line in enumerate(grid):
        posWid = 0
        if line.__contains__('S'):
            posWid = index
            posLen = [index for index, char in enumerate(line) if char == 'S'][0]
            return (posWid, posLen)

def getSymbol(coordinate):
    for index, row in enumerate(grid):
        if index == coordinate[0]:
            return(row[coordinate[1]])

def isValid(symbol, direction):
    symbolDirections = [dict for dict in directions if dict.get('symbol') == symbol]
    return(symbolDirections[0].get(direction))


def getEntryWays(startingPoint):
    # print(startingPoint)
    # potential entryways are ordered in this array as up, right, down, left
    potentialEntryWays = [
        (startingPoint[0] - 1, startingPoint[1]),
        (startingPoint[0], startingPoint[1] + 1),
        (startingPoint[0] + 1, startingPoint[1]),
        (startingPoint[0], startingPoint[1] - 1),
    ]
    boundEntryWays = [
        coord 
        if (0 <= coord[0] <= gridSize[1] and 0 <= coord[1] <= gridSize[0]) 
        else (startingPoint) 
        for coord in potentialEntryWays
    ]
    dlur = ['down', 'left', 'up', 'right']
    validCoordinates = []
    for index, entry in enumerate(boundEntryWays):
        symbol = getSymbol(entry)
        if(isValid(symbol, dlur[index])):
            validCoordinates.append(entry)
    return(validCoordinates)

def mapPipePaths(entryWays):
    def getNextDir(symbol, prevDir):
        usedConnection = ''
        match prevDir:
            case 'up':
                usedConnection = 'down'
            case 'right':
                usedConnection = 'left'
            case 'down':
                usedConnection = 'up'
            case 'left':
                usedConnection = 'right'
        symbolDirections = [dict for dict in directions if dict.get('symbol') == symbol][0]
        directionList = list(symbolDirections.items())
        return [dir[0] for dir in directionList if dir[1] == True and dir[0] != usedConnection][0]

    def getNextCoord(nextDir, lastCoord):
        coord = lastCoord
        if nextDir == 'up':
            coord = (lastCoord[0] - 1, lastCoord[1])
        if nextDir == 'right':
            coord = (lastCoord[0], lastCoord[1] + 1)
        if nextDir == 'down':
            coord = (lastCoord[0] + 1, lastCoord[1])
        if nextDir == 'left':
            coord = (lastCoord[0], lastCoord[1] - 1)
        return coord

    def makePath(arr, entry):
        result = arr
        if len(result) == 1:
            result.append(entry)

        # get the last two coordinates from the result
        lastCoord = (result[-1:][0])
        lastCoords = (result[-2:])
        # figure out the direction that was travelled based on those coordinates
        prevDir = '?'
        if (lastCoords[1][0] - lastCoords[0][0] == -1):
            prevDir = 'up'
        if (lastCoords[1][1] - lastCoords[0][1] == 1):
            prevDir = 'right'
        if (lastCoords[1][0] - lastCoords[0][0] == 1):
            prevDir = 'down'
        if (lastCoords[1][1] - lastCoords[0][1] == -1):
            prevDir = 'left'
        
        # get the symbol for the last coordinate
        lastSymbol = getSymbol(lastCoord)
        
        # based on the symbol, what's the next direction?
        nextDir = getNextDir(lastSymbol, prevDir)

        # based on the next direction, what's the next coordinate?
        nextCoord = getNextCoord(nextDir, lastCoord)
        # append the next coordinate and return that result
        result.append(nextCoord)
        return(result)

    def isMidPoint(path1, path2):
        pipeLen = len(path1) - 1
        return path1[pipeLen] == path2[pipeLen]
    
    path1 = [startingPoint]
    path2 = [startingPoint]
    
    i = 1
    midPoint = False
    
    while not midPoint:
        i = i + 1
        for index, entry in enumerate(entryWays):
            if index == 0:
                path1 = (makePath(path1, entry))
            if index == 1:
                path2 = (makePath(path2, entry))
        if isMidPoint(path1, path2):
            midPoint = True
            joinedPaths = path1 + path2
            result = []
            [result.append(coord) for coord in joinedPaths if coord not in result]
            return result
        

def visualizePipes(grid):
    for line in grid:
        for index, char in enumerate(line):
            if char == 'F':
                line[index] = '┌'
            if char == '7':
                line[index] = '┐'
            if char == 'J':
                line[index] = '┘'
            if char == 'L':
                line[index] = '└'

        line = ''.join(line)
        print(line)

def replaceDots(grid):
    #replace the starting point symbol with the correct symbol.
    def fixS():
        newS = sorted([(startingPoint[0] - coord[0], startingPoint[1] - coord[1]) for coord in entryWays])
        print(newS)
        sSymbol = ''
        if newS == [(-1, 0), (0, -1)]:
            sSymbol = 'F'
        if newS == [(-1, 0), (0, 1)]:
            sSymbol = '7'
        if newS == [(1, 0), (0, 1)]:
            sSymbol = 'J'
        if newS == [(1, 0), (0, -1)]:
            sSymbol = 'L'
        if newS == [(-1, 0), (1, 0)]:
            sSymbol = '|'
        if newS == [(0, -1), (0, 1)]:
            sSymbol = '-'
        return sSymbol
    
    for line in grid:
        for index, char in enumerate(line):
            if char == 'S':
                line[index] = fixS()

    # change all the fake pipes to dots.
    def fixFakePipes():
        for row, line in enumerate(grid):
            for col, char in enumerate(line):
                if char != '.':
                    coord = (row, col)
                    if not mappedPath.__contains__(coord):
                        line[col] = '.'
    # edge dots should be changed to an 'O'
    def fixEdgeDots():
        for row, line in enumerate(grid):
            for col, char in enumerate(line):
                if char == '.' and (row == 0 or row == gridSize[1]):
                    line[col] = 'O'
                if char == '.' and (col == 0 or col == gridSize[0]):
                    line[col] = 'O'

    def replaceDotsByRow():
        for rowIndex, line in enumerate(grid):
            print(f'reviewing line # {rowIndex}')
            isInside = True
            storedCorner = []
            positions = []
            for index, char in enumerate(line):
                if isInside:
                    pos = 'O'
                else:
                    pos = 'I'
                if char == '|':
                    print(f'at index: {index} ({char} is {pos})')
                    isInside = not isInside
                if ('F', '7', 'L','J').__contains__(char):
                    print(f'{char} is a corner piece')
                    storedCorner.append(char)
                    if len(storedCorner) == 2:
                        print(sorted(storedCorner))
                        if sorted(storedCorner) == sorted(['F','J']) or sorted(storedCorner) == sorted(['7','L']):
                            isInside = not isInside
                        storedCorner = []    
                positions.append(pos)
            for index, char in enumerate(line):
                if char == '.':
                    line[index] = positions[index]
        print(positions)
        print(line)
        return line

                        
    def countRemainingDots():
        arr = []
        for line in grid:
            for char in line:
                if char == 'I':
                    arr.append(char)
        dotCount = len(arr)
        return(dotCount)
    fixFakePipes()
    fixEdgeDots()
    replaceDotsByRow()
    print(f'there are {countRemainingDots()} remaining dots.')
    return(grid)

input = parseInput(chosenPath) 
grid = input[0]
gridSize = (input[1], input[2])
startingPoint = getStartingPosition(grid)
entryWays = getEntryWays(startingPoint)
mappedPath = mapPipePaths(entryWays)

newGrid = replaceDots(grid)
visualizePipes(newGrid)

