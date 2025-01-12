###################################
####### SPOILERS FOR DAY 10 #######
###################################

import os, sys

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def part_one(input):
    joltages = []
    for n in input:
        joltages.append(int(n))
    joltages.sort()
        
    # We start "threes" at 1 to account for the last connection to our device
    ones = 0
    threes = 1
    for idx, j in enumerate(joltages):
        if idx == 0:
            if j == 3:
                threes += 1
            elif j == 1:
                ones += 1
        if j - joltages[idx - 1] == 3:
            threes += 1
        elif j - joltages[idx - 1] == 1:
            ones += 1
            
    return threes * ones

def part_two(input, _debug=False):
    # Parse the input and sort it
    joltages = [int(n) for n in input]
    joltages.append(0)  # Add the charging outlet (0 jolts)
    joltages.sort()
    joltages.append(joltages[-1] + 3)  # Add the device's built-in adapter (+3 jolts)

    # Initialize a dictionary to store the number of ways to reach each adapter
    dp = {0: 1}  # There's 1 way to reach the charging outlet (0 jolts)

    # Calculate the number of ways to reach each adapter
    for joltage in joltages[1:]:
        # For each adapter, sum the number of ways to reach it from the previous 1, 2, or 3 joltages
        dp[joltage] = dp.get(joltage - 1, 0) + dp.get(joltage - 2, 0) + dp.get(joltage - 3, 0)

    # The answer is the number of ways to reach the highest adapter
    return dp[joltages[-1]]

if __name__ == "__main__":
    P1TEST, P2TEST = 220, 19208
    test_input, input = parse_file("10test.txt"), parse_file("10.txt")
    print(f"Part 1 Test: {part_one(test_input)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_input)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    print(f"Part 2: {part_two(input)}")
    
### Part 2 implemented by someone and interpreted by ChatGPT