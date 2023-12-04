###################################
####### SPOILERS FOR DAY 04 #######
###################################
### HE CONFORMS TO THE TEMPLATE ###
###################################

import os, sys
import re

running_totals = {}

def parse_file(path):
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split("\n")
	return parsed_input

def split_numbers_for_game(numbers):
    parts = numbers.split('|')
    a = [m.group() for m in re.finditer(r'\d+', parts[0])]
    b = [m.group() for m in re.finditer(r'\d+', parts[1])]
    return a, b

def get_win_amount(numbers):
    house_numbers, my_numbers = split_numbers_for_game(numbers)
    winners = 0
    
    for my_number in my_numbers:
        if (my_number in house_numbers):
            winners += 1
    return winners

def calculate_points_for_card(numbers):
    winners = get_win_amount(numbers)
    
    if (winners == 0):
        return 0
   
    return pow(2, winners - 1)

def add_to_running_totals(idx, numbers): 
    game_number = idx + 1   
    winners = get_win_amount(numbers)
    power = 1   
        
    if (game_number in running_totals):
        power = running_totals[game_number]
    else:
        running_totals[game_number] = 1 # If current game doesn't have an entry yet, we only have one ticket
        
    ### Debugging
    if (game_number >= 195 and game_number <= 201):
        print(winners)    
    ### End
        
    for n in range(1, winners + 1):
        if (game_number + n in running_totals):
            running_totals[game_number + n] += power
        else:
            running_totals[game_number + n] = power + 1 # Need to remember we start with a ticket
            
def sum_all_running_totals(input_length):
    answer = 0
    # for num in range(0, input_length):
    #     answer += list(running_totals.values())[num]
    for val in running_totals.values():
        answer += val
    return answer        

def part_one(input):
    answer = 0
    for row in input:
        numbers = row.split(':')[1]
        answer += calculate_points_for_card(numbers)        
    return answer

def part_two(input):
    # running_totals.clear()
    global running_totals
    running_totals = {}
    
    input_length = len(input)
    for idx, row in enumerate(input):
        numbers = row.split(':')[1]
        add_to_running_totals(idx, numbers)        
    return sum_all_running_totals(input_length)

if __name__ == "__main__":
    P1TEST, P2TEST = 13, 30
    test_input, input = parse_file("4test.txt"), parse_file("4.txt")
    print(f"Part 1 Test: {part_one(test_input)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_input)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    print(f"Part 2: {part_two(input)}")
    
    ## Overall this one wasn't too bad... have to keep track of your indexes mainly, with this approach at least
    ## Also, weirdly if i run the test for part 2 it breaks the real output (even if i try to reset with 'running_totals = {}')
    ## Fixed this with 'running_totals.clear()' ^^