###################################
####### SPOILERS FOR DAY 02 #######
###################################
#### THE POPE PLANTED POTATOES ####
###### IN HIS PUMPKIN PATCH. ######
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
        
def count_trees(input):
    x = 0
    dx = 3
    y_start = 0
    dy = 1
    count = 0
    
    for y in range (y_start, len(input), dy):
        row = input[y]
        print_debug(row)
        
        if (x >= len(row)):
            x = x - len(row)
            
        print(x, len(row))
        
        if (row[x] == "#"):
            count += 1
        x += dx
        
    return count

def part_one(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    answer = count_trees(input)
    return answer

def part_two(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    answer = "Part 2"
    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 7, 1
    test_input, input = parse_file("3test.txt"), parse_file("3.txt")
    print(f"Part 1 Test: {part_one(test_input, False)} (expected {P1TEST})")
    # print(f"Part 2 Test: {part_two(test_input, False)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input, False)}")
    # print(f"Part 2: {part_two(input)}")