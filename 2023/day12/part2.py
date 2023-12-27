import time
from functools import cache
inputPath = "2023/day12/input.txt"
testPath = "2023/day12/testInput1.txt"
chosenPath = testPath
part = 'part2'

startTime = time.time()

with open(chosenPath, 'r') as file:
    input = file.readlines()

results = []
for line in input:
    startingSeq = [int(x) for x in line.split()[1].split(',')]
    startingSpringRecord = line.split()[0]
    if part == 'part1':
        seq = [int(x) for x in line.split()[1].split(',')]
        springRecord = line.split()[0]
    
    if part == 'part2':
        seq = []
        springRecordArr = []
        for i in range(5):
            seq += startingSeq
            springRecordArr += startingSpringRecord + '?'
        springRecord = ''.join(springRecordArr)
    
    # check the string to see if it's valid given the sequence provided.
    def isValid(seq, possibility):
        springResults = [len(x) for x in possibility.split('.') if x != '']
        return(springResults == seq)
    
    # check the partially built string to see if it's valid... 
    # we should abandon any additional efforts to build out strings that are invalid.
    def wipIsValid(seq, wip):
        if wip.__contains__('#') and wip[-1] == '.':
            wipSequences = [len(x) for x in wip.split('.') if x != '']
            if len(wipSequences) <= len(seq):
                for wipIdx, num in enumerate(wipSequences):
                    if num != seq[wipIdx]:
                        return False 
        return True

    # update the string based on the different possible combinations.
    def generateSubstitutions(charCount, charIndex=0, current=[]):
        if charCount == 0:
            if isValid(seq, ''.join(current)):
                results.append(1)
                return
        elif springRecord[charIndex] != '?':
            if not wipIsValid(seq, ''.join(current)):
                return
            generateSubstitutions(charCount - 1, charIndex = charIndex + 1, current = current + [springRecord[charIndex]])
        else:
            for char in ['.','#']:
                if not wipIsValid(seq, ''.join(current)):
                    return
                generateSubstitutions(charCount - 1, charIndex = charIndex + 1, current = current + [char])
    generateSubstitutions(len(springRecord))

    endTime = time.time()
    elapsedTime = round(endTime - startTime, 3)

print(sum(results))
print(f'time elapsed: {elapsedTime} seconds')
    

    