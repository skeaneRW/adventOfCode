import re
inputPath = "2023/day5/input.txt"
testPath = "2023/day5/testInput1.txt"


def getSeeds(path):
    file = open(path, 'r')
    for index, line in enumerate(file):
        if index == 0:
            result = line.replace('seeds: ', '').replace('\n', '').split(' ')
            result = list(map(lambda x : int(x), result))
            return result

def inputToArray(path):
    result = []
    file = open(path, 'r')
    for index, line in enumerate(file):
        if index > 0:
            result.append(line.replace('\n',''))
    filteredList = list(filter(lambda x: x != '', result) )
    return filteredList


def splitArray(arr):
    arrLen = len(arr)
    splitIndexes = [index for index, line in enumerate(arr) if line.__contains__('map')]
    splitIndexes.append(arrLen)
    splitArray = [arr[a:b] for a, b in zip([0]+ splitIndexes, splitIndexes)]
    splitArrayLen = len(splitArray)
    splitArray = splitArray[1:splitArrayLen]
    return splitArray

def makeListObj(arr):
    listObj = []
    for line in arr:
        lineResult = []
        name = line[0].replace(' map:', '').split('-to-')
        sourceDestMap = line[1::]
        sourceDestMap = list(map(lambda x: x.split(' '), sourceDestMap))
        sequences = []
        for sequence in sourceDestMap:
            sequence = list(map(lambda x: int(x), sequence))
            sequences.append(sequence)
        sourceDestMap = sequences
        lineResult = {
            'name': name,
            'keys': sequences
        }
        listObj.append(lineResult)
    return(listObj)


def findLocations(listObj, seedNumbers):
    def changeTargetValue(targetValue, sourceStart, destStart):
        difference = targetValue - sourceStart
        # print(f'{targetValue} is greater than {sourceStart} by {difference}')
        # print(f'new target value is {destStart} + {difference} = {destStart + difference}')
        return destStart + difference

    def findLocation(seedNum):
        # print(f'searching seed {seedNum}')
        targetValue = seedNum
        targetSource = 'seed'
        for obj in listObj:
            source = obj['name'][0]
            destination = obj['name'][1]
            if source == targetSource:
                # print(f'reviewing {destination}: {obj["keys"]}')
                valSet = False
                for arr in obj['keys']:
                    destStart = arr[0]
                    sourceStart = arr[1]
                    sourceRangeEnd = arr[2]
                    isFound = targetValue >= sourceStart and targetValue <= sourceStart + sourceRangeEnd -1
                    
                    if isFound and valSet == False:
                        # print(f'targetNumber {targetValue} is between {sourceStart} and {sourceStart + sourceRangeEnd - 1}')
                        targetValue = changeTargetValue(targetValue, sourceStart, destStart)
                        valSet = True
                    # else:
                        # print(f'targetNumber {targetValue} is not between {sourceStart} and {sourceStart + sourceRangeEnd - 1}')
                    targetSource = destination
                valSet = False
                # print(destination, targetValue)
        return(targetValue)
    seedResults = []
    for seedNum in seedNumbers:
        seedResults.append(findLocation(seedNum))
    print(min(seedResults))
    


chosenPath = inputPath

seeds = getSeeds(chosenPath)
arr = inputToArray(chosenPath)
splitArray = splitArray(arr)
listObj = makeListObj(splitArray)
findLocations(listObj, seeds)


    
    








