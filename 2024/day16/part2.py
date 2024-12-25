from collections import deque
import heapq
test_path = 'adventofcode/2024/day16/testInput.txt'
input_path = 'adventofcode/2024/day16/input.txt'

class Maze:
    COST = 1
    PENALTY = 1000
    def __init__(self, path):
        self.puzzle_input = path
        self.grid = [list(line.strip()) for line in open(path)]
        self.start_coord = self.get_start()

    def get_start(self):
        for x, row in enumerate(self.grid):
            for y, node in enumerate(row):
                if node == 'S':
                    start_coord = (x, y)
                    break
                else:
                    continue
        return start_coord
                
def get_good_seats(maze):
    start_row, start_col = maze.start_coord
    pending_queue = []
    # initialize pending_queue with starting_values for cost, row, col, row_dir, col_dir
    heapq.heappush(pending_queue,(0, start_row, start_col, 0, 1)) 
    lowest_cost = {(start_row, start_col, 0, 1): 0}
    backtrack = {}
    best_cost = float("inf")
    end_states = set()

    while pending_queue:
        cost, row, col, row_dir, col_dir = heapq.heappop(pending_queue)
        if cost > lowest_cost.get((row, col, row_dir, col_dir), float('inf')): continue
        lowest_cost[(row, col, row_dir, col_dir)] = cost
        if maze.grid[row][col] == "E":
            if cost > best_cost: break
            best_cost = cost
            end_states.add((row, col, row_dir, col_dir)) # track end states and directions (for backtracking)
        next_directions = [
            (cost + maze.COST, row + row_dir, col + col_dir, row_dir, col_dir),
            (cost + maze.PENALTY, row, col, col_dir, -row_dir),
            (cost + maze.PENALTY, row, col, -col_dir, row_dir)
        ]
        for new_cost, next_row, next_col, next_row_dir, next_col_dir in next_directions:
            if maze.grid[next_row][next_col] == "#": continue
            curr_lowest = lowest_cost.get((next_row, next_col, next_row_dir, next_col_dir), float('inf'))
            if new_cost > curr_lowest: continue # skp if cost is higher than current lowest.
            if new_cost == curr_lowest: # add to backtrack.
                backtrack[(next_row, next_col, next_row_dir, next_col_dir)].add((row, col, row_dir, col_dir))
            if new_cost < curr_lowest: # reset and add to backtrack.
                backtrack[(next_row, next_col, next_row_dir, next_col_dir)] = set()
                backtrack[(next_row, next_col, next_row_dir, next_col_dir)].add((row, col, row_dir, col_dir))
                lowest_cost[(next_row, next_col, next_row_dir, next_col_dir)] = new_cost
            heapq.heappush(pending_queue, (new_cost, next_row, next_col, next_row_dir, next_col_dir))
    
    # bfs to find all states leading to end states.
    states = deque(end_states)
    print(states)
    seen = set(end_states)
    while states:
        key = states.popleft()
        for last in backtrack.get(key, []):
            if last in seen: continue
            seen.add(last)
            states.append(last)
    return(len({(row, col): maze.grid[row][col] for row, col, _, _ in seen}))

chosen_path = input_path
maze = Maze(chosen_path)
good_seats_count = get_good_seats(maze)
print(f'there are {good_seats_count} good seats')

