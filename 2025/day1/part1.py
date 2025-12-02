test = '2025/day1/testInput.txt'
actual = '2025/day1/input.txt'
chosenPath = actual

def parse_input (path):
    file = open(path, 'r')
    result = []
    for x, line in enumerate(file):
        direction, steps = line[0], line[1:].strip('\n')
        result.append({"direction":-1 if direction == 'L' else 1, "steps":int(steps)})
    return result

clean_input = parse_input(chosenPath)

def turn_dial(next_move, pos):
    steps = next_move["steps"]
    modifier = next_move["direction"]
    pos = 50 if pos == None else pos
    for _ in range (next_move["steps"]):
        if pos + modifier == -1:
            pos = 99
        elif pos + modifier == 100:
            pos = 0
        else:
            pos = pos + modifier
    print(f'after turning {'R' if modifier > 0 else 'L'} {steps} times, the position is {pos}')
    return (pos, True if pos == 0 else False)

def get_password():
    position = None
    zeroes = 0
    for input in clean_input:
        position, bool = turn_dial(input, position)
        print(f"{position} is {bool}")
        zeroes = zeroes + 1 if bool else zeroes
    return zeroes

print(get_password())
