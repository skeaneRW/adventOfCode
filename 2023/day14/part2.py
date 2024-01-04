import time
from functools import cache
from multiprocessing import Process
testPath = '2023/day14/testInput1.txt'
inputPath = '2023/day14/input.txt'
chosenPath = inputPath

if __name__ == "__main__":
    def parseInput(path):
        with open(path, 'r') as file:
            return [tuple(line.strip()) for line in file]

    #transpose rows and columns
    def transpose(arr):
        return ([arr[row][col] for row in range(len(arr))] for col in range(len(arr[0])))
    
    def visualize(arr):
        for row in arr:
            print(''.join(row))
        
    @cache
    def tilt (arr, dir):
        if dir == 'north' or dir == 'south':
            arr = transpose(arr)
        newArr = []
        for row in arr:
            str = ''
            subArr = []
            for colNum, char in enumerate(row):
                if char != '#' and colNum != len(row) - 1:
                    str += char
                elif char == '#':
                    subArr.append(str)
                    subArr.append('#')
                    str = ''
                else:
                    str += char
                    subArr.append(str)
                subArr = [x for x in subArr if x != '']
                if dir in ('north','west'):
                    sortedRow = tuple(tuple(sorted(val, reverse=True)) if val.__contains__('O') else val for val in subArr)
                if dir in ('south', 'east'):
                    sortedRow = tuple(tuple(sorted(val)) if val.__contains__('O') else val for val in subArr)
                sortedRow = tuple(''.join(val) for val in sortedRow)
            newArr.append(tuple(x for x in ''.join(sortedRow)))
        if dir == 'north' or dir == 'south':
            return transpose(newArr)
        return(tuple(newArr))

    @cache
    def spinCycle(input):
        result = input
        directions = ('north', 'west', 'south', 'east')
        for dir in directions:
            result = tilt(result, dir)
        return result

    def getScore(arr):
        rowNum = len(arr)
        score = 0
        for row in arr:
            letterOs = [char for char in row if char == 'O']
            score += rowNum * len(letterOs)
            rowNum -= 1
        return(score)

    startTime = time.time()

    input = tuple(parseInput(chosenPath))
    
    def detectCycle(input):
        def stringify(grid):
            return ''.join([''.join(row) for row in input])
        GRIDS = dict()
        i = 1
        while True:
            input = spinCycle(input)
            hash = stringify(input)

            if hash in GRIDS:
                cycleLen = i - GRIDS[hash]
                return (input, i, cycleLen)
            else: 
                GRIDS[hash] = i
                i += 1
    
    grid, stablePoint, cyclen = detectCycle(input)
    print(stablePoint, cyclen)

    num =   1000000000
    n = 0
    storedVal = 0

    while n < num:
        numberofCycles = (num - stablePoint) // cyclen
        if n < stablePoint:
            input = (spinCycle(input))
            n += 1
        if n == stablePoint:
            print(cyclen * numberofCycles)
            n += (cyclen * numberofCycles)
        if n > stablePoint:
            input = (spinCycle(input))
            n += 1

    endTime = time.time()
    print(f'final score = {getScore(input)}')
    print(f'elapsed time: {round(endTime - startTime, 2)}')
