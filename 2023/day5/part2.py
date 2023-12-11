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

def fixSeeds(seeds):
    splitIndexes = [index for index, item in enumerate(seeds) if not index % 2]
    splitIndexes.append(len(seeds))
    seedMap = [seeds[a:b] for a, b in zip([0]+ splitIndexes, splitIndexes)][1::]
    return(seedMap)

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



def getSeedFromLocation(listObj):
    def changeTargetValue(targetVal, sourceStart, destStart):
        difference = targetVal - destStart
        return sourceStart + difference
    
    def checkForValidSeed(targetVal):
        isValid = False
        for arr in newSeeds:
            isMatch = targetVal >= arr[0] and targetVal <= arr[0] + arr[1] - 1
            # print(f'is {targetVal} between {arr[0]} and {arr[0] + arr[1] - 1}: ({isMatch})')
            if isMatch:
                isValid = True
                return isValid
            # print(arr)
        return isValid
    
    def findSeed(locNum):
        targetVal = locNum
        targetDest = 'location'
        for obj in listObj:
            source = obj['name'][0]
            destination = obj['name'][1]
            if targetDest == destination:
                # print(f'{destination} is {targetVal}. Looking for {source}')
                valSet = False
                for arr in obj['keys']:
                    destStart = arr[0]
                    sourceStart = arr[1]
                    destRangeEnd = arr[2]
                    isFound = targetVal >= destStart and targetVal <= destStart + destRangeEnd -1
                    # print(f'checking if {targetVal} is between {destStart} and {destStart + destRangeEnd -1} ({isFound})')
                    if isFound and valSet != True:
                        targetVal = changeTargetValue(targetVal, sourceStart, destStart)
                        valSet = True
                    targetDest = source
                valSet = False
        print(f'is {targetVal} a valid seed number (evaluation location #{locNum})?')
        if checkForValidSeed(targetVal):
            print(f'{locNum} is a valid location!')
            return True
        else:
            return False

    i = 0
    while findSeed(i) == False:
        i = i + 1
        


chosenPath = testPath

seeds = getSeeds(chosenPath)
newSeeds = fixSeeds(seeds)

arr = inputToArray(chosenPath)
splitArray = splitArray(arr)
listObj = makeListObj(splitArray)
listObj.reverse()

getSeedFromLocation(listObj)



    
    








