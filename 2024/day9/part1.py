import math
import re
testPath = './testInput.txt'
testPath2 = './testInput2.txt'
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
    def countFreeSpace(arr):
        count = 0
        for i in arr:
            if i == '.':
                count += 1
        return count

    def fillFreeSpace(arr):
        freeSpaceIndex = arr.index('.')
        lastNumber = ''
        for i in range(len(arr)):
            if arr[i] != '.':
                lastNumber = arr[i]
        arr[freeSpaceIndex] = lastNumber
        lastNumberIndex = 0
        for i in range(len(arr)):
            if arr[i] == lastNumber:
                lastNumberIndex = i
        arr[lastNumberIndex] = '.'
        return arr
    freeSpaceCount = countFreeSpace(disk)
    for i in range(freeSpaceCount):
        newDisk = fillFreeSpace(disk)
        if i % 100 == 0:
            print(f'{i/freeSpaceCount}')
    return newDisk

newDisk = condense(disk)

def checkSum(disk):
    sum = 0
    for i, num in enumerate(disk):
        if num != '.':
            sum += (int(num) * i)
    return sum

print(checkSum(newDisk))
