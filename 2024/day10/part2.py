import itertools

testPath = './testInput.txt'
inputPath = './input.txt'
chosenPath = inputPath

def getTrailmap(path):
    file = open(path, 'r')
    rows = list(file.readlines())
    map = {}
    for x, row in enumerate(rows):
        cols = list(row.strip())
        for y, val in enumerate(cols):
            map[(x,y)] = int(val)

    rowLength = len(rows[0].strip())
    return map, rowLength

trailMap, mapLen = getTrailmap(chosenPath)

def getEndpoints(map):
    count = 0
    for key in map:
        if map[key] == 9:
            count += 1
    return count

def getStartpoint(map):
    count = 0
    for key in map:
        if map[key] == 0:
            count += 1
    return count

startpoints = getStartpoint(trailMap)
endpoints = getEndpoints(trailMap)

def getCoords(map, value):
    coords = []
    for key in map:
        if map[key] == value:
            coords.append(key)
    return coords


endPoints = getCoords(trailMap, 9)
def getTrailCount(map, endPoints):
    def checkDirection (coord, direction):
        y, x = coord
        if direction == 'up':
            y -= 1
        if direction == 'down':
            y += 1
        if direction == 'left':
            x -= 1
        if direction == 'right':
            x += 1
        if x < 0 or y < 0:
            return None
        if x >= mapLen or y >= mapLen:
            return None
        return (y, x)
    
    def getPaths():
        values = ['left', 'right', 'up', 'down']
        combinations = list(itertools.product(values, repeat=9))
        return combinations
    
    possiblePaths = getPaths()
    validCombos = []

    def checkTrailPath(coord, directions):
        startingCoord = coord
        for direction in directions:
            target = map[coord] - 1
            nextCoord = checkDirection(coord, direction)
            if nextCoord is None or map[nextCoord] != target:
                return False
            if map[nextCoord] == 0 and target == 0:
                validCombos.append(f'{startingCoord}-{nextCoord}')
                return True
            coord = nextCoord
        return False
    
    for point in endPoints:
        for n, directions in enumerate(possiblePaths):
            checkTrailPath(point, directions)
    # in part 1, we elimintated duplicates.
    # in part 2, we keep the duplicates -- those represent all
    # possible paths            
    return len(validCombos)


arr = getTrailCount(trailMap, endPoints)
print(arr)
