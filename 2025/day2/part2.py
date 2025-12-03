test = '2025/day2/testInput.txt'
actual = '2025/day2/input.txt'
chosenPath = actual

def parse_input (path):
    file = open(path, 'r')
    result = []
    for line in file:
        row = line.split(',')
        for number_range in row:
            base_number, end_number = number_range.split('-')
            base_number, end_number = int(base_number), int(end_number)
            this_range = []
            for i in range (base_number, end_number + 1):
                this_range.append(base_number)
                base_number += 1
            result.append(this_range)
        
    return result

ranges = parse_input(chosenPath)

def get_invalid_numbers (input_num):
    num_string = str(input_num)
    str_len = len(num_string)

    def all_chars_are_identical(array_of_numbers):
        if len(array_of_numbers)>1:
            return all(each_number == str(array_of_numbers[0]) for each_number in array_of_numbers)

    if all_chars_are_identical(list(num_string)):
        return input_num
    
    if str_len > 3:
        for i in range(int(str_len/2),1,-1):
            if float(str_len/i).is_integer():
                set_len = int(str_len/i)
                string_sets = []
                for count, x in enumerate(range(0,str_len,set_len)):
                    count += 1
                    string_sets.append(num_string[x:count * set_len])
                if all_chars_are_identical(string_sets):
                    return input_num    
    return


def get_invalid_number_sum():
    invalid_numbers = []
    numbers_reviewed = 0
    for number_arr in ranges:
        for i, num in enumerate(number_arr):
            numbers_reviewed += 1
            review_results = get_invalid_numbers(num)
            if review_results != None: invalid_numbers.append(review_results)
    invalid_numbers_total = sum(invalid_numbers)
    return invalid_numbers_total

result = get_invalid_number_sum()
print(result)

