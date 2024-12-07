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

def getInvalidUpdates(rules, updates):
    invalidUpdates = []
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
                    if update not in invalidUpdates:
                        invalidUpdates.append(update)
                    break
            for followingPage in followingPages:
                if followingPage in update[:pageSeq] and update.index(followingPage) < pageSeq:
                    if update not in invalidUpdates:
                        invalidUpdates.append(update)
                    break
    return invalidUpdates
        

invalidUpdates = getInvalidUpdates(pageOrderingRules, updates)

def sortUpdates(rules, update):
    results = []
    def getApplicableRules(update, rules):
        matchedRules = []
        applicableRules = []
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                matchedRules.append(rule)
        for rule in matchedRules:
            if update.index(rule[0]) > update.index(rule[1]):
                applicableRules.append(rule)
        return applicableRules

    def swapPages(page1, page2, update):
        page1Index = update.index(page1)
        page2Index = update.index(page2)
        update[page1Index], update[page2Index] = update[page2Index], update[page1Index]
        return update

    def reorder(update, rules):
        applicableRules = getApplicableRules(update, rules)
        if len(applicableRules) > 0:
            for rule in applicableRules:
                update = swapPages(rule[0], rule[1], update)
                return reorder(update, rules)
        return update
    
    reorderedUpdate = reorder(update, rules)
    rules = getApplicableRules(reorderedUpdate, rules)
    if len(rules) <= 0:
        results.append(reorderedUpdate)
    return results

results = []
for update in invalidUpdates:
    sortedUpdates = sortUpdates(pageOrderingRules, update)
    results.extend(sortedUpdates)

def getMidPoint(arrays):
    print(f'arrays: {arrays}')
    midPoints = []
    for array in arrays:
        print(f'looking at array: {array}')
        midPointIndex = len(array) // 2
        print(f' the midpoing is page: {array[midPointIndex]}')
        midPoints.append(array[midPointIndex])
    return midPoints


midponts = getMidPoint(results)
print(f' sum of midpoints is: {sum(midponts)}')

