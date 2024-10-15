###################################
####### SPOILERS FOR DAY 09 #######
###################################
##### PLEASE INSERT FUNNYBONE #####
###################################

import os, sys

debug = False

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def print_debug(string):
    if (debug):
        print(string)
        
def check_index(input, considered_idx, preamble_length):
    for i in range(considered_idx - preamble_length, considered_idx - 1):
            for j in range((considered_idx - preamble_length) + 1, considered_idx):
                if int(input[i]) + int(input[j]) == int(input[considered_idx]):
                    return True
    return False

def part_one(input, preamble_length, _debug = False):
    if (_debug):
        global debug
        debug = True
    considered_idx = preamble_length
    while (True):        
        if not check_index(input, considered_idx, preamble_length):
            return input[considered_idx], considered_idx
        else:
            considered_idx += 1

def part_two(input, preamble_length, _debug = False):
    if (_debug):
        global debug
        debug = True
    
    invalid_number, invalid_idx = part_one(input, preamble_length)
    
    working_sum = input[0]    
    for i in range(0, invalid_idx):
        if working_sum + input[i + 1] == invalid_number:
            print(input[i])
            print(input[i + 1])
        
    answer = 'Part two'            
    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 127, 0
    test_input, input = parse_file("9test.txt"), parse_file("9.txt")
    # print(f"Part 1 Test: {part_one(test_input, 5, False)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_input, 5, False)} (expected {P2TEST})")
    # print()
    # print(f"Part 1: {part_one(input, 25)}")
    # print(f"Part 2: {part_two(input)}")