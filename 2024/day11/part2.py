testPath = './testInput.txt'
inputPath = './input.txt'
chosenPath = inputPath

def getStartingStones(chosenPath):
    with open(chosenPath) as file:
        line = file.read().splitlines()
        arr = line[0].split(' ')
        dict = {}
        for x in arr:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        return dict
    
    
def applyRule(stone):
    if stone == str(0): 
        return 1, None
    if len(str(stone)) % 2 == 0:
        stoneString = str(stone)
        half = int(len(stoneString) / 2)
        firstHalf = int(stoneString[:half])
        secondHalf = int(stoneString[half:])
        return firstHalf, secondHalf
    else:
        return int(stone) * 2024, None
 
stoneDict = getStartingStones(chosenPath)

def blink(thisDict):
    newDict = {}
    for key, count in thisDict.items():
        newStoneA, newStoneB = applyRule(str(key))
        if newStoneA in newDict:
            newDict[newStoneA] += count
        else:
            newDict[newStoneA] = count
        if newStoneB != None:
            if newStoneB in newDict:
                newDict[newStoneB] += count
            else:
                newDict[newStoneB] = count
    return newDict

def repeatBlinks(repititions, stones):
    for i in range(repititions):
        stones = blink(stones)
        print(f'{i}: {i/repititions}%') if i % 5 == 0 else None
    return stones

result = repeatBlinks(75, stoneDict)

print(sum(result.values()))
    