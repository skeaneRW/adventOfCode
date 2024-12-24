from collections import deque

testPath = 'adventofcode/2024/day15/testInput.txt'
inputPath = 'adventofcode/2024/day15/input.txt'
chosenPath = inputPath

'''
parse the input file to return a map, rowLen, colLen, robot, and directions
the map should be a key value pair of (x,y) coordinates and the tile type
the rowLen is the length of the row in the map
the colLen is the length of the column in the map
the robot is the starting position of the robot
'''
def parseInput(filename):
    with open(filename) as file:
        input = file.read().splitlines()
    map = {}
    rowLen = len(input[0]) * 2
    colLen = 0
    arrows = ''

    for y in range(len(input)):
        line = input[y]
        if len(line) == 0:
            continue
        elif line[0] == '#':
            x = 0
            colLen += 1
            for ch in line:
                if ch == '#':
                    tile = '##'
                elif ch == 'O':
                    tile = '[]'
                elif ch == '.':
                    tile = '..'
                elif ch == '@':
                    robot = (x,y)
                    tile = '@.'
                map[x,y] = tile[0]
                x += 1
                map[x,y] = tile[1]
                x += 1
        elif line[0] in '<v>^':
            arrows += line
    
    directions = list(arrows)
    return map, rowLen, colLen, robot, directions

'''
if you hit a wall, return the current position of the robot
otherwise update the position of the robot
and any boxes that are in the way
'''
def updateRobotPosition(robot, direction):
    boxes = findBoxesToBeMoved(robot, direction)
    if len(boxes) == 0:
        return robot
    clearMovableParts(boxes)
    robot = moveRobotAndBoxes(boxes, direction)
    return robot

def findBoxesToBeMoved(robot, direction):
    queue = deque([(robot, '@')])
    boxesToBeMoved = {robot: '@'}
    visited = []

    while len(queue) > 0:
        (x, y), _ = queue.popleft()
        coord = (x, y)
        nextX, nextY = move(coord, direction)
        nextSpace = map[nextX, nextY]
        visited.extend((nextX, nextY))

        if nextSpace == '#':
            return {} 
        elif nextSpace == '[':
            if (nextX, nextY) not in visited:
                queue.append(((nextX, nextY), '['))
                boxesToBeMoved[(nextX, nextY)] = '['
                if direction == '^' or direction == 'v':
                    queue.append(((nextX + 1, nextY), ']'))
                    boxesToBeMoved[(nextX + 1, nextY)] = ']'
        elif nextSpace == ']':
            if (nextX, nextY) not in visited:
                queue.append(((nextX, nextY), ']'))
                boxesToBeMoved[(nextX, nextY)] = ']'
                if direction == '^' or direction == 'v':
                    queue.append(((nextX - 1, nextY), '['))
                    boxesToBeMoved[(nextX - 1, nextY)] = '['
    return boxesToBeMoved

def clearMovableParts(boxes):
    for (x,y) in boxes:
        map[x,y] = '.'
    return

def moveRobotAndBoxes(boxes, direction):
    for (x,y), ch in boxes.items():
        coord = (x,y)
        nextX, nextY = move(coord,direction)
        map[nextX, nextY] = ch
        if ch == '@':
            robot = (nextX,nextY)
    return robot

def move(coord,direction):
    x, y = coord
    if direction == '>':
        x += 1
    elif direction == '<':
        x -= 1
    elif direction == '^':
        y -= 1
    else:
        y += 1
    return x, y

def renderMap():
    for y in range(colLen):
        line = ''
        for x in range(rowLen):
            line += map[x,y]
        print(line)
    print()
    return

def moveRobot(robot):
    for dir in directions:
        robot = updateRobotPosition(robot, dir)
        print(f'moving robot {dir}')
        renderMap()
    return

def getTotal():
    total = 0
    for (x,y), ch in map.items():
        if ch == '[':
            coordinate = y * 100 + x
            total += coordinate
    return total

map, rowLen, colLen, robot, directions = parseInput(chosenPath)
moveRobot(robot)
print(getTotal())
