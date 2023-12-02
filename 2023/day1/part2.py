import re
inputPath = "2023/day1/input.txt"
testPath = "2023/day1/testInput2.txt"
inputArray = []
numberObj = {
    '1': 'one', 
    '2': 'two', 
    '3': 'three', 
    '4': 'four', 
    '5': 'five', 
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
    }

def processInput(path):
    file = open(path, "r")

    def textToArray():
        for line in file.readlines():
            inputArray.append(line)

    #insert number values for each spelled-out number in the string. numbers must be in place.
    updatedStringArr = []
    def updateString(arr):
        for line in arr:
            #chop up the string on each numeric value.
            choppedUpLine = re.findall(r"[^\W\d_]+|\d+", line)
            newFragment = []
            newLineArr = []
            result = ''
            for strFragment in choppedUpLine:
                for key, value in numberObj.items():
                    #if any of the fragments contain a spelled-out number, make store that info in an array with the 
                    # key of the position index. Then reorder the array by the position. append the numbers to the string.
                    if strFragment.find(value) >= 0:
                        if strFragment.count(value) > 1:
                            #need to append a key value for each occurrance...
                            positions = [m.start() for m in re.finditer(value, strFragment)]
                            for position in positions:
                                newFragment.append({'key': key, 'position': position})
                        else:
                            newFragment.append({'key': key, 'position': strFragment.find(value)})
                        sortedFragment = sorted(newFragment, key=lambda x: x['position'])
                        values = list(map(lambda x:x['key'], sortedFragment))
                        result = ''.join(values)
                    
                newFragment = []
                strFragment = (strFragment + result)
                strFragment = (strFragment)
                newLineArr.append(strFragment)
                result = ''
            updatedStr = (''.join(newLineArr))
            updatedStringArr.append(updatedStr)
        return updatedStringArr

    #remove any non-numeric values from a string and convert to a list
    def removeNonNumeric(input):
        resultArr = []
        for line in input:
            stringList = list(line)
            cleanList = list([val for val in stringList if val.isnumeric()])
            resultArr.append(cleanList)
        return resultArr

    #loop through the array of numbers and get a new list with a two digit number based on first / last number combo.
    def getSecretNumber(arrays):
            numList = []
            for arr in arrays:
                firstDigit = arr[0]
                lastDigit = arr[len(arr) - 1]
                numList.append(int(f'{firstDigit}{lastDigit}'))
            return numList

    textToArray()
    convertedStrings = updateString(inputArray)
    resultArr = removeNonNumeric(convertedStrings)
    resultIntArr = getSecretNumber(resultArr)
    file.close()
    return (sum(resultIntArr))
    
print(processInput(inputPath))