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
    zero_counter = 0
    steps = next_move["steps"]
    modifier = next_move["direction"]
    pos = 50 if pos == None else pos
    for _ in range (next_move["steps"]):
        if pos + modifier == -1:
            pos = 99
        elif pos + modifier == 100:
            pos = 0
            zero_counter += 1
        elif pos + modifier == 0:
            pos = pos + modifier
            zero_counter += 1
        else:
            pos = pos + modifier
    print(f' {'R' if modifier > 0 else 'L'}:{steps} => {pos}')
    return (pos, zero_counter)

def get_password():
    position = None
    zeroes = 0
    for input in clean_input:
        position, zero_counter = turn_dial(input, position)
        print(f"this hits zero {zero_counter} times")
        zeroes += zero_counter
    return zeroes

print(get_password())
