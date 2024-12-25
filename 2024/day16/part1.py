import heapq
test_path = 'adventofcode/2024/day16/testInput.txt'
input_path = 'adventofcode/2024/day16/input.txt'
chosen_input = test_path

class Maze:
    MOVE_COST = 1
    TURN_PENALTY = 1000

    def __init__(self, path):
        self.puzzle_input = path
        self.graph, self.start_coord, self.end_coord = self.parse_input(path)

    def parse_input(self, puzzle_input):
        with open(puzzle_input, 'r') as file:
            rows = file.readlines()
        nodes = []
        graph = {}
        for y, row in enumerate(rows):
            for x, node in enumerate(row):
                if node in '.SE':
                    nodes.append((x, y))
        for node in nodes:
            x, y = node
            nswe = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
            graph[node] = [node for node in nswe if node in nodes]

        start_coord = [node for node in nodes if rows[node[1]][node[0]] == 'S'][0]
        end_coord = [node for node in nodes if rows[node[1]][node[0]] == 'E'][0]
        return graph, start_coord, end_coord

def getShortestPath(maze):
    print('looking for the score of the best path...')
    priority_queue = [(0, maze.start_coord, 'east')] # score, node, direction 
    visited = set()
    while priority_queue:
        score, node, direction = heapq.heappop(priority_queue)
        visited.add((score, node, direction))
        for new_score, new_node, new_direction in getNeighbors(maze, score, node, direction):
            if new_node == maze.end_coord:
                return new_score
            if (new_score, new_node, new_direction) not in visited:
                visited.add((new_score, new_node, new_direction))
                heapq.heappush(priority_queue, (new_score, new_node, new_direction))
    return visited

def getNeighbors(maze, score, node, direction):
    x, y = node
    neighbors = []
    directions = {
        'north': [((x, y-1), 'north'), ((x-1, y), 'west'), ((x+1, y), 'east')],
        'south': [((x, y+1), 'south'), ((x-1, y), 'west'), ((x+1, y), 'east')],
        'west': [((x-1, y), 'west'), ((x, y-1), 'north'), ((x, y+1), 'south')],
        'east': [((x+1, y), 'east'), ((x, y-1), 'north'), ((x, y+1), 'south')]
    }
    for new_node, new_direction in directions[direction]:
        if new_node in maze.graph[node]:
            new_score = score + maze.MOVE_COST
            if new_direction != direction:
                new_score += maze.TURN_PENALTY
            neighbors.append((new_score, new_node, new_direction))
    return neighbors

def get_best_paths(maze, target_score):
    print('  looking for the all the tracks that can score', target_score)
    priority_queue = [(0, maze.start_coord, 'east', [])] # score, node, direction, path
    best_paths = []
    while priority_queue:
        score, node, direction, path = heapq.heappop(priority_queue)
        if node == maze.end_coord:
            best_paths.append(path)
        for new_score, new_node, new_direction in getNeighbors(maze, score, node, direction):
            if new_score <= target_score:
                new_path = path.copy()
                new_path.append(new_node)
                heapq.heappush(priority_queue, (new_score, new_node, new_direction, new_path))
    best_paths = [path for path in best_paths if path[-1] == maze.end_coord] # filter out paths that don't end at the end node
    return best_paths

def score_best_paths(paths):
    print(f'  going through each of the {len(paths)} tracks to find the number of good seats')
    good_seats = set()
    good_seats.add(maze.start_coord)
    for path in paths:
        for seat in path:
            good_seats.add(seat)
    return len(good_seats)



maze = Maze(chosen_input)
min_score = getShortestPath(maze)
best_paths = get_best_paths(maze, min_score)
number_of_good_seats = score_best_paths(best_paths)
print()
print(f'the shortest path costs {min_score} points')
print(f'there are {number_of_good_seats} good seats in the maze!')