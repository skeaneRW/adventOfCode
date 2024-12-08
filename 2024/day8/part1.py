import itertools

testPath = './testInput.txt'
inputPath = './input.txt'
chosenPath = inputPath

def parseInput(path):
    frequencies = {}
    with open(path, 'r') as file:
        frequencies = {}
        strings = [line.strip() for line in file.readlines()]
        map = [list(string) for string in strings]
        for y, col in enumerate(map):
            for x, char in enumerate(col):
                if char != '.':
                    frequencies[char] = []
        for y, col in enumerate(map):
            for x, char in enumerate(col):
                if char != '.':
                    frequencies[char].append((x, y))
        return (frequencies, map)
    
input, map = parseInput(chosenPath)

def getAntiNodes(key, frequencies):
    print(f'key: {key} appears in map {len(frequencies)} times:  {frequencies}\n')
    pairings = list(itertools.combinations(frequencies, 2))
    def coordIsOffMap(coord):
        x, y = coord
        return x < 0 or x >= len(map[0]) or y < 0 or y >= len(map)
    antinodes = []
    for pair in pairings:
        #print(f'pair: {pair[0]} and {pair[1]}')
        distanceBetweenY = (pair[1][1] - pair[0][1])
        distanceBetweenX = (pair[1][0] - pair[0][0])
        #print(f'distance between: {distanceBetweenX}, {distanceBetweenY}')
        antiNode1 = (pair[0][0] - distanceBetweenX, pair[0][1] - distanceBetweenY)
        antiNode2 = (pair[1][0] + distanceBetweenX, pair[1][1] + distanceBetweenY)
        #print(f'antiNode1 for {pair[0]}: {antiNode1}')
        #print(f'antiNode2 for {pair[1]}: {antiNode2}\n')
        if not coordIsOffMap(antiNode1):
            antinodes.append(antiNode1)
        if not coordIsOffMap(antiNode2):
            antinodes.append(antiNode2)
    return antinodes
        
        
result = []
for key in input:
    antiNodesByKey = (getAntiNodes(key, input[key]))
    for coord in antiNodesByKey:
        if coord not in result:
            result.append(coord)

print(f'antiNodes: {len(result)}')


