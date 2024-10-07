###################################
####### SPOILERS FOR DAY 01 #######
###################################
####  IT'S NOT EVEN CHRISTMAS. ####
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
        
def find_two_numbers(number_list, magic_number):
    numbers = -1
    for idx, n in enumerate(number_list):
        if numbers != -1:
            break
        for midx in range (idx + 1, len(number_list) - 1):
            m = number_list[midx]            
            if (int(n) + int(m) == magic_number):
                numbers = (int(n), int(m))
                break
    return numbers

def find_three_numbers(number_list, magic_number):
    numbers = -1
    for idx, n in enumerate(number_list):
        if numbers != -1:
            break
        for midx in range (idx + 1, len(number_list) - 1):
            if numbers != -1:
                break
            m = number_list[midx]
            for pidx in range (idx + 2, len(number_list) - 1):
                p = number_list[pidx]
                if (int(n) + int(m) + int(p) == magic_number):
                    numbers = (int(n), int(m), int(p))
                    break
    return numbers

def part_one(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    magic_number = 2020        
    numbers = find_two_numbers(input, magic_number)
    
    # Return 0 if no two numbers summed up to the magic number    
    if (numbers == -1):
        return 0
    
    answer = numbers[0] * numbers[1]
    return answer

def part_two(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    magic_number = 2020        
    numbers = find_three_numbers(input, magic_number)
    
    # Return 0 if no three numbers summed up to the magic number    
    if (numbers == -1):
        return 0
    
    answer = numbers[0] * numbers[1] * numbers[2]
    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 514579, 241861950
    test_input, input = parse_file("1test.txt"), parse_file("1.txt")
    print(f"Part 1 Test: {part_one(test_input, False)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_input, False)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    print(f"Part 2: {part_two(input)}")