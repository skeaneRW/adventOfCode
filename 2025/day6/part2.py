test = '2025/day6/testInput.txt'
actual = '2025/day6/input.txt'
chosenPath = actual

def parse_input (path):
    file = open(path, 'r')
    number_lists = []
    operators = None
    file = [line.strip('\n') for line in file]
    for line in file:
        if '*' not in line or '+' not in line:
            line_dict = {}
            for i, char in enumerate(line):
                line_dict[i] = char
            number_lists.append(line_dict)
        else:
            def is_not_empty(char):
                return char != ''
            operators = list(filter(is_not_empty,line.split(' ')))
    return {"num_lists": number_lists, "operators":operators}


def get_result (input):
    num_lists = input["num_lists"]
    operators = input["operators"]
    key_count = len(num_lists[0])
    starting_list = []
    for i in range(key_count,0,-1):
        idx = (i-1)
        this_number = ''.join([num[idx] for num in num_lists]).strip()
        starting_list.append(this_number)
    
    sublists = []
    current_sublist = []
    for item in starting_list:
        if item == '':
            if current_sublist:
                sublists.append(current_sublist)
            current_sublist = [item]
        else:
            current_sublist.append(item)
    if current_sublist:
        sublists.append(current_sublist)
    def not_empty(n):
        return n != ''
    sublists = [ list(filter(not_empty,arr)) for arr in sublists]
    int_sublists = [[int(n) for n in num_str ] for num_str in sublists]
    totals = []
    for i, symbol in enumerate(reversed(operators)):
        total = 0 if symbol == '+' else 1
        for number in int_sublists[i]:
            total = number + total if symbol == '+' else number * total
        totals.append(total)
    return(sum(totals))

parsed_input = parse_input(chosenPath)
result = get_result(parsed_input)
print(result)