inputPath = "2023/day1/input.txt"
testPath = "2023/day1/testInput1.txt"

def processInput(path):
    file = open(path, "r")
    resultArr = []
    for line in file.readlines():
        stringList = list(line)
        cleanList = list([val for val in stringList if val.isnumeric()])
        firstDigit = cleanList[0]
        lastDigit = cleanList[len(cleanList) - 1]
        resultArr.append(int(f'{firstDigit}{lastDigit}'))
    file.close()
    return sum(resultArr)

print(processInput(testPath))    
print(processInput(inputPath))


