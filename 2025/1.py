###################################
####### SPOILERS FOR DAY 01 #######
###################################

import os, sys

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_data = f.read().split('\n')
	return parsed_data

def part_one(data: list[str]) -> int:
    dial = 50
    zeros = 0
    for line in data:
        direction = line[0]
        amount = int(line[1:])
        if direction == "L":
            dial = (dial - amount) % 100
        else:
            dial = (dial + amount) % 100
        if dial == 0:
            zeros += 1
    return zeros

def part_two(data):
    dial = 50
    zeros = 0
    passes = 0

    for line in data:
        direction = line[0]
        amount = int(line[1:])
        delta = -amount if direction == "L" else amount

        start = dial
        extended_end = start + delta

        # Count how many multiples of 100 are strictly between start and extended_end.
        low = min(start, extended_end)
        high = max(start, extended_end)

        # Number of multiples strictly between low and high:
        # multipliers k such that low < k*100 < high
        # equals ( (high-1)//100 ) - ( low//100 )
        passes += max(0, ( (high - 1) // 100 ) - (low // 100))

        dial = extended_end % 100

        if dial == 0:
            zeros += 1

    return zeros + passes

if __name__ == "__main__":
    P1TEST, P2TEST = 3, 6
    test_data, data = parse_file("1test.txt"), parse_file("1.txt")
    # print(f"Part 1 Test: {part_one(test_data)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_data)} (expected {P2TEST})")
    # print()
    # print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")