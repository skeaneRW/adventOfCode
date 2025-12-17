test = '2025/day6/testInput.txt'
actual = '2025/day6/input.txt'
chosenPath = actual

def parse_input (path):
    file = open(path, 'r')
    number_lists = []
    operators = None
    file = [line.strip('\n') for line in file]
    for line in file:
        new_line = line.split(' ')
        def is_not_empty(char):
            return char != ''
        new_line = list(filter(is_not_empty, new_line))
        new_line = [int(str) if str.isnumeric() else str for str in new_line ]
        if all(isinstance(d,int) for d in new_line):
            number_lists.append(new_line)
        else:
            operators = new_line
    return ({"num_lists":number_lists, "operators":operators})

def pivot(input):
    num_lists = input["num_lists"]
    operators = input["operators"]
    results = []
    for i in range(len(operators)):
        operator = operators[i]
        result = 0 if operator == '+' else 1
        for num_list in num_lists:
            if operator == '+':
                result = num_list[i] + result
            else:
                result = num_list[i] * result
        results.append(result)
    return results


parsed_input = (parse_input(chosenPath))
sums = pivot(parsed_input)
print(sum(sums))


