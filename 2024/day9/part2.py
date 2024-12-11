import math
import re
testPath = './testInput.txt'
inputPath = './input.txt'
chosenPath = inputPath

def readDiskMap(path):
    file = open(path, 'r')
    arr = list(file.read())
    disk = []
    for i, value in enumerate(arr):
        if i % 2 == 0:
            id = str(math.floor(i/2))
            for i in range(int(value)):
                disk.append(id)
        else:
            for i in range(int(value)):
                disk.append('.')
    return disk, int(id)

disk, endingNumber = readDiskMap(chosenPath)

def condense(disk):
    newDisk = []
    fileIds = []
    for i in range(len(disk)):
        if disk[i] != '.' and disk[i] not in fileIds:
            fileIds.append(disk[i])

    def countInstances(arr, pattern):
        count = 0
        for i in arr:
            if i == pattern:
                count += 1
        return count

    def getSpaceIndex(arr, targetCount):
        count = 0
        for i in range(len(arr)):
            if arr[i] != '.':
                count = 0
            if arr[i] == '.':
                count += 1
            if count == targetCount:
                return i + 1 - targetCount
        return 0
            
    def canMove(arr, id):
        instances = countInstances(arr, id)
        arraySegment = arr[:arr.index(id)]
        freeSpaceIndex = getSpaceIndex(arraySegment, instances)
        if freeSpaceIndex == 0:
            return False
        return True

    def fillFreeSpace(arr, id):
        instances = countInstances(arr, id)
        freeSpaceIndex = getSpaceIndex(arr, instances)
        indexesOfId = [i for i, x in enumerate(arr) if x == id]
        for n in indexesOfId:
            arr[n] = '.'
        for i in range(instances):
            arr[freeSpaceIndex + i] = id
        return arr
        
    for i, id in enumerate(fileIds[::-1]):
        if canMove(disk, id):
            newDisk = fillFreeSpace(disk, id)
        if i % 100 == 0:
            print(f'{i/len(fileIds)}')
    return newDisk

newDisk = condense(disk)

def checkSum(disk):
    sums = []
    for i, num in enumerate(disk):
        if num == '.':
            #print(f'{i} is a . do not add to sum')
            sums.append(0)
        else:
            #print(f'{i} * {int(num)} = {int(num) * i}')
            sums.append(int(num) * i)
    #print(sums)
    return sum(sums)

print('----------')
print(checkSum(newDisk))

# expect a result of 00992111777.44.333....5555.6666.....8888.. on test input.
