inputPath = "2023/day12/input.txt"
testPath = "2023/day12/testInput1.txt"
chosenPath = inputPath

with open(chosenPath, 'r') as file:
    input = file.readlines()

results = []

for line in input:
    seq = [int(x) for x in line.split()[1].split(',')]
    springRecord = line.split()[0]

    # generate a list of all of the the different possible replacements for any char == '?'
    # e.g. '???' could be '###' or '##.' or '#..' etc...
    def generateSubstitutions(charCount, current=[]):
        if charCount == 0:
            substitutions.append(current)
            return
        for char in ['.','#']:
            generateSubstitutions(charCount - 1, current = current + [char])
    possibility = springRecord
    substitutions = []

    numberOfUnknownChars = len([x for x in springRecord if x == '?'])
    generateSubstitutions(numberOfUnknownChars)

    # filter substitutions to only include those with the expected number of hashes
    def filterByHashCount(arr):
        filteredList = []
        totalHashes = sum(seq)
        existingHashes = len([x for x in springRecord if x == '#'])
        requiredHashes = totalHashes - existingHashes
        for subArr in arr:
            if len([x for x in subArr if x == '#']) == requiredHashes:
                filteredList.append(subArr)
        return filteredList
    substitutions = filterByHashCount(substitutions)

    goodSeqCount = 0
    # for each of the remaining possible substitutions, make a string a tested.
    for subs in substitutions:
        unknownPos = [i for i, x in enumerate(springRecord) if x == '?']
        counter = 0
        def getPossibility(string):
            subsIndex = 0
            testString = string
            for stringIndex, char in enumerate(string):
                if char == '?':
                    testString = ''.join([subs[subsIndex] if i == stringIndex else x for i, x in enumerate(testString)])
                    subsIndex += 1
            return testString                
        aPossibility = getPossibility(springRecord)
        
        # check the string to see if it's valid given the sequence provided.
        def isValid(seq, possibility):
            springResults = [len(x) for x in possibility.split('.') if x != '']
            return(springResults == seq)
        if isValid(seq, aPossibility):
            goodSeqCount += 1
    # accumulate all of the combinations and provide the total.
    #print(f'{springRecord} {seq} \n  has {goodSeqCount} good combination{"" if goodSeqCount == 1 else "s"}')
    results.append(goodSeqCount)
    
print(sum(results))
    

    