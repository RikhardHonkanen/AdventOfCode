###################################
####### SPOILERS FOR DAY 03 #######
###################################

import os, sys

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_data = f.read()
	return parsed_data

def modify_tuple(tpl, idx, incr):
    lst = list(tpl)
    lst[idx] += incr
    return tuple(lst)

def part_one(data):   
    visited = set()
    current = (0, 0)
    visited.add(current)  
    for c in data:  # N:^ E:> S:v W:<
        if c == '^':
            current = modify_tuple(current, 0, -1)
        if c == '>':
            current = modify_tuple(current, 1, 1)
        if c == 'v':
            current = modify_tuple(current, 0, 1)
        if c == '<':
            current = modify_tuple(current, 1, -1)
        visited.add(current)
    return len(visited)

def part_two(data):
    visited = set()
    current = (0, 0)
    r_current = (0, 0)
    visited.add(current)  
    for idx, c in enumerate(data):  # N:^ E:> S:v W:<
        if idx % 2 == 0:        
            if c == '^':
                current = modify_tuple(current, 0, -1)
            if c == '>':
                current = modify_tuple(current, 1, 1)
            if c == 'v':
                current = modify_tuple(current, 0, 1)
            if c == '<':
                current = modify_tuple(current, 1, -1)
            visited.add(current)
        else:
            if c == '^':
                r_current = modify_tuple(r_current, 0, -1)
            if c == '>':
                r_current = modify_tuple(r_current, 1, 1)
            if c == 'v':
                r_current = modify_tuple(r_current, 0, 1)
            if c == '<':
                r_current = modify_tuple(r_current, 1, -1)        
            visited.add(r_current)
    return len(visited)

if __name__ == "__main__":
    P1TEST, P2TEST = 5, 0
    test_data, data = parse_file("3test.txt"), parse_file("3.txt")
    print(f"Part 1 Test: {part_one(test_data)} (expected {P1TEST})")
    # print(f"Part 2 Test: {part_two(test_data)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")