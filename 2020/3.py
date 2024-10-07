###################################
####### SPOILERS FOR DAY 03 #######
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
        
def count_trees(input, dx, dy):
    x = 0
    y_start = 0
    count = 0
    for y in range (y_start, len(input), dy):
        row = input[y]
        # Loop back to start when x gets too big
        if (x >= len(row)):
            x = x - len(row)
        if (row[x] == "#"):
            count += 1
        x += dx
    return count

def part_one(input, _debug = False):
    if (_debug):
        global debug
        debug = True   
             
    dx = 3     
    dy = 1
    answer = count_trees(input, dx, dy)
    return answer

def part_two(input, _debug = False):
    if (_debug):
        global debug
        debug = True  
              
    answer = 0
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for s in slopes:
        dx = s[0]
        dy = s[1]
        trees = count_trees(input, dx, dy)
        if (answer == 0):
            answer = trees
        else:
            answer = answer * trees            
    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 7, 336
    test_input, input = parse_file("3test.txt"), parse_file("3.txt")
    print(f"Part 1 test: {part_one(test_input, False)} (expected {P1TEST})")
    print(f"Part 2 test: {part_two(test_input, False)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input, False)}")
    print(f"Part 2: {part_two(input)}")