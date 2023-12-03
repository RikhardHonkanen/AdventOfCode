#################
### SPOILERS  ###
### FOR DAY 3 ###
### OF AOC    ###
#################

import os, sys
import re

# dict as {0: [], 1: [8, 25, 49, 53, 75, 95], 2: [10, 31, 41, 69, 86, 104, 112, 123], 3: [3, 61, 72, 80]}......
symbol_indexes_map = {}
# hardcoded input rows, because lazy
num_rows = 140

def store_symbol_indexes(schematic):
    row_length = len(schematic[0])
    for idx, line in enumerate(schematic):
        indexes = []
        for cidx, char in enumerate(line):
            if(not char.isdigit() and char != '.'):
                indexes.append(cidx)
        symbol_indexes_map[idx] = indexes
    return row_length
        
def compare_symbol_number_locations(idx, numbers_with_locations):
    eligible_parts = []
    for number_location in numbers_with_locations:
        compare_to_adjacent_rows(idx, number_location)
    
def compare_to_adjacent_rows(idx, number_location):
    n = list(number_location.keys())[0]
    bounds = list(number_location.values())[0]
    # note to self: risk of off by one errors here
    min_bound = bounds[0] - 2 if bounds[0] - 2 >= 0 else bounds[0] - 1
    max_bound = bounds[1] + 2 if bounds[1] + 2 <= row_length + 1 else bounds[1] + 1
    row_above = idx - 1 if idx - 1 >= 0 else idx
    row_below = idx + 1 if idx + 1 <= num_rows else idx
    
    for vindex in range(row_above, row_below):
        for hindex in range(min_bound, max_bound):
            if(int(hindex) in symbol_indexes_map[vindex]):
                results.append(n)
        
def extract_number_locations(line):
    results = [{m.group(): (m.start(0), m.end(0) + 1)} for m in re.finditer(r'\d+', line)]
    #return [{'180': (5, 8)}, {'230': (17, 20)} ... ]
    return results

def populate_results(schematic):
    for idx, line in enumerate(schematic):
        numbers_with_locations = extract_number_locations(line)
        compare_symbol_number_locations(idx, numbers_with_locations)

def parse_file(path):
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split("\n")
	return parsed_input

def add_all_results(results):
    sum = 0
    for res in results:
        sum += int(res)
    return sum

results = []
schematic = parse_file('3.txt')
row_length = store_symbol_indexes(schematic)
populate_results(schematic)
answer = add_all_results(results)
print(answer)