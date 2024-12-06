import re
testPath = './testInput.txt'
inputPath = './input.txt'
chosenPath = inputPath

def getGrid(path):
    file = open(path, 'r')
    grid = []
    for line in file:
        line = line.strip('\n')
        grid.append(list(line))
    return grid

grid = getGrid(chosenPath)

def getDirections(direction, grid):
    result = []
    if direction == 'horizontal':
        for row in grid:
            result.append(''.join(row))
    elif direction == 'vertical':
        for i in range(len(grid[0])):
            column = []
            for row in grid:
                column.append(row[i])
            result.append(''.join(column))
    
    elif direction == 'postiveDiagonal':
        def getDiagonalString(startingCol, startingRow, endingCol):
            diagonal = []
            for i in range(endingCol - startingCol + 1):
                diagonal.append(grid[startingRow + i][startingCol + i])
            return ''.join(diagonal)
        
        for row in range(len(grid)):
            if row == 0:
                for col in range(len(grid[0])):    
                    print(f'need to get diagnol string starting on: col{col},row{row} and ending on {len(grid[0])-1},{len(grid)-col-1}:')
                    print(getDiagonalString(col, row, len(grid[0])-1))
                    result.append(getDiagonalString(col, row, len(grid[0])-1))
            else:
                result.append(getDiagonalString(0, row, len(grid[0])-1-row))
    elif direction == 'negativeDiagonal':
        
        def getString(startingCol, startingRow, endingCol, endingRow):
            diagonal = []
            stringLen = startingCol - endingCol + 1
            if endingCol == 0:
                for i in range(stringLen):
                    diagonal.append(grid[i][stringLen - 1 - i])
                return ''.join(diagonal)
            else:
                for i in range(stringLen):
                    diagonal.append(grid[startingRow + i][startingCol - i])
                return ''.join(diagonal)
        
        for row in range(len(grid)):
            if row == 0:
                for col in range(len(grid[0])):
                    startingCol = col
                    startingRow = row
                    endingCol = 0
                    endingRow = col
                    string = getString(startingCol, startingRow, endingCol, endingRow)
                    result.append(string)
            else:
                startingCol = len(grid[0]) - 1
                startingRow = row
                endingCol = row
                endingRow = len(grid) - 1
                string = getString(startingCol, startingRow, endingCol, endingRow)
                result.append(string)
    return result

horizontalStrings = getDirections('horizontal', grid)
verticalStrings = getDirections('vertical', grid)
positiveDiagonalStrings = getDirections('postiveDiagonal', grid)
negativeDiagonalStrings = getDirections('negativeDiagonal', grid)

combinedStrings = horizontalStrings + verticalStrings + positiveDiagonalStrings + negativeDiagonalStrings

print(negativeDiagonalStrings)

def getMatches(pattern, arr):
    count = 0
    for string in arr:
        print(f'checking {string}')
        matches = re.findall(pattern, string) + re.findall(pattern[::-1], string)
        print(f'found {len(matches)} in {string}')
        count += len(matches)
    return count

print(getMatches('XMAS', combinedStrings))