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
rightArr = getColumn('right', chosenPath)
leftArr = getColumn('left', chosenPath)

#fn to get similarities between the two arrays
def getSimilarities(leftArr, rightArr):
    result = []
    for i in range(len(leftArr)):
        count = rightArr.count(leftArr[i])
        result.append(leftArr[i] * count)
    return result

print(sum(getSimilarities(leftArr, rightArr)))




        
        



