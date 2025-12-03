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


def review_number (input_num):
    num_string = str(input_num)

    def trim_zeroes(original_string):
        trimmed_string = original_string.lstrip('0')
        return trimmed_string
    
    num_string = trim_zeroes(num_string)

    str_len = len(num_string)
    num_prefix, num_suffix = num_string[0:int(str_len/2)], num_string[(int(str_len/2)):]
    if num_prefix == num_suffix:
        return input_num

def get_invalid_number_sum():
    invalid_numbers = []
    for number_arr in ranges:
        for num in number_arr:
            review_results = review_number(num)
            if review_results != None: invalid_numbers.append(review_results)
    invalid_numbers_total = sum(invalid_numbers)
    return invalid_numbers_total

result = get_invalid_number_sum()
print(result)

