import time
from functools import cache
inputPath = "2023/day12/input.txt"
testPath = "2023/day12/testInput1.txt"
chosenPath = inputPath
part = 'part2'

startTime = time.time()

with open(chosenPath, 'r') as file:
    input = file.readlines()

total = 0
def parse(line: str):
    record, groups = line.split(" ")
    groups = tuple(map(int, groups.split(",")))
    if part == 'part2':
        record = "?".join([record] * 5)
        groups *= 5
    return record, groups

def isValid (record, startPoint, endPoint):
    # record cannot be out of bounds
    if startPoint - 1 <  0 or endPoint + 1 >= len(record):
        return False
    # record can't have an additional hash at either end
    if record[startPoint - 1] == '#' or record[endPoint + 1] == '#':
        return False
    # we cant exclude prior hashes
    if '#' in record[:startPoint]:
        return False
    # check to make sure we don't have any dots in the target segment
    for charIndex in range(startPoint, endPoint + 1):
        if record[charIndex] == '.':
            return False
    # if we pass all previous checks, the result is valid
    print(record, startPoint, endPoint)
    return True

@cache
def depthFirstSearch(record, groups):
    # if we go through the solution and get to the end there should
    # be no more hash symbols. if you still have a hash, it's not a valid solution.
    if not groups:
        return 0 if "#" in record else 1
    
    hashSize, restOfGroup = groups[0], groups[1:]
    count = 0
    
    for endPoint in range(len(record)):
        startPoint = endPoint - (hashSize - 1)
        if isValid(record, startPoint, endPoint):
            count += depthFirstSearch(record[endPoint + 1:], restOfGroup)
    return count

for lineIdx, line in enumerate(input):
    record, groups = parse(line)
    record = '.' + record + '.'
    total += depthFirstSearch(record, groups)


print(total)
    
   