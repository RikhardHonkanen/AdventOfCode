###################################
####### SPOILERS FOR DAY 16 #######
###################################
######## CHOO HECKING CHOO ########
###################################

import os, sys, math

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
            for r in ranges:
                if(r[0] <= val <= r[1]):
                    return False    # Return false if the value is in any stored range
        return True
    
def setup_data(input):
    # Rules end at 1st empty string. Map field names to allowed ranges-{field_name: [(r_start, r_end)]}        
    rules_end_idx = input.index("")
    rules = {
    s.split(':')[0]: [
        tuple(map(int, r.split('-'))) 
        for r in s.split(':')[1].strip().split(' or ')
    ] 
    for s in input[:rules_end_idx]
    }
    
    my_ticket = input[input.index('your ticket:') + 1]
    
    nearby_tickets_idx = input.index('nearby tickets:')
    nearby_tickets = input[nearby_tickets_idx + 1:]
    
    return rules, my_ticket, nearby_tickets

def crunch_the_tickets(rules, valid_tickets):
    def get_possible_keys(rules, values_in_pos):
        # Collect all keys that could match `values_in_pos`
        possible_keys = []
        for key, ranges in rules.items():
            if all(any(lower <= value <= upper for (lower, upper) in ranges) for value in values_in_pos):
                possible_keys.append(key)
        return possible_keys

    # Step 1: Collect all possible keys for each index
    possible_keys_for_indices = []
    for i in range(len(rules)):  # Iterate over all field indices
        values_in_pos = [int(ticket.split(',')[i]) for ticket in valid_tickets]
        possible_keys_for_indices.append(get_possible_keys(rules, values_in_pos))

    # Step 2: Resolve keys using elimination
    resolved_keys = [None] * len(rules)
    while None in resolved_keys:
        for i, possible_keys in enumerate(possible_keys_for_indices):
            # If only one possible key remains, it must be assigned
            if len(possible_keys) == 1:
                resolved_key = possible_keys[0]
                resolved_keys[i] = resolved_key
                # Remove the resolved key from other positions
                for other_keys in possible_keys_for_indices:
                    if resolved_key in other_keys:
                        other_keys.remove(resolved_key)

    return resolved_keys

def part_one(input, _debug = False):
    if (_debug):
        global debug
        debug = True
    
    rules, _, nearby_tickets = setup_data(input) 
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
        
    rules, my_ticket, nearby_tickets = setup_data(input)
    my_ticket_values = [int(value) for value in my_ticket.split(',')]
    valid_tickets = nearby_tickets.copy()
    
    for ticket in nearby_tickets:
        values = [int(value) for value in ticket.split(',')]
        for val in values:
            if (value_not_in_ranges(rules, val)):
                valid_tickets.remove(ticket)
                
    field_names = crunch_the_tickets(rules, valid_tickets)
    values_to_multiply = []
    
    for idx, name in enumerate(field_names):
        if name.startswith('departure'):
            print(name)
            values_to_multiply.append(my_ticket_values[idx])
              
    print(values_to_multiply)
    return math.prod(values_to_multiply)

if __name__ == "__main__":
    P1TEST, P2TEST = 71, 0
    test_input, test2_input, input = parse_file("16test.txt"), parse_file("16test2.txt"), parse_file("16.txt")
    # print(f"Part 1 Test: {part_one(test_input, False)} (expected {P1TEST})")
    # print(f"Part 2 Test: {part_two(test2_input, False)} (expected {P2TEST})")
    # print()
    # print(f"Part 1: {part_one(input)}")
    print(f"Part 2: {part_two(input)}")