test = '2025/day5/testInput.txt'
actual = '2025/day5/input.txt'
chosenPath = actual

def parse_input (path):
    file = open(path, 'r')
    fresh = []
    available = []
    file = [line.strip('\n') for line in file]
    for line in file:
        if '-' in line:
            start, end = [int(n) for n in line.split('-')]
            fresh.append({"start":start, "end":end})
        elif line == '':
            continue
        else:
            available.append(int(line))
    return {"fresh_ids": fresh, "available_ids": available}

fresh_ingredient_ids = parse_input(chosenPath)["fresh_ids"]
available_ingredient_ids = parse_input(chosenPath)["available_ids"]

def is_fresh(number):
    is_fresh = False
    for ingredient_range in fresh_ingredient_ids:
        if number >= ingredient_range["start"] and number <= ingredient_range["end"]:
            print(f"{number} is fresh")
            is_fresh = True
            return is_fresh
    print(f"{number} is spoiled")
    return is_fresh

def get_available_fresh():
    available_fresh = []
    for id in available_ingredient_ids:
        if is_fresh(id) == True:
            available_fresh.append(id)
    return available_fresh

print(len(get_available_fresh()))
