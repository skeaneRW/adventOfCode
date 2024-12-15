from collections import deque
testPath = 'adventofcode/2024/day12/testInput.txt'
inputPath = 'adventofcode/2024/day12/input.txt'
chosenPath = inputPath
       
def getMap(input):
    file = open(input, 'r')
    rows = [line.replace('\n','') for line in file.readlines()]
    gardenMap = {}
    rowLength = len(rows[0])
    colLength = len(rows)
    for x, row in enumerate(rows):
        cols = list(row.strip())
        for y, val in enumerate(cols):
            gardenMap[(y,x)] = val
    return gardenMap, rowLength, colLength

map, maxRow, maxCol = getMap(chosenPath)
coords = list(map.keys())

def isValidCoord(coord):
    x, y = coord
    if x < 0 or y < 0:
        return False
    if x >= maxRow or y >= maxCol:
        return False
    return True

def getCoordValue(coord):
    x, y = coord
    return map[(x,y)]

def getCorners(patch):
    corners = 0
    for coord in patch:
        x, y = coord
        up = (x, y-1)
        down = (x, y+1)
        left = (x-1, y)
        right = (x+1, y)
        upLeft = (x-1, y-1)
        upRight = (x+1, y-1)
        downLeft = (x-1, y+1)
        downRight = (x+1, y+1)
        cornerConditions= [
            up not in patch and left not in patch,
            up not in patch and right not in patch,
            down not in patch and left not in patch,
            down not in patch and right not in patch,
            up in patch and left in patch and upLeft not in patch,
            up in patch and right in patch and upRight not in patch,
            down in patch and left in patch and downLeft not in patch,
            down in patch and right in patch and downRight not in patch,
        ]
        for condition in cornerConditions:
            if condition:
                corners += 1
    return corners

def getPatch(coord):
    veggie = getCoordValue(coord)
    notReviewed = deque([coord])
    patch = set()
    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    while len(notReviewed) > 0:
        thisCoord = notReviewed.popleft()
        if thisCoord in patch: # we dont want to review the same coord twice
            continue
        patch.add(thisCoord)
        x, y = thisCoord
        for xDirection, yDirection in directions:
            newCoord = (x + xDirection, y + yDirection)
            if isValidCoord(newCoord) and newCoord not in patch:
                if getCoordValue(newCoord) == veggie:
                    notReviewed.append(newCoord)
        
    
    corners = getCorners(patch)
    return {'name': veggie, 'area': len(patch), 'corners':corners, 'patch': patch, }
    

def getPatches():
    previouslyReviewedPatches = []
    patches = []
    for coord in coords:
        if coord not in previouslyReviewedPatches:
            patch = getPatch(coord)
            patches.append(patch)
            previouslyReviewedPatches += patch['patch']
    return patches            

patches = getPatches()
cost = 0
for patch in patches:
    cost += patch['area'] * patch['corners']
    print(f'{patch["name"]} has area {patch["area"]} and {patch["corners"]} sides.')
print(f'total cost is {cost}')
