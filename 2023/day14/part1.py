testPath = '2023/day14/testInput1.txt'
inputPath = '2023/day14/input.txt'
chosenPath = inputPath

def parseInput(path):
    result = []
    file = open(path, 'r')
    for line in file:
        line = line.replace('\n','')
        result.append([x for x in line])
    return result

def transpose(arr):
    return [[arr[row][col] for row in range(len(arr))] for col in range(len(arr[0]))]

def tiltNorth(arr):
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
                subArr = [x for x in subArr if x != '']
                newArr.append(subArr)
    
    for rowNum, row in enumerate(newArr):
        sortedRow = [sorted(val, reverse=True) for val in row]
        sortedRow = [''.join(val) for val in sortedRow]
        newArr[rowNum] = [x for x in ''.join(sortedRow)]
    return newArr
    
def visualize(arr):
    for row in arr:
        print(''.join(row))

def getScore(arr):
    rowNum = len(arr)
    score = 0
    for row in arr:
        letterOs = [char for char in row if char == 'O']
        score += rowNum * len(letterOs)
        print(rowNum, letterOs, len(letterOs), rowNum * len(letterOs))
        rowNum -= 1
    print(score)

input = parseInput(chosenPath)
print(f'input:\n {input}')
transposedInput = transpose(input)
result = tiltNorth(transposedInput)
print(f'result:\n{result}')
transposedResult = transpose(result)
visualize(transposedResult)
getScore(transposedResult)
