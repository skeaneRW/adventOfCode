test = '2025/day3/testInput.txt'
actual = '2025/day3/input.txt'
chosenPath = actual

def parse_input (path):
    file = open(path, 'r')
    result = []
    for line in file:
        result.append(line.strip('\n'))
    return result

battery_banks = parse_input(chosenPath)

def largest_joltage (bank):
    # print(f"\nevaluating {bank}")
    solution = []
    bank_list = list(bank)
    list_index = 0
    starting_pos = 0
    for ending_pos in range(11,-1,-1):
        print(ending_pos)
        beginning_part = bank_list[0:starting_pos]
        middle_part = bank_list[starting_pos:len(bank_list)-ending_pos]
        # ending_part = bank_list[len(beginning_part) + len(middle_part):]
        # print(f"    {beginning_part},{middle_part},{ending_part}")
        # print(f"    beginning: [0:{starting_pos}], middle: [{starting_pos}:{len(bank_list)-ending_pos}], end: [{len(beginning_part) + len(middle_part)}:]")
        # if len(middle_part):
        max_digit = max(middle_part)
        solution.append(max_digit)
        list_index = middle_part.index(max_digit) + 1
        starting_pos = len(beginning_part)  + list_index 
        ending_pos += 1
    solution = int(''.join(solution))
    print(f"    {bank} => {solution}")
    return solution

def get_total_jolts (battery_stack):
    joltages = []
    for battery_row in battery_stack:
        joltages.append(largest_joltage(battery_row))
    return sum(joltages)

answer = get_total_jolts(battery_banks)
print(answer)

