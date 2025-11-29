###################################
####### SPOILERS FOR DAY 04 #######
###################################

import os, sys
import hashlib

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_data = f.read()
	return parsed_data

def solve(data, zeros):
    target = "0" * zeros
    i = 0
    while True:
        s = data + str(i)
        if hashlib.md5(s.encode()).hexdigest().startswith(target):
            return i
        i += 1

if __name__ == "__main__":
    P1TEST, P2TEST = 609043, 6742839
    test_data, data = parse_file("4test.txt"), parse_file("4.txt")
    print(f"Part 1 Test: {solve(test_data, 5)} (expected {P1TEST})")
    print(f"Part 2 Test: {solve(test_data, 6)} (expected {P2TEST})")
    print()
    print(f"Part 1: {solve(data, 5)}")
    print(f"Part 2: {solve(data, 6)}")