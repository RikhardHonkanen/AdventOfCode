###################################
####### SPOILERS FOR DAY 04 #######
###################################

import os, sys

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def find_XMASes(letter_map, ridx, cidx):
    directions = [
        [(0, -1), (0, -2), (0, -3)],        # left
        [(-1, -1), (-2, -2), (-3, -3)],     # up-left
        [(-1, 0), (-2, 0), (-3, 0)],        # up
        [(-1, 1), (-2, 2), (-3, 3)],        # up-right
        [(0, 1), (0, 2), (0, 3)],           # right
        [(1, 1), (2, 2), (3, 3)],           # right-down
        [(1, 0), (2, 0), (3, 0)],           # down
        [(1, -1), (2, -2), (3, -3)]         # down-left
    ]
    row_length = len(letter_map[0])
    num_rows = len(letter_map)
    
    found = 0    
    for direction in directions:
        valid = True
        for i, (dr, dc) in enumerate(direction):
            new_ridx, new_cidx = ridx + dr, cidx + dc
            if not (0 <= new_ridx < num_rows and 0 <= new_cidx < row_length):
                valid = False
                break
            # Check if the letters match the expected ones ('M', 'A', 'S'), we start at 'X'
            expected_char = 'M' if i == 0 else ('A' if i == 1 else 'S')
            if letter_map[new_ridx][new_cidx] != expected_char:
                valid = False
                break
        if valid:
            found += 1
    return found

def find_X_MASes(letter_map, ridx, cidx):
    row_length = len(letter_map[0])
    num_rows = len(letter_map)
    if (not (0 < ridx < num_rows - 1 and 0 < cidx < row_length - 1)):
        return 0
    
    targets = ['M', 'S']
    valid = True
    # Top left to bottom right diagonal
    if (letter_map[ridx - 1][cidx - 1] not in targets
        or letter_map[ridx + 1][cidx + 1] not in targets
        or letter_map[ridx - 1][cidx - 1] == letter_map[ridx + 1][cidx + 1]):
        valid = False
    # Bottom left to top right diagonal
    if (letter_map[ridx + 1][cidx - 1] not in targets
        or letter_map[ridx - 1][cidx + 1] not in targets
        or letter_map[ridx + 1][cidx - 1] == letter_map[ridx - 1][cidx + 1]):
        valid = False
        
    return 1 if valid else 0

def part_one(letter_map):
    XMASes = 0
    for ridx, line in enumerate(letter_map):
        for cidx, c in enumerate(line):
            if c == 'X':
                XMASes += find_XMASes(letter_map, ridx, cidx)
        
    return XMASes

def part_two(letter_map):
    X_MASes = 0
    for ridx, line in enumerate(letter_map):
        for cidx, c in enumerate(line):
            if c == 'A':
                X_MASes += find_X_MASes(letter_map, ridx, cidx)
        
    return X_MASes

if __name__ == "__main__":
    P1TEST, P2TEST = 18, 9
    test_input, input = parse_file("4test.txt"), parse_file("4.txt")
    print(f"Part 1 Test: {part_one(test_input)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_input)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    print(f"Part 2: {part_two(input)}")