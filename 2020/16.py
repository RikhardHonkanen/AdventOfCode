###################################
####### SPOILERS FOR DAY 16 #######
###################################
######## CHOO HECKING CHOO ########
###################################

import os, sys

debug = False

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def print_debug(string):
    if (debug):
        print(string)
        
def value_not_in_ranges(rules, val):
        for ranges in rules.values():
            for range in ranges:
                if(range[0] <= val <= range[1]):
                    return False    # Return false if the value is in any stored range
        return True

def part_one(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    # Rules end at 1st empty string. Map field names to allowed ranges-{field_name: [(r_start, r_end)]}        
    rules_end_idx = input.index("")
    rules = {
    s.split(':')[0]: [
        tuple(map(int, r.split('-'))) 
        for r in s.split(':')[1].strip().split(' or ')
    ] 
    for s in input[:rules_end_idx]
    }
    
    nearby_tickets_idx = input.index('nearby tickets:')
    nearby_tickets = input[nearby_tickets_idx + 1:]
    
    ticket_scanning_error_rate = 0        
    for ticket in nearby_tickets:
        values = [int(value) for value in ticket.split(',')]
        for val in values:
            if (value_not_in_ranges(rules, val)):
                ticket_scanning_error_rate += val
            
    return ticket_scanning_error_rate

def part_two(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    answer = 'Part two'            
    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 71, 0
    test_input, input = parse_file("16test.txt"), parse_file("16.txt")
    print(f"Part 1 Test: {part_one(test_input, False)} (expected {P1TEST})")
    # print(f"Part 2 Test: {part_two(test_input, False)} (expected {P2TEST})")
    # print()
    print(f"Part 1: {part_one(input)}")
    # print(f"Part 2: {part_two(input)}")