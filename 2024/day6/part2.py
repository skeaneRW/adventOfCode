testPath = './testInput.txt'
inputPath = './input.txt'
chosenPath = inputPath
import sys
limit = 10**8
sys.setrecursionlimit(limit)

def getPatrolMap(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        patrolMap = []
        for line in lines:
            line = list(line.strip())
            patrolMap.append(line)
    return patrolMap

def getGuardPosition(patrolMap):
    pattern = '^' or 'v' or '<' or '>'
    for y in range(len(patrolMap)):
        for x in range(len(patrolMap[y])):
            if patrolMap[y][x] == pattern:
                return (x, y)
            
patrolMap = getPatrolMap(chosenPath)
getGuardPosition = getGuardPosition(patrolMap)

objectsEncountered = []
def moveGuard(map, guardPosition, direction, icon, objectsEncountered):
    newPatrolMap = map
    x, y = guardPosition
    def getGuardsNextPosition(guardPosition, travelDirection):
        x, y = guardPosition
        if travelDirection == 'up':
            return (x, y - 1)
        elif travelDirection == 'down':
            return (x, y + 1)
        elif travelDirection == 'left':
            return (x - 1, y)
        elif travelDirection == 'right':
            return (x + 1, y)
    
    def turnGuard(currentDirection):
        if currentDirection == 'up':
            newDirection, newIcon = ('right', '>')
        elif currentDirection == 'right':
            newDirection, newIcon = ('down', 'v')
        elif currentDirection == 'down':
            newDirection, newIcon = ('left', '<')
        elif currentDirection == 'left':
            newDirection, newIcon = ('up', '^')
        return newDirection, newIcon
    
    def isOffMap(nextPosition):
        x, y = nextPosition
        if x < 0 or y < 0 or y >= len(newPatrolMap) or x >= len(newPatrolMap[y]):
            return True
        return False
    
    def isObstacle(nextPosition):
        x, y = nextPosition
        if newPatrolMap[y][x] == '#':
            objectsEncountered.append(nextPosition)
            return True
        return False
    
    def isInfinte(objectsEncountered):
        # if we come against the same object 5 times or more, 
        # then we are in an infinite loop
        arr = []
        for i, object in enumerate(objectsEncountered):
            count = objectsEncountered.count(object)
            arr.append((object, count))
        def removeDuplicates(duplicate):
            final_list = []
            for num in duplicate:
                if num not in final_list:
                    final_list.append(num)
            return final_list
        arr = removeDuplicates(arr)
        result = False
        for i, object in enumerate(arr):
            if object[1] > 4:
                result = True
        return result

    def updatePatrolMap(map, guardPosition, direction=direction, icon=icon):
        x, y = guardPosition
        newPatrolMap = map
        guardsNextPosition = getGuardsNextPosition(guardPosition, direction)
        keepMoving = not isOffMap(guardsNextPosition) and not isInfinte(objectsEncountered)
        if not keepMoving:
            if isOffMap(guardsNextPosition):
                print(f'the guard is off the map')
            elif isInfinte(objectsEncountered):
                print(f'the guard is in an infinite loop')
        while keepMoving:
            if isOffMap(guardsNextPosition):
                return
            
            elif isObstacle(guardsNextPosition):
                direction, icon = turnGuard(direction)
                moveGuard(newPatrolMap, guardPosition, direction, icon, objectsEncountered)
            else:
                newPatrolMap[y][x] = 'X'
                xGuard, yGuard = guardsNextPosition
                newPatrolMap[yGuard][xGuard] = icon
                updatePatrolMap(newPatrolMap, guardsNextPosition)
            return newPatrolMap
    updatePatrolMap(newPatrolMap, guardPosition)
    return isInfinte(objectsEncountered)

def resetMap():
    patrolMap = getPatrolMap(chosenPath)
    return patrolMap

def printMap(patrolMap):
    for row in patrolMap:
        joineRow = ''.join(row)
        print(joineRow)
    print('\n')

def getInfiniteCounts():
    count = 0
    for rowNo, row in enumerate(patrolMap):
        for colNo, col in enumerate(row):
            mapCopy = resetMap()
            mapCopy[colNo][rowNo] = '#'
            result = moveGuard(mapCopy, getGuardPosition, 'up', '^', [])
            if result == True:
                count += 1
    return count

print(getInfiniteCounts())



    