###################################
####### SPOILERS FOR DAY 00 #######
###################################

import os, sys

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_data = f.read().split('\n')
	return parsed_data

def part_one(data):      
    answer = 'Part one'            
    return answer

def part_two(data):
    answer = 'Part two'            
    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 0, 0
    test_data, data = parse_file("0test.txt"), parse_file("0.txt")
    print(f"Part 1 Test: {part_one(test_data)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_data)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")