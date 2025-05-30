import time
testPath = 'adventofcode/2024/day14/testInput.txt'
inputPath = 'adventofcode/2024/day14/input.txt'
chosenPath = inputPath

def getRobots(input):
    file = open(input, 'r')
    lines = [line.replace('\n','') for line in file.readlines()]
    results = []
    for line in lines:
        robot = {}
        line = line.replace('p=','')
        line = line.replace('v=','')
        line = line.split(' ')
        postition = line[0].split(',')
        velocity = line[1].split(',')
        robot['position'] = (int(postition[0]), int(postition[1]))
        robot['velocity'] = (int(velocity[0]), int(velocity[1]))
        results.append(robot)
    return results

def updatePosition (robot, seconds):
    x, y = robot['position']
    xV, yV = robot['velocity']
    for i in range(seconds):
        x += xV
        y += yV
        if x > maxWidth -1:
            x = x - maxWidth
        elif x < 0:
            x = maxWidth + x
        if y > maxHeight -1:
            y = y - maxHeight
        elif y < 0:
            y = maxHeight + y
        
    updatedPosition = (x, y)
    return {'position': updatedPosition, 'velocity': robot['velocity']}

def isMapTreeShaped(map):
    for i, row in enumerate(map):
        stringRow = ''.join(row)
        if stringRow.__contains__('##########'):
            return True
    return False

def updatePositions(robots, seconds):
    for i in range(seconds):
        updatedRobots = []
        for robot in robots:
            updatedRobot = updatePosition(robot, 1)
            updatedRobots.append(updatedRobot)

        drawnMap = renderMap(updatedRobots, i)
        isTree = isMapTreeShaped(drawnMap)
        if isTree:
            print(f'tree at {i + 1} MIGHT BE TREE-SHAPED')
        robots = updatedRobots
    return updatedRobots

def renderMap(robots, sec):
    # print(f'{"-"*35} {sec + 1} rendered below: {"-"*35} ')
    map = [[' ' for i in range(maxWidth)] for j in range(maxHeight)]
    for robot in robots:
        x, y = robot['position']
        map[y][x] = '#'
    return map

def getRobotQuadrants(robots):
    quadrant1 = []
    quadrant2 = []
    quadrant3 = []
    quadrant4 = []
    for robot in robots:
        x, y = robot['position']
        if x < voidColumn and y < voidRow:
            quadrant1.append(robot)
        elif x > voidColumn and y < voidRow:
            quadrant2.append(robot)
        elif x < voidColumn and y > voidRow:
            quadrant3.append(robot)
        elif x > voidColumn and y > voidRow:
            quadrant4.append(robot)
    robotQuadrants = [quadrant1, quadrant2, quadrant3, quadrant4]
    return robotQuadrants

def getProduct(robotQuadrants):
    product = 1
    for quadrant in robotQuadrants:
        product *= len(quadrant)
    return product

maxWidth = 101 if chosenPath == inputPath else 11
maxHeight = 103 if chosenPath == inputPath else 7
voidColumn = maxWidth//2
voidRow = maxHeight//2
seconds = 10000000000

robots = getRobots(chosenPath)
robotsAfterMove = updatePositions(robots, seconds)
quads = getRobotQuadrants(robotsAfterMove)
productOfRobots = getProduct(quads)
print(productOfRobots)
