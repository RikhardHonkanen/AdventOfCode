###################################
####### SPOILERS FOR DAY 12 #######
###################################
### MESSAGE OF THE DAY IS: COW. ###
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
        
def get_direction(facing, instruction, value):
    directions = ['E', 'S', 'W', 'N']
    turns = int(value) / 90 if instruction == 'R' else int(value) / 90 * -1
    current_index = directions.index(facing)
    # Calculate the new index after the turns (use modulo to loop around the list)
    new_index = (current_index + int(turns)) % len(directions)
    return directions[new_index]

def part_one(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    facing = 'E'
    position = (0, 0)
    
    for i in input:
        instruction, value = i[0], i[1:]
        value = int(value)
        if instruction == 'R' or instruction == 'L':        
            facing = get_direction(facing, instruction, value)
        if instruction == 'F':
            if facing == 'N' or facing == 'S':
                value = value if facing == 'N' else value * -1
                position = (position[0], position[1] + value)
            else:
                value = value if facing == 'E' else value * -1
                position = (position[0] + value, position[1])
        else:
            if instruction == 'E':
                position = (position[0] + value, position[1])
            if instruction == 'S':
                position = (position[0], position[1] - value)
            if instruction == 'W':
                position = (position[0] - value, position[1])
            if instruction == 'N':
                position = (position[0], position[1] + value)
    
    return sum(abs(x) for x in position)

def part_two(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    answer = 'Part two'            
    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 25, 286
    test_input, input = parse_file("12test.txt"), parse_file("12.txt")
    print(f"Part 1 Test: {part_one(test_input, False)} (expected {P1TEST})")
    # print(f"Part 2 Test: {part_two(test_input, False)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    # print(f"Part 2: {part_two(input)}")