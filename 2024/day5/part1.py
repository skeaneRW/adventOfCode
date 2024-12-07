testPath = './testInput.txt'
inputPath = './input.txt'
chosenPath = inputPath

def parseInput(path):
    pageOrderingRules = []
    updates = []
    file = open(path, 'r')
    for line in file:
        if '|' in line:
            line = line.strip('\n').split('|')
            line = list(map(int, line))
            pageOrderingRules.append(line)
        elif ',' in line:
            line = line.strip('\n').split(',')
            line = list(map(int, line))
            updates.append(line)
    return pageOrderingRules, updates

pageOrderingRules, updates = parseInput(chosenPath)

def getValidUpdates(rules, updates):
    invalidUpdates = []
    updatesCopy = updates.copy()
    def getPrecedingPages(page, rules):
        precedingPages = []
        for before, after in rules:
            if after == page:
                precedingPages.append(before)
        return precedingPages
    def getFollowingPages(page, rules):
        followingPages = []
        for before, after in rules:
            if before == page:
                followingPages.append(after)
        return followingPages
    for update in updates:
        for pageSeq, page in enumerate(update):
            precedingPages = getPrecedingPages(page, rules)
            followingPages = getFollowingPages(page, rules)
            for precedingPage in precedingPages:
                if precedingPage in update[pageSeq:] and update.index(precedingPage) > pageSeq:
                    invalidUpdates.append(update)
                    break
            for followingPage in followingPages:
                if followingPage in update[:pageSeq] and update.index(followingPage) < pageSeq:
                    if update not in invalidUpdates:
                        invalidUpdates.append(update)
                    break
    for invalidUpdate in invalidUpdates:
        if invalidUpdate in updatesCopy:
            updatesCopy.remove(invalidUpdate)
    return updatesCopy
        

validUpdates = getValidUpdates(pageOrderingRules, updates)

def getMidPoint(arrays):
    midPoints = []
    for array in arrays:
        midPointIndex = len(array) // 2
        midPoints.append(array[midPointIndex])
    return midPoints

midPoints = getMidPoint(validUpdates)

print(sum(midPoints))
