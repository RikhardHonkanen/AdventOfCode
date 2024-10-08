###################################
####### SPOILERS FOR DAY 05 #######
###################################
####### A DINGO ATE MY BABY #######
###################################

import os, sys, re

debug = False

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def print_debug(string):
    if (debug):
        print(string)
        
def find_seat(s):
    lower_bound = 0
    upper_bound = 127
    row = 0        
    for i in range(0, 7):
        print_debug("")
        print_debug("Lower bound: " + str(lower_bound) + ", Upper bound: " + str(upper_bound))
        print_debug("Step " + str(i) + ", Evaluating \"" + s[i] + "\".")
        if i == 6:
            if s[i] == 'F': row = lower_bound
            else: row = upper_bound
        if s[i] == 'F':
            upper_bound = (lower_bound + upper_bound) // 2
        else:
            lower_bound = round((lower_bound + upper_bound) / 2)
        print_debug("Revised:")
        print_debug("Lower bound: " + str(lower_bound) + ", Upper bound: " + str(upper_bound))
        
    lower_bound = 0
    upper_bound = 7            
    column = 0            
    for i in range(7, 10):
        if s[i] == 'L':
            upper_bound = (lower_bound + upper_bound) // 2
            if i == 9: column = upper_bound
        else:
            lower_bound = round((lower_bound + upper_bound) / 2)
            if i == 9: column = upper_bound
         
    seat_id = row * 8 + column
    return row, column, seat_id

def find_missing_seat_id(seat_ids):
    for idx, id in enumerate(seat_ids):
        if idx == 0: continue
        # First time we encounter an empty seat simply return it, not robust but works here
        if not (id - 1 in seat_ids and id + 1 in seat_ids):
            return id + 1
        
def part_one(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    answer = 0
    for s in input:
        _row, _column, seat_id = find_seat(s)
        if seat_id > answer: answer = seat_id
                
    return answer

def part_two(input, _debug = False):
    if (_debug):
        global debug
        debug = True 
        
    print_debug("Total boarding passes: " + str(len(input)))
        
    seat_map = []
    for i in range(0, 128):
        seat_map.append("")
        for j in range(0, 8):
            seat_map[i] += "X"
            
    seat_ids = {""}
    seat_ids.remove("")
    dupe_count = 0
    for idx, s in enumerate(input):
        _row, _column, seat_id = find_seat(s)
        row = int(_row) - 1
        column = int(_column)
        
        ### DEBUG
        if seat_id in seat_ids:
            dupe_count += 1
            print_debug("DUPLICATE FOUND")
        ### END DEBUG
        
        seat_ids.add(seat_id)
        seat_map[row] = seat_map[row][:column] + "O" + seat_map[row][column + 1:]
        
        ### DEBUG  
        if (idx == 907): 
            print_debug("")
            print_debug("### BOARDING PASS NO. " + str(idx + 1) + ": " + s + " ###")
            print_debug("Seat map, total rows: " + str(len(seat_map)))  
            for r in seat_map:
                print_debug(r)
                
            print_debug("")
            print_debug("Taken seats: " + str(len(seat_ids)))
            print_debug("Dupes found: " + str(dupe_count))
            print_debug(seat_ids)
            print_debug("row: " + str(row) + ", column: " + str(column))
        ### END DEBUG
                
    answer = find_missing_seat_id(seat_ids)
    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 820, 0
    test_input, input = parse_file("5test.txt"), parse_file("5.txt")
    print(f"Part 1 test: {part_one(test_input, False)} (expected {P1TEST})")
    print(f"Part 2 test: {part_two(test_input, False)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input, False)}")
    print(f"Part 2: {part_two(input)}")