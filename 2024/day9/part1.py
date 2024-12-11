import math
import re
testPath = './testInput.txt'
testPath2 = './testInput2.txt'
inputPath = './input.txt'
chosenPath = testPath2

def readDiskMap(path):
    file = open(path, 'r')
    arr = list(file.read())
    disk = ''
    for i, value in enumerate(arr):
        if i % 2 == 0:
            id = str(math.floor(i/2))
            disk += id * int(value)
        else:
            disk += '.' * int(value)
    return disk, int(id)

disk, endingNumber = readDiskMap(chosenPath)

def updateDisk (disk, num):
    newDisk = disk
    endingNumber = [num]

    def getEndingNumber(thisDisk, endNo):
        if endNo <= 0:
            return 0
        pattern = str(endNo)
        cleanDisk = thisDisk.replace('.', '')
        lastIndexOfPattern = cleanDisk.rfind(pattern)
        lengthOfPattern = len(pattern)
        endOfPatternIndex = lastIndexOfPattern + lengthOfPattern - 1
        if endOfPatternIndex != len(cleanDisk) - 1:
            endingNumber.append(endNo - 1)
        else:
            endingNumber.append(endNo)

    def condenseDisk(thisDisk, endingNumber):
        pattern = str(endingNumber)
        indexOfFirstDot = newDisk.find('.')
        newStringArray = list(thisDisk)
        newStringArray[indexOfFirstDot] = str(endingNumber)
        newString = ''.join(newStringArray)
        #find the last instance of the pattern and replace each character with a dot
        lastIndexOfPattern = newString.rfind(pattern)
        newStringArray = list(newString)
        for i in range(lastIndexOfPattern, lastIndexOfPattern + len(pattern)):
            newStringArray[i] = '.'
        newString = ''.join(newStringArray)
        print(newString)
        return newString

    countOfDots = [i for i, char in enumerate(newDisk) if char == '.']
    for i in range(len(countOfDots)):
        num = endingNumber[len(endingNumber) - 1]
        newDisk = condenseDisk(newDisk, num)
        getEndingNumber(newDisk, num)
        if i % 200 == 0:
            print(f'{i / len(countOfDots)}% complete')
    return newDisk

newDisk = updateDisk(disk, endingNumber)

def checkSum(disk):
    numberString = disk.replace('.', '')
    sum = 0
    for i, num in enumerate(numberString):
        print(f'{i} * {num} = {i * int(num)}')
        sum += i * int(num)
    return sum

print(checkSum(newDisk))
