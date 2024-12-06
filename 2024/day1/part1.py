inputPath = "./input.txt"
testPath = "./testInput.txt"
chosenPath = inputPath

#fn to get the column of numbers from the file
def getColumn(arrayType, path):
    def splitInt (arrayType):
        if arrayType == 'left':
            return 0
        else: 
            return 1
    file = open(path, "r")
    result =  []
    for line in file.readlines():
        number = int(line.split()[splitInt(arrayType)])
        result.append(number)
    return result

# sort both arrays
rightArr = sorted(getColumn('right', chosenPath))
leftArr = sorted(getColumn('left', chosenPath))

#fn to get the difference between the two arrays
def getDifference(leftArr, rightArr):
    result = []
    for i in range(len(leftArr)):
        result.append((rightArr[i] - leftArr[i]))
    return result

print (sum(getDifference(leftArr, rightArr)))



        
        



