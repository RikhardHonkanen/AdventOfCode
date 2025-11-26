###################################
####### SPOILERS FOR DAY 01 #######
###################################

import os, sys

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def part_one(data):
    floor = 0
    for line in data:
        for c in line:
            floor = floor + 1 if (c == '(') else floor - 1
    return floor

def part_two(data):
    floor = 0
    pos = 0
    for line in data:
        for c in line:
            if floor == -1:
                return pos
            pos += 1
            floor = floor + 1 if (c == '(') else floor - 1
    return 0

if __name__ == "__main__":
    data = parse_file("1.txt")
    print()
    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")