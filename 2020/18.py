###################################
####### SPOILERS FOR DAY 18 #######
###################################

import os, sys

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def print_debug(string):
    if (debug):
        print(string)

def part_one(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    for expression in input:
        pass
        
    print(input)
    exit()
    
    answer = 'Part one'            
    return answer

def part_two(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    answer = 'Part two'            
    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 122, 0
    test_input, input = parse_file("18test.txt"), parse_file("18.txt")
    print(f"Part 1 Test: {part_one(test_input, False)} (expected {P1TEST})")
    # print(f"Part 2 Test: {part_two(test_input, False)} (expected {P2TEST})")
    # print()
    # print(f"Part 1: {part_one(input)}")
    # print(f"Part 2: {part_two(input)}")