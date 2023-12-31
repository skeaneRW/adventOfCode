import time
testPath = '2023/day14/testInput1.txt'
inputPath = '2023/day14/input.txt'
chosenPath = testPath


def parseInput(path):
    result = []
    file = open(path, 'r')
    for line in file:
        line = line.replace('\n','')
        result.append([x for x in line])
    return result

#transpose rows and columns
def transpose(arr):
    return [[arr[row][col] for row in range(len(arr))] for col in range(len(arr[0]))]

def tilt(arr, dir):
    if dir == 'north' or dir == 'south':
        arr = transpose(arr)
    newArr = []
    for row in arr:
        str = ''
        subArr = []
        for colNum, char in enumerate(row):
            if char != '#':
                str += char
            if char == '#':
                subArr.append(str)
                subArr.append('#')
                str = ''
            if colNum == len(row) - 1:
                if len(str) > 0:
                    subArr.append(str)
                subArr = tuple(x for x in subArr if x != '')
                newArr.append(subArr)
    
    for rowNum, row in enumerate(newArr):
        if dir == 'north' or dir == 'west':
            sortedRow = [tuple(sorted(val, reverse=True)) for val in row]
        if dir == 'south' or dir == 'east':
                sortedRow = [tuple(sorted(val)) for val in row]
        sortedRow = [''.join(val) for val in sortedRow]
        newArr[rowNum] = [x for x in ''.join(sortedRow)]
    if dir == 'north' or dir == 'south':
        return transpose(newArr)
    else:
        return(newArr)
    
def visualize(arr):
    for row in arr:
        print(''.join(row))

def spinCycle(input):
    result = input[:]
    result = tilt(result, 'north')
    result = tilt(result, 'west')
    result = tilt(result, 'south')
    result = tilt(result, 'east')
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

input = parseInput(chosenPath)
results = [input]
scores = []
num = 10
print(num)
for n in range(num):
    results.append(spinCycle(tuple(results[-1])))
    scores.append(getScore(results[-1]))

endTime = time.time()

visualize(results[-1])
print(getScore(results[-1]))
print(f'elapsed time: {round(endTime - startTime, 2)}')
for i, score in enumerate(scores):
    print(i, score)