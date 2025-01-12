###################################
####### SPOILERS FOR DAY 10 #######
###################################

import os, sys

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def part_one(map):  
    trailheads = {
        ridx: [cidx for cidx, c in enumerate(row) if c == '0']
        for ridx, row in enumerate(map)
        if '0' in row
    }
    print(map)
    print(trailheads)
    exit()
    # Iterate over trailheads. For every topographical max (9), check if path exists to
    # trailhead.
    answer = 'Part one'            
    return answer

def part_two(input):
    answer = 'Part two'            
    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 0, 0
    test_input, input = parse_file("10test.txt"), parse_file("10.txt")
    print(f"Part 1 Test: {part_one(test_input)} (expected {P1TEST})")
    # print(f"Part 2 Test: {part_two(test_input)} (expected {P2TEST})")
    # print()
    # print(f"Part 1: {part_one(input)}")
    # print(f"Part 2: {part_two(input)}")