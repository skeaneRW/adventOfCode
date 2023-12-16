inputPath = "2023/day8/input.txt"
testPath = "2023/day8/testInput1.txt"
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
    def executeDirections(currentStep, stepCount):
        for stepNum in input.get('pattern'):
            nextStep = input.get('directions')[currentStep][stepNum]
            stepCount = stepCount + 1
            print(nextStep, stepCount)
            currentStep = nextStep
            if currentStep == 'ZZZ':
                print(f'current {currentStep}')
                return stepCount    
        return executeDirections(currentStep, stepCount)
    return executeDirections('AAA', 0)

input = parseInput(chosenPath)
answer = runPattern(input)
print(answer)