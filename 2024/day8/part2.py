import itertools
# import sys
# limit = 10 ** 6
# sys.setrecursionlimit(limit)

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

def renderAntinodes(antinodes):
    for y, col in enumerate(map):
        for x, char in enumerate(col):
            if (x, y) in antinodes:
                print('#', end='')
            else:
                print(char, end='')
        print('')

def getAntiNodes(key, frequencies):
    print(f'key: {key} appears in map {len(frequencies)} times:  {frequencies}\n')
    pairings = list(itertools.combinations(frequencies, 2))
    def coordIsOffMap(coord):
        x, y = coord
        return x < 0 or x >= len(map[0]) or y < 0 or y >= len(map)
    
    antinodes = []

    def appendAntiNode1(pair):
        if not antinodes.__contains__(pair[0]):
            antinodes.append(pair[0])
        if not antinodes.__contains__(pair[1]):
            antinodes.append(pair[1])
        distanceBetweenY = (pair[1][1] - pair[0][1])
        distanceBetweenX = (pair[1][0] - pair[0][0])
        
        def getAntiNode1(coord):
            result = (coord[0] - distanceBetweenX, coord[1] - distanceBetweenY)
            if not coordIsOffMap(result):
                return result
            
        antiNode1 = getAntiNode1(pair[0])

        if antiNode1:
            antinodes.append(antiNode1)
            appendAntiNode1((antiNode1, pair[0]))

    def appendAntiNode2(pair):
        distanceBetweenY = (pair[1][1] - pair[0][1])
        distanceBetweenX = (pair[1][0] - pair[0][0])

        def getAntiNode2(coord):
            result = (coord[0] + distanceBetweenX, coord[1] + distanceBetweenY)
            if not coordIsOffMap(result):
                return result
            
        antiNode2 = getAntiNode2(pair[1])

        if antiNode2:
            antinodes.append(antiNode2)
            newPair = (pair[1], antiNode2)
            appendAntiNode2(newPair)
    
    for pair in pairings:
        appendAntiNode1(pair)
        appendAntiNode2(pair)

    renderAntinodes(antinodes)
    return antinodes
        
        
result = []
for key in input:
    antiNodesByKey = (getAntiNodes(key, input[key]))
    for coord in antiNodesByKey:
        if coord not in result:
            result.append(coord)

print(f'antiNodes: {len(result)}')


