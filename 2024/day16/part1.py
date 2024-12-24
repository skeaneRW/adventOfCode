from collections import deque
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
        cost = 1
        x, y = node
        if (x, y + 1) in nodes:
            edge[(x, y + 1)] = cost
        if (x + 1, y) in nodes:
            edge[(x + 1, y)] = cost
        if (x, y - 1) in nodes:
            edge[(x, y - 1)] = cost
        if (x - 1, y) in nodes:
            edge[(x - 1, y)] = cost
        graph[node] = edge

    startCood = [node for node in nodes if rows[node[1]][node[0]] == 'S'][0]
    endCoord = [node for node in nodes if rows[node[1]][node[0]] == 'E'][0]
    return graph, startCood, endCoord

graph,startCood,endCoord = parseInput(chosenPath)

def getAllPathSequences(graph, startCoord, endCoord):
# get all the sequences of paths that go from the start to the end without backtracking
    paths = []
    queue = deque()
    queue.append([startCoord])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == endCoord:
            paths.append(path)
        for neighbor in graph[node]:
            if neighbor not in path:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return paths

def renderMap(path, graph, startCoord, endCoord):
    maxY = max([coord[1] for coord in graph.keys()])
    maxX = max([coord[0] for coord in graph.keys()])
    for y in range(maxY + 2):
        for x in range(maxX + 2):
            if (x, y) == startCoord:
                print('S', end='')
            elif (x, y) == endCoord:
                print('E', end='')
            elif (x, y) in path:
                print('.', end='')
            elif (x, y) in graph:
                print(' ', end='')
            else:
                print('#', end='')
        print()

allPaths = getAllPathSequences(graph, startCood, endCoord)

costs = {}
for i, path in enumerate(allPaths):
    print(f'\nPath {i}:')
    direction = 'horizontal'
    cost = 0
    movingEastFromStart = startCood[0] < path[1][0]
    if not movingEastFromStart:
        cost += 1000
    for j, step in enumerate(path):
        if j == len(path) - 1:
            break
        if direction == 'horizontal' and path[j][0] != path[j + 1][0]:
            direction = 'vertical'
            cost += 1000
        if direction == 'vertical' and path[j][1] != path[j + 1][1]:
            direction = 'horizontal'
            cost += 1000    
        cost += 1
    costs[i] = cost
    print(f'{len(path)-1} steps; cost:{cost}')
    print(path)
    renderMap(path, graph, startCood, endCoord)
    
print(f'min cost = {min(costs.values())}')
