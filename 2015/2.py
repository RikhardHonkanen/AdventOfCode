###################################
####### SPOILERS FOR DAY 02 #######
###################################

import os, sys

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_data = f.read().split('\n')
	return parsed_data

def part_one(data):
    total = 0
    for line in data:
        a, b, c = map(int, line.split('x'))
        sides = [a*b, a*c, b*c]
        total += 2*sum(sides) + min(sides)
    return total

def part_two(data):
    total = 0
    for line in data:
        a, b, c = map(int, line.split('x'))
        sides = [a+a+b+b, a+a+c+c, b+b+c+c]
        total += min(sides) + a*b*c
    return total

if __name__ == "__main__":
    P1TEST, P2TEST = 101, 48
    test_data, data = parse_file("2test.txt"), parse_file("2.txt")
    print(f"Part 1 Test: {part_one(test_data)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_data)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")
    