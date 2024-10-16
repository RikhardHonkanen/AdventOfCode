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
    invalid_number = int(invalid_number)
    
    working_sum = int(input[0])
    encryption_weakness_range = []
    for i in range(0, invalid_idx - 1):
        if working_sum > invalid_number:
            working_sum = int(input[i + 1])
            continue
        for j in range(i + 1, invalid_idx):
            working_sum += int(input[j])
            if working_sum == invalid_number:
                encryption_weakness_range = input[i: j + 1]
                break
            elif working_sum > invalid_number:
                continue
                
    encryption_weakness_range.sort()    
    return int(encryption_weakness_range[0]) + int(encryption_weakness_range[-1])

if __name__ == "__main__":
    P1TEST, P2TEST = 127, 62
    test_input, input = parse_file("9test.txt"), parse_file("9.txt")
    print(f"Part 1 Test: {part_one(test_input, 5, False)[0]} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_input, 5, False)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input, 25)[0]}")
    print(f"Part 2: {part_two(input, 25)}")