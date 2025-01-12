###################################
####### SPOILERS FOR DAY 13 #######
###################################

import os, sys

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def part_one(input):
    t_zero = int(input[0])
    departures = input[1].split(',')
    departures = {d for d in departures}
    departures.remove("x")
    
    time = t_zero
    best_dep = -1
    while(True):
        for d in departures:
            d = int(d)
            if time % d == 0:
                best_dep = d
                break
        if best_dep != -1:
            break
        time += 1
        
    return best_dep * (time - t_zero)

def part_two(input):
    # Split and parse bus IDs
    departures = input[1].split(',')
    bus_ids = [(int(bus), offset) for offset, bus in enumerate(departures) if bus != 'x']
    print(bus_ids)

    # Initial timestamp and step (starting with the first bus ID)
    timestamp = 0
    step = bus_ids[0][0]

    # Iterate through each bus ID and its offset
    for bus_id, offset in bus_ids[1:]:
        # Increment timestamp by the current step until we satisfy the condition for the current bus ID
        while (timestamp + offset) % bus_id != 0:
            timestamp += step
        
        '''
        Each time we alter the "step" variable we will currently be aligned at a timestamp that works for all ID's we have checked so far, 
        so we can add in the factor of the current ID without having to worry about "missing" any points of interest.
        '''
        # Multiply the step by the current bus ID to keep all previous buses aligned
        step *= bus_id  # LCM-like behavior

    return timestamp

if __name__ == "__main__":
    P1TEST, P2TEST = 295, 1068781
    test_input, input = parse_file("13test.txt"), parse_file("13.txt")
    print(f"Part 1 Test: {part_one(test_input)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_input)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    print(f"Part 2: {part_two(input)}")
    
# Part 2 by ChatGPT