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
                    return re.match('[*]', value)
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

    validResults = []
    def checkRow(rowNum):
        symbols = puzzObjects[rowNum].get('symbols')
        if len(symbols):
            for symbol in symbols:
                result = []
                i = symbol.get('index')
                symbolRange = [i - 1, i, i + 1]
                def checkForAdjacentNumbers(row):
                    for number in puzzObjects[row].get('numbers'):
                        intersection = list(set(symbolRange) & set(number.get('indexes')))
                        if len(intersection):
                            result.append(int(number.get('numVal')[0]))
                checkForAdjacentNumbers(rowNum - 1)
                checkForAdjacentNumbers(rowNum)
                checkForAdjacentNumbers(rowNum + 1)
                if len(result) == 2:
                    resultsMultiplied = (result[0] * result[1])
                    validResults.append(resultsMultiplied)
                    

    def getGoodParts():
        for index, line in enumerate(puzzObjects):
            checkRow(index)
        print(sum(validResults))
        
    parseRow(file)
    checkForNumbers(puzzObjects)
    checkForSymbols(puzzObjects)
    getGoodParts()

findGoodParts(inputPath)

