testPath = 'adventofcode/2024/day15/testInput.txt'
inputPath = 'adventofcode/2024/day15/input.txt'
chosenPath = testPath

def parseInput(path):
    file = open(path, 'r')
    lines = file.readlines()
    map = []
    directions = []
    arr = map
    for line in lines:
        line = line.strip()
        if line != '':
            arr.append(list(line)) if arr == map else arr.extend(line)
        if line == '':
            arr = directions
    return map, directions

map, directions = parseInput(chosenPath)
mapLength = len(map)
mapWidth = len(map[0])

def getMapObjects(map):
    mapObjects = []
    for y in range(len(map)):
        for i, x in enumerate(range(len(map[y]))):
            mapObj = {}
            mapObj['coord'] = (x, y)
            mapObj['type'] = map[y][x]
            mapObj['index'] = y * len(map[y]) + i
            mapObjects.append(mapObj)
    return mapObjects


'''
'#' = wall
'.' = open space
'@' = robot
'O' = box
'''

def renderMap(map):
    for y in range(mapLength):
        for x in range(mapWidth):
            print([obj['type'] for obj in map if obj['coord'] == (x, y)][0], end='')
        print('')
    print()

def getIndex(map, coord):
    return [obj['index'] for obj in map if obj['coord'] == coord]

def getColumn(map, y):
    return [obj for obj in map if obj['coord'][0] == y]

def getRow(map, x):
    return [obj for obj in map if obj['coord'][1] == x]


def getNextSpace(map, dir, startingIndex):
    if dir == 'v':
        nextSpace = [obj for obj in map if obj['index'] == startingIndex + mapWidth][0]
        nextIndex = nextSpace['index']
    if dir == '^':
        nextSpace = [obj for obj in map if obj['index'] == startingIndex - mapWidth][0]
        nextIndex = nextSpace['index']
    if dir == '>':
        nextSpace = [obj for obj in map if obj['index'] == startingIndex + 1][0]
        nextIndex = nextSpace['index']
    if dir == '<':
        nextSpace = [obj for obj in map if obj['index'] == startingIndex - 1][0]
        nextIndex = nextSpace['index']
    return nextSpace, nextIndex

def getSegment(map, dir, startingCoord):
    x, y = startingCoord
    if dir == 'v':
        segment = [obj['type'] for obj in getColumn(map, x)][y+1:]
        indexOfHash = segment.index('#')
        segment = segment[:indexOfHash]
    if dir == '^':
        segment = [obj['type'] for obj in getColumn(map, x)][0:y][::-1]
        indexOfHash = segment.index('#')
        segment = segment[:indexOfHash]
    if dir == '>':
        segment = [obj['type'] for obj in getRow(map, y)][x+1:]
        indexOfHash = segment.index('#')
        segment = segment[:indexOfHash]
    if dir == '<':
        segment = [obj['type'] for obj in getRow(map, y)][0:x][::-1]
        indexOfHash = segment.index('#')
        segment = segment[:indexOfHash]
    return segment

def moveRobot(dir, map):
    print(f"moving robot {dir}")
    currentRobot = [obj for obj in map if obj['type'] == '@'][0]
    currentIndex = currentRobot['index']

    nextSpace, nextIndex = getNextSpace(map, dir, currentIndex)
    segment = getSegment(map, dir, currentRobot['coord'])
    
    if len(segment) == 0 or '.' not in segment:
        return map
    
    if segment[0] == '.':
        nextSpace['type'] = '@'
        currentRobot['type'] = '.'
        map[nextIndex] = nextSpace
        map[currentIndex] = currentRobot
        return map
    else:
        map = pushBoxes(dir, map, segment)
        return map

def pushBoxes(dir, map, segment):
    indexOfDot = segment.index('.') + 1
    clippedSegment = segment[:indexOfDot]
    currentRobot = [obj for obj in map if obj['type'] == '@'][0]
    currentIndex = currentRobot['index']
    boxSpace, boxIndex = getNextSpace(map, dir, currentIndex)
    
    currentRobot['type'] = '.'
    map[currentIndex] = currentRobot
    boxSpace['type'] = '@'
    map[boxIndex] = boxSpace

    numberOfBoxes = len([space for space in clippedSegment if space == 'O'])
    for box in range(numberOfBoxes):
        nextSpace, nextIndex = getNextSpace(map, dir, boxIndex)
        nextSpace['type'] = 'O'
        map[nextIndex] = nextSpace
        boxIndex = nextIndex
    return map

mapObjects = getMapObjects(map)
def followPath(directions, map):
    for dir in directions:
        map = moveRobot(dir, map)
    return map

def scoreBoxes(map):
    boxes = [obj for obj in map if obj['type'] == 'O']
    sum = 0
    for box in boxes:
        coord = box['coord']
        x, y = coord
        sum += (100 * y) + x
    return sum

orderedBoxes = followPath(directions, mapObjects)
print(scoreBoxes(orderedBoxes))