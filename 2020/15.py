###################################
####### SPOILERS FOR DAY 15 #######
###################################

import os, sys

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def solve(input, final_turn=2020):
    # Map starting numbers to dict - {number: turn_last_spoken}   
    numbers_with_turns = {int(char): idx + 1 for idx, char in enumerate(input[0].split(','))}
    last_num_spoken = input[0].split(',')[-1]       # Init at last starting number in input
    
    # Each starting number uses a turn at the beginning of the game 
    current_turn = len(numbers_with_turns) + 1
    
    
    while current_turn <= final_turn:            
        if last_num_spoken in numbers_with_turns:
            # Calculate the difference since last spoken (keeping in mind it was spoken *last turn*)
            new_num = (current_turn - 1) - numbers_with_turns[last_num_spoken]
        else:
            # If not found, speak 0
            new_num = 0

        # Update the dictionary with the turn the last number was spoken
        numbers_with_turns[last_num_spoken] = current_turn - 1
        last_num_spoken = new_num  # Set last spoken to the newly calculated number
        current_turn += 1
        
    return last_num_spoken

if __name__ == "__main__":
    P1TEST, P2TEST = 436, 0
    test_input, input = parse_file("15test.txt"), parse_file("15.txt")
    print(f"Part 1 Test: {solve(test_input)} (expected {P1TEST})")
    print(f"Part 2 Test: {solve(test_input, 30000000)} (expected {P2TEST})")
    print()
    print(f"Part 1: {solve(input)}")
    print(f"Part 2: {solve(input, 30000000)}")