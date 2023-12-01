import os, sys

numbers_as_words = {
    "one":      "1",
    "two":      "2",
    "three":    "3",
    "four":     "4",
    "five":     "5",
    "six":      "6",
    "seven":    "7",
    "eight":    "8",
    "nine":     "9",
}

def find_first_number_as_string(cal):
    for key in numbers_as_words.keys():  
        if key in cal:
            return numbers_as_words[key]  

def parse_coordinates(calibration_values):
    for jumbled_string in calibration_values:
        first_char = get_first_coordinate(jumbled_string)
        second_char = get_last_coordinate(jumbled_string)
        results.append(str(first_char) + str(second_char))    

def get_first_coordinate(cal):  
    if (find_first_number_as_string(cal)):
        return find_first_number_as_string(cal)
    else:
        for char in cal:
            if (char.isdigit()):
                return char

def get_last_coordinate(cal):
    reversed_cal = reverse_string(cal)    
    if (find_first_number_as_string(reversed_cal)):
        return find_first_number_as_string(reversed_cal)
    else:
        for char in cal:
            if (char.isdigit()):
                return char

def parse_file(path):
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split("\n")
	return parsed_input

def add_all_coordinates(results):
    sum = 0
    for res in results:
        sum += int(res)
    return sum

def reverse_string(input):
  return input[::-1]

results = []
calibration_values = parse_file('input.txt')
single_coordinate = parse_coordinates(calibration_values)
answer = add_all_coordinates(results)
print(answer)