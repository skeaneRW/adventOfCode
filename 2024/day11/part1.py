import functools
import time

start_time = time.time()

testPath = './testInput.txt'
inputPath = './input.txt'
chosenPath = inputPath

def getStartingStones(chosenPath):
    with open(chosenPath) as file:
        line = file.read().splitlines()
        arr = line[0].split(' ')
        return [int(x) for x in arr]

def getStoneRule (stone):
    if stone == 0:
        return 'zero'
    if len(str(stone)) % 2 == 0:
        return 'even digits'
    else:
        return 'x 2024'
    

@functools.cache
def applyRule(stone, rule):
    if rule == 'zero': 
        return [1]
    if rule == 'even digits':
        stoneString = str(stone)
        half = int(len(stoneString) / 2)
        firstHalf = int(stoneString[:half])
        secondHalf = int(stoneString[half:])
        return [firstHalf, secondHalf]
    if rule == 'x 2024':
        return [stone * 2024]
 
def blink(stonesArr):
    newStones = []
    for stone in stonesArr:
        rule = getStoneRule(stone)
        appliedRules = applyRule(stone, rule)
        for rule in appliedRules:
            newStones.append(rule)
    return newStones

stones = getStartingStones(chosenPath)

def repeatBlinks(repititions, stones):
    for i in range(repititions):
        stones = (blink(stones))
        print(f'{i}: {i/repititions}%') if i % 5 == 0 else None
    return stones

    
result = repeatBlinks(75, stones)
print(len(result))
print("--- %s seconds ---" % (time.time() - start_time))