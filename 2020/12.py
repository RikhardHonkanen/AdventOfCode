###################################
####### SPOILERS FOR DAY 12 #######
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

def move_ship(position, waypoint, value):
    print(f"Position: {position}, Waypoint: {waypoint}")
    movement = ((waypoint[0] - position[0]) * value, (waypoint[1] - position[1]) * value)
    position = (position[0] + movement[0], position[1] + movement[1])
    waypoint = (waypoint[0] + movement[0], waypoint[1] + movement[1])
    
    return position, waypoint

def rotate_waypoint(position, waypoint, instruction, value):
    relative_pos = ((waypoint[0] - position[0]), (waypoint[1] - position[1]))
    turns = int(value) / 90 if instruction == 'R' else int(value) / 90 * -1
    # There are 4 unique positions to rotate to
    turns = int(turns % 4)
    
    if turns == 0:
        return waypoint # Every 4 turns we're back where we started     
    if turns == 1 or turns == -3:
        relative_pos = (relative_pos[1], relative_pos[0] * -1)
    elif turns == 2 or turns == -2:
        relative_pos = (relative_pos[0] * -1, relative_pos[1] * -1)
    elif turns == 3 or turns == -1:
        relative_pos = (relative_pos[1] * -1, relative_pos[0])
        
    return (position[0] + relative_pos[0], position[1] + relative_pos[1])

def move_waypoint(waypoint, instruction, value):
    if instruction == 'E':
        waypoint = (waypoint[0] + value, waypoint[1])
    if instruction == 'S':
        waypoint = (waypoint[0], waypoint[1] - value)
    if instruction == 'W':
        waypoint = (waypoint[0] - value, waypoint[1])
    if instruction == 'N':
        waypoint = (waypoint[0], waypoint[1] + value)
        
    return waypoint

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
    
    position = (0, 0)
    waypoint = (10, 1)
    
    for i in input:
        instruction, value = i[0], i[1:]
        value = int(value)
        if instruction == 'F':
            position, waypoint = move_ship(position, waypoint, value)
        elif instruction == 'R' or instruction == 'L':        
            waypoint = rotate_waypoint(position, waypoint, instruction, value)
        else:
            waypoint = move_waypoint(waypoint, instruction, value)
        
    return sum(abs(x) for x in position)

if __name__ == "__main__":
    P1TEST, P2TEST = 25, 286
    test_input, input = parse_file("12test.txt"), parse_file("12.txt")
    print(f"Part 1 Test: {part_one(test_input, False)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_input, False)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    print(f"Part 2: {part_two(input)}")