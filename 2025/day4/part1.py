test = '2025/day4/testInput.txt'
actual = '2025/day4/input.txt'
chosenPath = actual

def parse_input (path):
    file = open(path, 'r')
    result = []
    for col_y, line in enumerate(file):
        row = list(line.strip('\n'))
        for row_x, warehouse_space in enumerate(row):
            has_roll = True if warehouse_space == '@' else False
            result.append({"coord":(row_x, col_y),"has_roll": has_roll, "symbol": warehouse_space}) 
    return result
roll_room = parse_input(chosenPath)


def is_accessible (roll_being_evaluated):
    current_coord = roll_being_evaluated["coord"]
    if roll_being_evaluated["has_roll"] == False:
        return False
    
    def get_adjacent_list(current_coord):
        '''
        get the list of adjacent coordinates. Note: this fn will 
        return invalid coords (e.g. (-1,-1)). We'll filter those out in the later steps.
        '''
        x = current_coord[0]
        y = current_coord[1]
        adjacent_coords = []
        for row in range(-1,2):
            for col in range(-1,2):
                adjacent_coord = (x+row,y+col)
                if adjacent_coord != current_coord:
                    adjacent_coords.append(adjacent_coord)
        return adjacent_coords

    def get_adjacent_dict_items(coords_list, data_list):
        '''
        loop through the list of adjacent rolls and return the dictionaries
        of the rolls present in the roll room. This eliminates any invalid
        coordinates and includes the key "has_roll" which can be used for later
        calculations.
        '''
        filtered_data = [
            roll for roll in data_list
            for coord in coords_list
            if roll.get('coord') == coord
        ]
        return filtered_data
    
    def count_rolls(list_of_rolls):
        '''
        returns the count of how many rolls are adjacent to roll_being_evaluated
        '''
        count = 0
        for roll in list_of_rolls:
            if roll.get('has_roll') == True:
                count += 1
        return count
    
    def is_under_limit(limit):
        if total_rolls < limit:
            roll_being_evaluated["symbol"] = 'x'
            return True
        return False
    
    adjacent_coords = get_adjacent_list(current_coord)
    adjacent_dict_items = get_adjacent_dict_items(adjacent_coords, roll_room)
    total_rolls = count_rolls(adjacent_dict_items)
    return is_under_limit(4)
    

def check_roll_room(roll_room):
    roll_counts = 0
    for roll in roll_room:
        if is_accessible(roll):
            roll_counts += 1
            print(f"{roll["coord"]} is accessible")
    return roll_counts

print(check_roll_room(roll_room))

def visualized_solution():
    roll_map = [roll["symbol"] for roll in roll_room]
    chunked_map = [roll_map[n:n+10] for n in range(0,len(roll_map),10)]
    for chunk in chunked_map:
        print(''.join(chunk))
    return

# print(visualized_solution())
