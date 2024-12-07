testPath = './testInput.txt'
inputPath = './input.txt'
chosenPath = inputPath

def getBigGrid(path):
    file = open(path, 'r')
    grid = []
    for line in file:
        line = line.strip('\n')
        grid.append(list(line))
    return grid

bigGrid = getBigGrid(chosenPath)

def getMiniGrid(startingPosition, grid):
    miniGrid = []
    for row in range(3):
        miniGrid.append(grid[startingPosition[0] + row][startingPosition[1]:startingPosition[1] + 3])
    return miniGrid

def findXMas(grid):
    debugRow = 2
    debugCol = 3
    def isAGoodMiniGrid(grid):
        checkCoord = lambda coord, char: grid[coord[0]][coord[1]] == char
        topToBottomDiagnol = (checkCoord((0,0), 'M') and checkCoord((2,2), 'S')) or (checkCoord((0,0), 'S') and checkCoord((2,2), 'M'))
        centerSpace = checkCoord((1,1), 'A')
        bottomToTopDiagnol = (checkCoord((2,0), 'M') and checkCoord((0,2), 'S')) or (checkCoord((2,0), 'S') and checkCoord((0,2), 'M'))
        if row == debugRow and col == debugCol:
            print(f'topToBottomDiagnol: {topToBottomDiagnol}, centerSpace: {centerSpace}, bottomToTopDiagnol: {bottomToTopDiagnol}')
            for line in grid:
                print(line)
            if not topToBottomDiagnol:
                print(f'valid solutions for topToBottomDiagnol:')
                print(f"grid[0][0]= 'M', grid[2][2]= 'S'")
                print(f"grid[0][0]= 'S', grid[2][0]= 'M'")
                print(f'grid[0][0]: {grid[0][0]}, grid[2][2]: {grid[2][2]}')
                print(f'grid[0][0]: {grid[0][0]}, grid[2][0]: {grid[2][0]}')
            if not centerSpace:
                print(f'grid[1][1]: {grid[1][1]}')
            if not bottomToTopDiagnol:
                print(f'grid[2][0]: {grid[2][0]}, grid[0][2]: {grid[0][2]}')
                print(f'grid[2][0]: {grid[2][0]}, grid[0][2]: {grid[0][2]}')
        return topToBottomDiagnol and centerSpace and bottomToTopDiagnol
    count = 0
    for row in range(len(grid) - 2):
        for col in range(len(grid[0]) - 2):
            miniGrid = getMiniGrid((row, col), grid)
            if isAGoodMiniGrid(miniGrid):
                print(f'grid[{row}][{col}] is a good grid')
                count += 1
            if row == debugRow and col == debugCol:
                print(f'evaluating grid[{row}][{col}]:')

                    

    print(f'found {count} good mini grids')
    return count
            
findXMas(bigGrid)