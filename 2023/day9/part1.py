inputPath = "2023/day9/input.txt"
testPath = "2023/day9/testInput1.txt"
chosenPath = inputPath

def inputToArray(path):
    result = []
    file = open(path, 'r')
    for line in file.readlines():
        line = line.replace('\n','').split(' ')
        line = [int(num) for num in line]
        result.append(line)
    return result


def createSequences(input):
    def createSequence(line):
        result = [line]
        
        def isComplete(arr):
            noZeros = [char for char in arr if char != 0]
            return(len(noZeros) == 0)
        currentLine = line
        
        while not isComplete(result[len(result) - 1]):
            newLine = []
            for index, num in enumerate(currentLine):
                if index > 0:
                    newLine.append(num - currentLine[index - 1])
            result.append(newLine)
            currentLine = newLine
        return result
    
    sequences = []
    for line in input:
        sequences.append(createSequence(line))
    return sequences

def predictNextValues(sequences):
    def predictNextValue(sequence):
        reversedList = sequence[::-1]
        result = 0
        for index, listItem in enumerate(reversedList):
            if index > 0:
                lastListItem = listItem[len(listItem) - 1]
                result = lastListItem + result
        return result
    nextValues = []
    for sequence in sequences:
        nextValues.append(predictNextValue(sequence))
    return nextValues

inputArr = inputToArray(chosenPath)
sequences = createSequences(inputArr)
nextValues = predictNextValues(sequences)
print(sum(nextValues))