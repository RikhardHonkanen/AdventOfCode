###################################
####### SPOILERS FOR DAY 03 #######
###################################

import os, sys, re

TUPLE_PATTERN = r"mul\((-?\d+),(-?\d+)\)"

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def part_one(input):
    input_string = "".join(input)
    return sum(int(x) * int(y) for x, y in re.findall(TUPLE_PATTERN, input_string))

def part_two(input):
    clean_pattern = r"don't\(\).*?do\(\)"
    input_string = "".join(input)
    cleaned_line = re.sub(clean_pattern, '', input_string)
    return sum(int(x) * int(y) for x, y in re.findall(TUPLE_PATTERN, cleaned_line))

if __name__ == "__main__":
    P1TEST, P2TEST = 161, 48
    test_input, test2_input, input = parse_file("3test.txt"), parse_file("3test2.txt"), parse_file("3.txt")
    print(f"Part 1 Test: {part_one(test_input)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test2_input)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    print(f"Part 2: {part_two(input)}")