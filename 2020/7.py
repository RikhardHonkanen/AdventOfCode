###################################
####### SPOILERS FOR DAY 07 #######
###################################
##### https://www.youtube.com #####
###### /watch?v=ub82Xb1C8os #######
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
        
def extract_rules(input):
    rules = {}
    colors = set()
    for s in input:
        split = s.find("contain")
        # Using list comprehension and slicing
        # https://pythonguides.com/split-a-string-by-index-in-python/
        indices = [split - 1, split + 8]
        substrings = [s[start:end] for start, end in zip([0] + indices, indices + [None])]
        
        key = substrings[0][slice(-5)]
        colors.add(key)
        contents = substrings[2].split(',')
        for bag in contents:
            if bag.strip() == "no other bags.":
                rules[key] = {}
                continue
            
            clean_contents = bag.strip().rsplit(' ', 1)[0]
            sub_value = clean_contents.split(' ')[0]
            sub_key = ' '.join(clean_contents.split(' ')[1:])
            colors.add(sub_key)
            
            if key not in rules:
                rules[key] = {sub_key: int(sub_value)}
            else:
                rules[key][sub_key] = int(sub_value)
                
    return rules, colors

def part_one(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    rules, colors = extract_rules(input)
    target = "shiny gold"
    def check_path(colors, target, total, original_size):
        print_debug("CHECKING (Total is " + str(total) + "):")
        print_debug(colors)
        for color in colors:
            print_debug(color)
            if color == target: continue
            if target in rules[color]:
                total = total + 1
                print_debug(color + " is a match! (Total is " + str(total) + "):")
                if len(colors) != original_size: break
            else:
                if not rules[color]: 
                    continue
                total = check_path(list(rules[color].keys()), target, total, original_size)
        return total 
          
    answer = check_path(colors, target, 0, len(colors))
    print(len(colors))
    return answer

def part_two(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    answer = 'Part two'            
    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 4, 0
    test_input, input = parse_file("7test.txt"), parse_file("7.txt")
    print(f"Part 1 Test: {part_one(test_input, False)} (expected {P1TEST})")
    # print(f"Part 2 Test: {part_two(test_input, False)} (expected {P2TEST})")
    # print()
    print(f"Part 1: {part_one(input)}")
    # print(f"Part 2: {part_two(input)}")