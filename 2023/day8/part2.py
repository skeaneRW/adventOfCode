from functools import reduce
import math
inputPath = "2023/day8/input.txt"
testPath = "2023/day8/testInput2.txt"
chosenPath = inputPath

def parseInput (path):
    file = open(path, 'r')
    directions = {}
    pattern = ''
    for index, line in enumerate(file.readlines()):
        line = line.replace('\n', '')
        if index == 0:
            pattern = list(line)
            pattern = list(map(lambda x: x.replace('R', '1').replace('L', '0'), pattern))
            pattern = list(map(lambda x: int(x), pattern))
        elif line != '':
            splitLine = (line.split(' = '))
            dirKey = splitLine[0]
            dirVal = splitLine[1].replace('(','').replace(')','').split(', ')
            directions[dirKey] = dirVal
    return ({'pattern': pattern, 'directions': directions})

def runPattern(input):
    def lcm(numbers):
        return reduce(lambda x, y: x * y // math.gcd(x, y), numbers, 1)
    def getAnyKeysThatEndWithChar (directions, char):
        keys = list(directions.keys())
        endWithChar = [key for key in keys if key[2:3] == char]
        endWithChar.sort()
        return endWithChar
    def followSteps(currentStep, stepCount):
        countsArr = []
        for dir in startingPoint:
            currentStep = dir
            print(f'reviewing {dir}')
            while not endingPoint.__contains__(currentStep):
                for stepNum in input.get('pattern'):
                    print(f'L-R stepnum: {stepNum}')
                    nextStep = input.get('directions')[currentStep][stepNum]
                    stepCount = stepCount + 1
                    print(f'{currentStep} becomes {nextStep} (at count #{stepCount})')
                    currentStep = nextStep
                    if endingPoint.__contains__(currentStep):
                        print(f'steps complete at {stepCount}!')
                        countsArr.append(stepCount)
                        stepCount = 0
        print(lcm(countsArr))
            
    startingPoint = getAnyKeysThatEndWithChar(input.get('directions'), 'A')
    endingPoint = getAnyKeysThatEndWithChar(input.get('directions'), 'Z')
    return followSteps(startingPoint, 0)
input = parseInput(chosenPath)
answer = runPattern(input)