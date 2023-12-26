import time
inputPath = "2023/day12/input.txt"
testPath = "2023/day12/testInput1.txt"
chosenPath = inputPath


startTime = time.time()

with open(chosenPath, 'r') as file:
    input = file.readlines()

results = []
for line in input:
    startingSeq = [int(x) for x in line.split()[1].split(',')]
    seq = []
    startingSpringRecord = line.split()[0]
    springRecord = []
    for i in range(5):
       seq += startingSeq
       springRecord += startingSpringRecord + '?'
    '''
    seq = [int(x) for x in line.split()[1].split(',')]
    springRecord = line.split()[0]
    '''
    # check the string to see if it's valid given the sequence provided.
    def isValid(seq, possibility):
        springResults = [len(x) for x in possibility.split('.') if x != '']
        return(springResults == seq)
    # generate a list of all of the the different possible replacements for any char == '?'
    # e.g. '???' could be '###' or '##.' or '#..' etc...
    def generateSubstitutions(charCount, charIndex=0, current=[]):
        if charCount == 0:
            if isValid(seq, ''.join(current)):
                results.append(1)
            charIndex = 0
            return
        elif springRecord[charIndex] != '?':
            generateSubstitutions(charCount - 1, charIndex = charIndex + 1, current = current + [springRecord[charIndex]])
        else:
            for char in ['.','#']:
                generateSubstitutions(charCount - 1, charIndex = charIndex + 1, current = current + [char])
    print(f'reviewing: {line}')
    generateSubstitutions(len(springRecord))

    endTime = time.time()
    elapsedTime = round(endTime - startTime, 3)

print(sum(results))
print(f'time elapsed: {elapsedTime} seconds')
    

    