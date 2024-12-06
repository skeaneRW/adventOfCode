import re
testPath = "./testInput2.txt"
inputPath = "./input.txt"
chosenPath = inputPath

def cleanInput(path):
    file = open(path, "r")
    text = file.read()
    mulPattern = r'mul\(\d+,\d+\)'
    doPattern = r'do\(\)'
    dontPattern = r'don\'t\(\)'
    return re.findall(mulPattern + '|' + doPattern + '|' + dontPattern, text)

cleanInput = cleanInput(chosenPath)

def getMultiples(arr):
    result = []
    do = True
    for i in range(len(arr)):
        def checkCommand(string):
            if 'mul' in string:
                return 'mul'
            elif 'don\'t' in string:
                return 'don\'t'
            else:
                return 'do'
        command = checkCommand(arr[i])
        if command == 'mul' and do == True:
            nums = re.findall(r'\d+', arr[i])
            result.append(int(nums[0]) * int(nums[1]))
        elif command == 'don\'t':
            do = False
        elif command == 'do':
            do = True
    return result

multiples = (getMultiples(cleanInput))
print(sum(multiples))

