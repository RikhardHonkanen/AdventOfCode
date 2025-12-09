###################################
####### SPOILERS FOR DAY 02 #######
###################################

import os, sys

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_data = f.read()
	return parsed_data

def part_one(data):
    ranges = [tuple(map(int, part.split("-"))) for part in data.split(",")]
    total = 0
    for start, end in ranges:
        for n in range(start, end + 1):
            word = str(n)
            if len(word) % 2 == 0:
                mid = len(word) // 2
                if word[:mid] == word[mid:]:
                    total += n
    return total

def part_two(data):
    answer = 'Part two'            
    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 1227775554, 0
    test_data, data = parse_file("2test.txt"), parse_file("2.txt")
    print(f"Part 1 Test: {part_one(test_data)} (expected {P1TEST})")
    # print(f"Part 2 Test: {part_two(test_data)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(data)}")
    # print(f"Part 2: {part_two(data)}")