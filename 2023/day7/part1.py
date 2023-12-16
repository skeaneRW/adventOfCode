from collections import Counter as count
inputPath = "2023/day7/input.txt"
testPath = "2023/day7/testInput1.txt"
chosenPath = inputPath

def parseInput(path):
    result = []
    def convertToNum(n):
        if n.isnumeric():
            return int(n)
        else:
            return n
    file = open(path, 'r')
    for line in file.readlines():
        line = (line.replace('\n','').split(' '))     
        line = list(map(lambda x: convertToNum(x), line))
        result.append(line)
    result = list(map(lambda x: {'hand':x[0], 'bet': x[1]}, result))
    return(result)

def appendHandType(input):
    def makeCountObj(hand):
        arr = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
        results = {}
        for card in arr:
            results[card] = 0
        for card in str(hand):
            results[card] = results[card] + 1
        for card in arr:
            if results[card] == 0:
                del results[card]
        return results
        
    for cards in input:
        countOfCards = makeCountObj(cards['hand'])
        cardRepetitions = list(countOfCards.values())
        
        numberOfDistinctCards = len(countOfCards.keys())
        if numberOfDistinctCards == 1:
            cards['type'] = "Five of a kind"
        if numberOfDistinctCards == 2:
            if cardRepetitions.__contains__(3):
                cards['type'] = "Full House"
            else:
                cards['type'] = "Four of a kind"
        if numberOfDistinctCards == 3:
            if cardRepetitions.__contains__(2):
                cards['type'] = "Two pair"
            else:
                cards['type'] = "Three of a kind"
        if numberOfDistinctCards == 4:
            cards['type'] = "One pair"
        if numberOfDistinctCards == 5:
            cards['type'] = "High card"
    
def groupByType(input):
    fiveOfAKind = []
    fourOfAKind = []
    fullHouse = []
    threeOfAKind = []
    twoPair = []
    onePair = []
    highCard = []
    
    for cards in input:
        if cards['type'] == "Five of a kind":
            fiveOfAKind.append(cards)
        if cards['type'] == "Four of a kind":
            fourOfAKind.append(cards)
        if cards['type'] == "Full House":
            fullHouse.append(cards)
        if cards['type'] == "Three of a kind":
            threeOfAKind.append(cards)
        if cards['type'] == "Two pair":
            twoPair.append(cards)
        if cards['type'] == "One pair":
            onePair.append(cards)
        if cards['type'] == "High card":
            highCard.append(cards)
    result = [fiveOfAKind, fourOfAKind, fullHouse, threeOfAKind, twoPair, onePair, highCard]
    result = list(filter(lambda x: x != [], result))
    return result

def assignOrderValue(arr):
    faceValues = [['A', 14],['K',13],['Q',12],['J',11],['T', 10]]
    def sortCardType(hands):
        def getCardValue (card):
            if card.isnumeric():
                return '0' + card
            else:
                return list(filter(lambda x: x[0] == card, faceValues))[0][1]
            
        for hand in hands:
            cardString = ''
            for i in range(5):
                thisCard = (str(hand['hand'])[i])
                cardValue = str(getCardValue(thisCard))
                cardString = cardString + cardValue
            hand['numberValue'] = int(cardString)
        return(hands)
    result = []
    for hand in arr:
        result.append(sortCardType(hand))
    return result
    
def sortCollections(groupedCards):
    def sortCollection(collection):
        sortedCollection = sorted(collection, key=lambda x: x['numberValue'], reverse=True)
        return(sortedCollection)
    result = []
    for collection in groupedCards:
        result = result + sortCollection(collection)
    resultLen = len(result)
    total = 0
    for i in range(resultLen):
        modifier = (resultLen - i)
        total = total + (result[i]['bet'] * modifier)
    print(total)
        

input = parseInput(chosenPath)
appendHandType(input)
groupedCards = groupByType(input)
assignOrderValue(groupedCards)
sortCollections(groupedCards)

