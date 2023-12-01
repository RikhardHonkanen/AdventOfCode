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

ahtwo3safhaoguwenola1ad

def clean_up_inputs(calibration_values):
    clean_calibration_values = []
    for string in calibration_values:
        clean_string = string
        for key in numbers_as_words.keys():  
            if key in clean_string:
                clean_string = string.replace(key, numbers_as_words[key])
        clean_calibration_values.append(clean_string)
    return clean_calibration_values        

def parse_coordinates(calibration_values):
    for jumbled_string in calibration_values:
        first_char = get_first_coordinate(jumbled_string)
        second_char = get_last_coordinate(jumbled_string)
        results.append(str(first_char) + str(second_char))    

def get_first_coordinate(cal):    
    for char in cal:
        if (char.isdigit()):
            return char

def get_last_coordinate(cal):
    reversed_cal = reverse_string(cal)    
    for char in reversed_cal:
        if char.isdigit():
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
clean_calibration_values = clean_up_inputs(calibration_values)
single_coordinate = parse_coordinates(clean_calibration_values)
answer = add_all_coordinates(results)
print(answer)