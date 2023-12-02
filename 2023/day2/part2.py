inputPath = "2023/day2/input.txt"
testPath = "2023/day2/testInput2.txt"

CUBE_COLORS = ['red', 'green', 'blue']

def processPath(path):
    #covert an input line into an array of arrays. The Array represents the game;
    #the subArray represents the game round
    def formatTextInput(str):
        cubeStr = str.split(':')[1]
        result = cubeStr.split(';')
        return result

    # converts each item into a dictionary for parsing.
    def makeDict(arr):
        result = []
        for eachStr in arr:
            dict={}
            cubes = eachStr.split(',')
            for cube in cubes:
                for color in CUBE_COLORS:
                    if cube.find(color) > -1:
                        newStr = '0'
                        for char in cube:
                            if char.isnumeric():
                                newStr = f'{newStr}{char}'
                            cubeCount = newStr
                        dict[color] = int(cubeCount)
            result.append(dict)
        return result

    #get a get the max value for each color cube...
    def getMaxColor(array):
        result = []
        dict = {'red': 0, 'green': 0, 'blue': 0}
        for eachItem in array:
            for key, value in eachItem.items():
                if value > dict[key]:
                    dict[key] = value
        return(dict)
    
    def getMinColor(array, maxColor):
        dict = maxColor
        for item in array:
            for key, value in item.items():
                if value < dict[key]:
                    dict[key] = value
        return(dict)


    def processInputLine(str):
        formattedLine = formatTextInput(str)
        gameDict = makeDict(formattedLine)
        gameResult = getMaxColor(gameDict)
        return gameResult
    
    result = []
    file = open(path, "r")
    for line in file.readlines():
        result.append(processInputLine(line))
    return result

parsedInput = (processPath(inputPath))

def makePowerArr(arr):
    resultArr = []
    for input in arr:
        exponent = 1
        for key, value in input.items():
            exponent = exponent * value
        resultArr.append(exponent)
    return resultArr

result = makePowerArr(parsedInput)
print(sum(result))




