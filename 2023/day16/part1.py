testPath = '2023/day16/testInput1.txt'
inputPath = '2023/day16/input.txt'
chosenPath = inputPath

def parseInput (path):
    file = open(path, 'r')
    grid = []
    for x, line in enumerate(file):
        line = line.replace('\n','')
        x = []
        for char in line:
            x.append(char)
        grid.append(x)
    return grid

def visualizeGrid(grid, energizedGridAreas):
    for gridArea in energizedGridAreas:
        x, y = gridArea
        grid[x][y] = '#'
    for rowNum, row in enumerate(grid):
        grid[rowNum] = ''.join(row)
    for row in grid:
        print(row)

def createBeam (startX, startY, dir, visitedBeams):
    def getNext(currentX, currentY, dir):
        nextX, nextY = currentX, currentY
        match dir:
            case 'up':
                nextX = currentX - 1
            case 'right':
                nextY = currentY + 1
            case 'down':
                nextX = currentX + 1
            case 'left':
                nextY = currentY - 1
            case _:
                print(f'error : invalid direction: {dir}')
        if 0 <= nextX <= len(grid) - 1 and 0 <= nextY <= len(grid[0]) - 1:
            return nextX, nextY
        else:
            return currentX, currentY 
    beamPath = []
    additionalBeams = []
    if beamPath == []:
        x, y = startX, startY
    while len(beamPath) <= 1 or (x, y) != beamPath[-1]:
        beamPath.append((x, y))
        thisValue = grid[x][y]
        match thisValue:
            case ".":
                x, y = getNext(x, y, dir)
            case "/":
                if dir == 'right':
                    dir = 'up'
                elif dir == 'up':
                    dir = 'right'
                elif dir == 'left':
                    dir = 'down'
                else:
                    dir = 'left'
                x, y = getNext(x, y, dir)
            case "\\":
                if dir == 'right':
                    dir = 'down'
                elif dir == 'down':
                    dir = 'right'
                elif dir == 'left':
                    dir = 'up'
                else:
                    dir = 'left'
                x, y = getNext(x, y, dir)
            case "|":
                if dir in ['up', 'down']:
                    x, y = getNext(x, y, dir)
                else:
                    if (x, y, 'up') not in visitedBeams:
                        additionalBeams.append((x, y, 'up'))
                    if (x, y, 'down') not in visitedBeams:
                        additionalBeams.append((x, y, 'down'))
            case "-":
                if dir in ['left', 'right']:
                    x, y = getNext(x, y, dir)
                else:
                    if (x, y, 'left') not in additionalBeams and (x, y, 'left') not in pendingBeams:
                        additionalBeams.append((x, y, 'left'))
                    if (x, y, 'right') not in additionalBeams and (x, y, 'right') not in pendingBeams:
                        additionalBeams.append((x, y, 'right'))
            case _:
                print(f'unexpected value {thisValue}')
    return(beamPath, additionalBeams)
    

grid = parseInput(chosenPath)
gridAreasCovered = []
pendingBeams = []
visitedBeams = []
beamPath, additionalBeams = createBeam(0,0,'right', visitedBeams)
gridAreasCovered.append(beamPath)
for beam in additionalBeams:
    pendingBeams.append(beam)
count = 0
while len(pendingBeams) > 0:
    x, y, dir = pendingBeams[0]
    beamPath, additionalBeams = createBeam(x, y, dir, visitedBeams)
    gridAreasCovered.append(beamPath)
    for beam in additionalBeams:
        pendingBeams.append(beam)
    visitedBeams.append(pendingBeams[0])
    del pendingBeams[0]
    count += 1

energizedGridAreas = []
for subArr in gridAreasCovered:
    for gridArea in subArr:
        if gridArea not in energizedGridAreas:
            energizedGridAreas.append(gridArea)

visualizeGrid(grid, energizedGridAreas)
print(len(energizedGridAreas))





