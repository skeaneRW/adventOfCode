testString = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
inputPath = "2023/day2/input.txt"
testPath = "2023/day2/testInput1.txt"

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

def getValidGames(array, requirements ):
    filteredList = []
    for index, item in enumerate(array):
        isValid = True
        for key, value in item.items():
            gameNumber = index + 1
            isValid = isValid and (requirements[key] >= value)
        if isValid:
            filteredList.append(gameNumber)
    return filteredList

parsedInput = (processPath(inputPath))
requirements = {'red': 12, 'green': 13, 'blue': 14}
result = sum(getValidGames(parsedInput, requirements))
print(result)


