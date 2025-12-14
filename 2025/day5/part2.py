test = '2025/day5/testInput.txt'
actual = '2025/day5/input.txt'
chosenPath = actual

def parse_input (path):
    file = open(path, 'r')
    fresh = []
    file = [line.strip('\n') for line in file]
    for line in file:
        if '-' in line:
            start, end = [int(n) for n in line.split('-')]
            fresh.append({"start":start, "end":end})
    return fresh

def stringify(ranges):
    '''
    helper function to make displaying ranges in console a little easier to visualize
    '''
    return ', '.join([f"{range['start']}-{range['end']}" for range in ranges])

def find_overlap(this_id, other_ids):
    '''
        reviews the range provided them and classifies it for additional action. can be 'none', 'full', or 'partial'
    '''
    full_overlap_list = [id for id in other_ids if id["start"] <= this_id["start"] <= id["end"] and id["start"] <= this_id["end"] <= id["end"]]
    partial_overlap_list = [id for id in other_ids if id["start"] <= this_id["start"] <= id["end"] or id["start"] <= this_id["end"] <= id["end"]]
    if len(full_overlap_list) > 0:
        return 'full'
    if len(partial_overlap_list) > 0:
        return 'partial'
    if len(partial_overlap_list) == 0:
        return 'none'
    
def split_range(this_id, other_ids):
    '''
    partials need to be broken up so that there's no overlap. consider the following:

        50-100 => 45-100 (based on overlap with 45-55)
        45-55 => 45-100 (based on overlap with 50-100)
        200-300 => 200-320 (based on overlap with 290-320)
        290-320 => 200-510 (based on overlap with both 200-300 and 310-510)
        500-600 => 310-600 (based on 310-510)
        310-510 => 290-600 (based on 290-320 and 500-600)

    '''
    partial_overlap_list = [id for id in other_ids if id["start"] <= this_id["start"] <= id["end"] or id["start"] <= this_id["end"] <= id["end"]]
    min_start = min([id["start"] for id in partial_overlap_list] + [this_id["start"]])
    max_end = max([id["end"] for id in partial_overlap_list] + [this_id["end"]])
    print(f"    overlap for {stringify([this_id])} is partial with {stringify(partial_overlap_list)}")
    return [{"start":min_start, "end":max_end}]


def alter_ingredients_ranges(ingredients):
    '''
    review the list of ingredients, classify, and return an simplified list of ingredients that does not 
    contain overlap or redundancies
    '''
    new_ingredients = ingredients.copy()
    def get_other_ids (this_id, full_list):
        return [id for id in full_list if id != this_id]
    
    for this_id in ingredients:
        other_ids = get_other_ids(this_id, ingredients)
        # print(stringify([this_id]),'|',stringify(ingredients))
        overlap_type = find_overlap(this_id, other_ids) # returns 'none', 'full', or 'partial'
        if overlap_type == 'none':
            continue
        if overlap_type == 'full':
            new_ingredients = [id for id in new_ingredients if id != this_id]
        if overlap_type == 'partial':
            split_range_list = split_range(this_id, other_ids)
            new_ingredients = [id for id in new_ingredients if id != this_id] + split_range_list
    
    overlap_types = [find_overlap(id,get_other_ids(id,new_ingredients)) for id in new_ingredients]
    
    if all(str == 'none' for str in overlap_types):
        unique_ingredient_ranges = [dict(frozen_set) for frozen_set in set(frozenset(food.items()) for food in new_ingredients)]
        return unique_ingredient_ranges
    else:
        return alter_ingredients_ranges(new_ingredients)
        
def get_sum(ranges):
    totals = []
    for range in ranges:
        start = range['start']
        end = range['end'] + 1
        totals.append(end - start)
    print(totals)
    return sum(totals)


fresh_ingredient_ids = parse_input(chosenPath)
fresh_ingredient_ids = alter_ingredients_ranges(fresh_ingredient_ids)
print('\n')
print(stringify(fresh_ingredient_ids))
print(get_sum(fresh_ingredient_ids))


