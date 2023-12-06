import re
inputPath = "2023/day3/input.txt"
testPath = "2023/day3/testInput1.txt"
puzzObjects = []

def findGoodParts (path):
    file = open(path, "r")
    def parseRow(file):
        lineIndex = 0
        puzzleInput = []
        for line in file.readlines():
            line = list(line)
            def isNotNewLine(char):
                return char != '\n'
            line = list(filter(isNotNewLine, line))
            obj = {'rowId': lineIndex, 'row': line, 'numbers': [], 'symbols': []}
            lineIndex += 1
            def makePuzzObj(obj):
                puzzObjects.append(obj)
            makePuzzObj(obj)
    
    def checkForNumbers(objects):
        for object in objects:
            num = ''
            result = []
            numValues = []
            indexes = []
            maxLen = len(object['row']) - 1
            def appendNum(n):
                numValues.append(num)
                result.append({'numVal': numValues, 'indexes': indexes, 'isGood': False})
            for index, char in enumerate(object['row']):
                if char.isnumeric():
                    num = f'{num}{char}'
                    indexes.append(index)
                    if index == maxLen:
                        appendNum(num)
                else:
                    numValues.append(num)
                    if num.isnumeric():
                        result.append({'numVal': numValues, 'indexes': indexes, 'isGood': False})
                    indexes = []
                    numValues = []
                    num = ''
            object['numbers'] = result
        return(objects)

    def checkForSymbols(objects):
        for object in objects:
            symbol = ''
            result = []
            for index, char in enumerate(object['row']):
                def isSymbol (value):
                    return re.match('[^A-Za-z0-9.]', value)
                if isSymbol(char):
                    symbol = char
                    symbolIndex = index
                else:
                    if isSymbol(symbol): #need to replace this bit with a check that the item is a symbol
                        result.append({'symbol': symbol, 'index': symbolIndex})
                    symbolIndex = ''
                    symbol = ''
            object['symbols'] = result
        return(objects)

    def checkRow(rowNum):
        goodResults = []
        maxLen = len(puzzObjects)
        def getSymbolPositions(rowNum):
            symbols = puzzObjects[rowNum].get('symbols')
            def getIndex(obj):
                return obj.get('index')
            return list(map(getIndex, symbols))
        
        def getNumbers(rowNum):
            def checkCurrentRow(number, rowNum):
                symbolPositions = getSymbolPositions(rowNum)
                intersection = list(set(symbolPositions) & set(numIndexes))
                if len(intersection):
                    number['isGood'] = True

            def checkPriorRow(number, rowNum):
                symbolPositions = getSymbolPositions(rowNum - 1)
                intersection = list(set(symbolPositions) & set(numIndexes))
                if len(intersection):
                    number['isGood'] = True

            def checkNextRow(number, rowNum):
                if rowNum + 1 < maxLen:
                    symbolPositions = getSymbolPositions(rowNum + 1)
                    intersection = list(set(symbolPositions) & set(numIndexes))
                    if len(intersection):
                        number['isGood'] = True
            for number in puzzObjects[rowNum].get('numbers'):
                numIndexes = number.get('indexes').copy()
                numIndexes.append(numIndexes[len(numIndexes) - 1] + 1)
                numIndexes.append(numIndexes[0]-1)
                checkPriorRow(number, rowNum)
                checkCurrentRow(number, rowNum)
                checkNextRow(number, rowNum)
                numIndexes = ''
                if number['isGood'] == True:
                    goodResults.append(number)
        getNumbers(rowNum)
        return goodResults

    def getGoodParts():
        results = []
        for index, line in enumerate(puzzObjects):
            for number in checkRow(index):
                numString = number.get('numVal')[0]
                results.append(int(numString))
        print(sum(results))
        return(sum(results))

    parseRow(file)
    checkForNumbers(puzzObjects)
    checkForSymbols(puzzObjects)
    getGoodParts()

findGoodParts(inputPath)

