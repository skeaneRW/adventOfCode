from collections import deque
from functools import lru_cache

testPath = './testInput.txt'
inputPath = './input.txt'
chosenPath = inputPath

class Veggie():
    def __init__(self, name, coord):
        self.name = name
        self.coord = coord
        print(f'added {name} at {coord}')
        
       
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

def getPerimeter(patch):
    perimeter = 0
    for coord in patch:
        sidesTouched = 4
        x, y = coord
        up = (x, y-1)
        down = (x, y+1)
        left = (x-1, y)
        right = (x+1, y)
        for coordToTest in [up, down, left, right]:
            if coordToTest in patch:
                sidesTouched -= 1
        perimeter += sidesTouched
    return perimeter

@lru_cache(maxsize=None)
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
        
    
    perimeter = getPerimeter(patch)
    return {'name': veggie, 'area': len(patch), 'perimeter':perimeter, 'patch': patch, }
    

def getPatches():
    previouslyReviewedPatches = []
    patches = []
    for coord in coords:
        print(f'gettingPatch for {coord}')
        if coord not in previouslyReviewedPatches:
            patch = getPatch(coord)
            patches.append(patch)
            previouslyReviewedPatches += patch['patch']
    return patches            

patches = getPatches()
cost = 0
for patch in patches:
    cost += patch['area'] * patch['perimeter']
    print(f'{patch["name"]} has area {patch["area"]} and perimeter {patch["perimeter"]}')
print(f'total cost is {cost}')
