###################################
####### SPOILERS FOR DAY 02 #######
###################################

import os, sys

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input
        
def parse_single_line(line):
    parts = line.split(' ')
    threshholds = parts[0].split('-')
    lower_threshhold = threshholds[0]
    upper_threshhold = threshholds[1]
    character = parts[1][0]
    password = parts[2]
    
    return lower_threshhold, upper_threshhold, character, password
    
def count_correct_passwords(input):
    count = 0
    for line in input:
        lower_threshhold, upper_threshhold, character, password = parse_single_line(line)
        occurences = password.lower().count(character)
        if (occurences >= int(lower_threshhold) and occurences <= int(upper_threshhold)):
            count += 1            
    return count      

def count_new_policy_passwords(input): 
    count = 0
    for line in input:
        first_position, second_position, character, password = parse_single_line(line)
        if (password[int(first_position) - 1] == character):
            if (password[int(second_position) - 1] != character):
                count += 1
        else:
            if (password[int(second_position) - 1] == character):
                count += 1           
    return count 

def part_one(input):
    answer = count_correct_passwords(input)
    return answer

def part_two(input):
    answer = count_new_policy_passwords(input)
    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 2, 1
    test_input, input = parse_file("2test.txt"), parse_file("2.txt")
    print(f"Part 1 Test: {part_one(test_input)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_input)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    print(f"Part 2: {part_two(input)}")