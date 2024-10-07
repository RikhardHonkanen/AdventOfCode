#################
### SPOILERS  ###
### FOR DAY 1 ###
### OF AOC    ###
#################

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
    "nine":     "9"
}

def find_lowest_index_character(indexes):
    lowest = -1
    answer = 0
    for pair in indexes:
        for key in pair:
            if ((pair[key] != -1 and pair[key] < lowest) or lowest == -1 ):
                lowest = pair[key]
                answer = key
    return answer  
    

def find_first_int_index(cal):
    for idx, char in enumerate(cal):
            if (char.isdigit()):
                return { char: idx }

def find_first_number_as_string_indexes(cal, reverse = False):
    word_index_map = []
    for key in numbers_as_words.keys():  
        compare = key if not reverse else reversed(key)
        if compare in cal:
            word_index_map.append({ numbers_as_words[key]: cal.index(compare) }) 
        else:
            word_index_map.append({ numbers_as_words[key]: -1 }) 
    return word_index_map

def parse_coordinates(calibration_values):
    for jumbled_string in calibration_values:
        first_char = get_first_coordinate(jumbled_string)
        second_char = get_last_coordinate(jumbled_string)
        results.append(str(first_char) + str(second_char))    

def get_first_coordinate(cal):  
    first_int_index = find_first_int_index(cal)
    word_indexes = find_first_number_as_string_indexes(cal)
    word_indexes.append(first_int_index)
    coordinate = find_lowest_index_character(word_indexes)
    return coordinate

def get_last_coordinate(cal):
    reversed_cal = reversed(cal)    
    first_int_index = find_first_int_index(reversed_cal)
    word_indexes = find_first_number_as_string_indexes(reversed_cal, True)
    word_indexes.append(first_int_index)
    coordinate = find_lowest_index_character(word_indexes)
    return coordinate

def add_all_coordinates(results):
    sum = 0
    for res in results:
        sum += int(res)
    return sum

def parse_file(path):
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split("\n")
	return parsed_input

results = []
calibration_values = parse_file('1.txt')
parse_coordinates(calibration_values)
answer = add_all_coordinates(results)
print(answer)