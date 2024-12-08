testPath = './testInput.txt'
inputPath = './input.txt'
chosenPath = inputPath
import sys
limit = 10**6
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
for row in patrolMap:
    print(row)
print(getGuardPosition)

def moveGuard(patrolMap, guardPosition, direction='up', icon='^'):
    newPatrolMap = patrolMap
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
        if x < 0 or y < 0 or y >= len(patrolMap) or x >= len(patrolMap[y]):
            return True
        return False
    
    def isObstacle(nextPosition):
        x, y = nextPosition
        if patrolMap[y][x] == '#':
            return True
        return False
    
    def countPath(patrolMap):
        pattern = ['X', '^', 'v', '<', '>']
        count = 0
        for y in range(len(patrolMap)):
            for x in range(len(patrolMap[y])):
                if pattern.__contains__(patrolMap[y][x]):
                    count += 1
        return count

    def updatePatrolMap(patrolMap, guardPosition, direction=direction, icon=icon):
        print(f'attempting to update patrol map')
        x, y = guardPosition
        newPatrolMap = patrolMap
        guardsNextPosition = getGuardsNextPosition(guardPosition, direction)
        if isOffMap(guardsNextPosition):
            print('off map')

        elif isObstacle(guardsNextPosition):
            print('hit obstacle turn 90 degrees')
            direction, icon = turnGuard(direction)
            print('new direction is', direction)
            print('new icon is', icon)
            moveGuard(patrolMap, guardPosition, direction, icon)
        else:
            newPatrolMap[y][x] = 'X'
            xGuard, yGuard = guardsNextPosition
            print('moving guard to', guardsNextPosition)
            newPatrolMap[yGuard][xGuard] = icon
            updatePatrolMap(newPatrolMap, guardsNextPosition)
        return newPatrolMap
    newPatrolMap = updatePatrolMap(patrolMap, guardPosition)
    for row in newPatrolMap:
        print(row)
    print('direction is', direction)
    return countPath(newPatrolMap)

moveGuard(patrolMap, getGuardPosition)
result = moveGuard(patrolMap, getGuardPosition)
print(result)

    