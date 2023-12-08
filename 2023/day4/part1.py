inputPath = "2023/day4/input.txt"
testPath = "2023/day4/testInput1.txt"

def parseInput(path):
    result = []
    file = open(path, "r")
    for line in file.readlines():
        input = line.split(': ')[1]
        card = line.split(': ')[0].replace('Card ', '')
        def isNumeric(char):
            return(str(char).isnumeric())
        winningNumbers = sorted(input.split(' | ')[0].split(' '))
        winningNumbers = list(filter(isNumeric, winningNumbers))
        scratchTicket = sorted(input.split(' | ')[1].replace('\n','').split(' '))
        scratchTicket = list(filter(isNumeric, scratchTicket))
        print(card)
        print(f'win: {winningNumbers}')
        print(f'you: {scratchTicket}')
        result.append({'card': card, 'winningNumbers': winningNumbers, 'scratchTicket': scratchTicket})
        
    return(result)

def appendPoints():
    for input in parsedInput:
        winList = (input.get('winningNumbers'))
        scratchList = (input.get('scratchTicket'))
        intersection = (list((set(winList) & set(scratchList))))
        if (len(intersection) > 0):
            n = 1
            for i in range(0, len(intersection)):
                if i > 0:
                    n = n * 2
            points.append(n)


parsedInput = parseInput(inputPath)
points = []
appendPoints()
print(sum(points))
        
    
