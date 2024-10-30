###################################
####### SPOILERS FOR DAY 13 #######
###################################
#### ANOTHER ONE RIDES THE BUS ####
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

def part_one(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    t_zero = int(input[0])
    departures = input[1].split(',')
    departures = {d for d in departures}
    departures.remove("x")
    
    time = t_zero
    best_dep = -1
    while(True):
        for d in departures:
            d = int(d)
            if time % d == 0:
                best_dep = d
                break
        if best_dep != -1:
            break
        time += 1
        
    return best_dep * (time - t_zero)

def part_two(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    answer = 'Part two'            
    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 295, 0
    test_input, input = parse_file("13test.txt"), parse_file("13.txt")
    print(f"Part 1 Test: {part_one(test_input, False)} (expected {P1TEST})")
    # print(f"Part 2 Test: {part_two(test_input, False)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    # print(f"Part 2: {part_two(input)}")