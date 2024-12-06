import re
testPath = "./testInput.txt"
inputPath = "./input.txt"
chosenPath = inputPath

def cleanInput(path):
    file = open(path, "r")
    text = file.read()
    pattern = r'mul\(\d+,\d+\)'
    return re.findall(pattern, text)

cleanInput = cleanInput(chosenPath)

def getMultiples(arr):
    result = []
    for i in range(len(arr)):
        nums = re.findall(r'\d+', arr[i])
        result.append(int(nums[0]) * int(nums[1]))
    return result

print(sum(getMultiples(cleanInput)))

