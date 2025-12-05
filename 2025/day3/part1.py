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
    bank_list = list(bank)
    ten_result = max(bank_list[0:len(bank)-1])
    tens_position = bank_list.index(ten_result)
    ones_list = bank_list[tens_position + 1:]
    one_result = max(ones_list)
    result = int(str(ten_result)+ str(one_result))
    print(f"largest joltage is {result}")
    return result

def get_total_jolts (battery_stack):
    joltages = []
    for battery_row in battery_stack:
        joltages.append(largest_joltage(battery_row))
    return sum(joltages)

answer = get_total_jolts(battery_banks)
print(answer)
