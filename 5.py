###################################
####### SPOILERS FOR DAY 05 #######
###################################
### ########################### ###
###################################

import os, sys
import re

maps = {}
seeds = []
debug = False

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def print_debug(string):
    if (debug):
        print(string)

def clean_up_data(input):
    clean_data = []
    for i in input:
        if (not i):
            continue
        j = i.split(':')
        if (j[0]):
            clean_data.append(j[0].strip())
        if (len(j) > 1 and j[1]):
            clean_data.append(j[1].strip())
    return clean_data

def populate_maps(clean_data):
    current_key = ''
    for entry in clean_data:
        if (not entry[0].isdigit()):
            current_key = entry
            continue
        number_list = [m.group() for m in re.finditer(r'\d+', entry)]
        if (current_key == 'seeds'):
            global seeds
            seeds = number_list
            continue
        if (current_key in maps):
            maps[current_key] += [number_list]
        else:
            maps[current_key] = [number_list]
            
def walk_the_maps(seed):
    print_debug(f"Seed: {seed}")
    current = seed
    path = []
    for rows in maps:
        print_debug(f"Current data: {rows}: {maps[rows]}")
        for r in maps[rows]:
            source_min = int(r[1]) 
            source_max = int(r[1]) + int(r[2]) - 1
            print_debug(f"Source min, source max: {source_min} - {source_max}")
            if (int(current) >= source_min and source_max >= int(current)):
                current = int(r[0]) + (int(current)) - source_min
                print_debug(f"Match! New current: {current}")
                break
            print_debug(f"No match. Current is still: {current}")
        # If no match, do nothing and go to next map
    print_debug(f"Destination: {current}")
    print_debug(f"------------------------------------")
    return current

def get_ranges(seeds):
    ranges = []
    for i in range(0, len(seeds), 2):
        range_start, duration = int(seeds[i]), int(seeds[i + 1])
        ranges.append((range_start, range_start + duration))
        
    return ranges

def find_nearest_location(seed_ranges = False):
    lowest = -1
    if seed_ranges:
        ranges = get_ranges(seeds)
        print(ranges)
        exit()
        for r in ranges:
            for seed in range(r[0], r[1]):
                destination = walk_the_maps(seed)
                if (destination < lowest or lowest == -1):
                    lowest = destination             
    else:
        for seed in seeds:
            destination = walk_the_maps(seed)
            if (destination < lowest or lowest == -1):
                lowest = destination 
        
    return lowest

def part_one(input, _debug = False):
    if (_debug):
        global debug
        debug = True
    maps.clear()
    seeds.clear()
    clean_data = clean_up_data(input)
    populate_maps(clean_data)
    answer = find_nearest_location()
            
    return answer

def part_two(input, _debug = False):
    if (_debug):
        global debug
        debug = True
    maps.clear()
    seeds.clear()
    clean_data = clean_up_data(input)
    populate_maps(clean_data)
    answer = find_nearest_location(True)
            
    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 35, 46
    test_input, input = parse_file("5test.txt"), parse_file("5.txt")
    # print(f"Part 1 Test: {part_one(test_input, False)} (expected {P1TEST})")
    # print(f"Part 2 Test: {part_two(test_input, False)} (expected {P2TEST})")
    # print()
    # print(f"Part 1: {part_one(input)}")
    print(f"Part 2: {part_two(input)}")
    
    ## 