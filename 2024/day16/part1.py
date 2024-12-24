import heapq
testPath = 'adventofcode/2024/day16/testInput.txt'
inputPath = 'adventofcode/2024/day16/input.txt'
chosenPath = testPath

def parseInput(path):
    file = open(path, 'r')
    rows = file.readlines()
    nodes = []
    graph = {}
    for y, row in enumerate(rows):
        for x, node in enumerate(row):
            if node in '.SE':
                nodes.append((x, y))
    for node in nodes:
        edge = {}
        weight = 1
        x, y = node
        nswe = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
        for direction in nswe:
            if direction in nodes:
                edge[direction] = weight
        graph[node] = edge

    startCood = [node for node in nodes if rows[node[1]][node[0]] == 'S'][0]
    endCoord = [node for node in nodes if rows[node[1]][node[0]] == 'E'][0]
    return graph, startCood, endCoord

def getShortestPath(graph, startCoord, endCoord):
    queue = [(0, startCoord, 'horizontal')] # score, node, direction 
    scores = {node: float('infinity') for node in graph}
    scores[startCoord] = 0
    while queue:
        currentScore, currentNode, prevDir = heapq.heappop(queue)
        if currentScore > scores[currentNode]:
            continue
        for adjacentNode, moveCost in graph[currentNode].items():
            currentDir = 'vertical' if adjacentNode[0] == currentNode[0] else 'horizontal'
            turnPenalty = 1000 if prevDir and currentDir != prevDir else 0
            score = currentScore + moveCost + turnPenalty
            if score < scores[adjacentNode]:
                scores[adjacentNode] = score
                heapq.heappush(queue, (score, adjacentNode, currentDir))
    return scores[endCoord]

graph,startCood,endCoord = parseInput(chosenPath)
min_score = getShortestPath(graph, startCood, endCoord)
print(f'min score: {min_score}')
