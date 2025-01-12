###################################
####### SPOILERS FOR DAY 07 #######
###################################

import os, sys, re

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input
        
def extract_rules(input):
    rules = {}
    colors = set()
    for s in input:
        split = s.find("contain")
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

def part_one(input):
    rules, colors = extract_rules(input)
    target = "shiny gold"
    valid_bags = set()  # Set to track bags that can contain the target
    
    def explore_paths(colors, target):
        found_any = False
        
        for color in colors:
            # Skip if this color is the target itself
            if color == target:
                continue
            
            # If the current color directly contains the target or we already know it does, add it
            if target in rules[color] or color in valid_bags:
                valid_bags.add(color)
                found_any = True
            
            # Otherwise, explore recursively
            elif rules[color]:
                if explore_paths(list(rules[color].keys()), target):
                    valid_bags.add(color)
                    found_any = True

        return found_any
        
    # Explore each top-level color and count the number of valid bags
    for color in colors:
        explore_paths([color], target)
    
    return len(valid_bags)

def part_two(input):
    rules, colors = extract_rules(input)
    outer_container = "shiny gold"
    
    def explore_paths(color, multiplier=1):
        total_bags = 0
        if rules[color]:
            for inner_color, quantity in rules[color].items():
                # Calculate the total number of bags for this color
                total_bags += quantity * multiplier
                # Recurse into the inner bags, multiplying by how many bags are needed
                total_bags += explore_paths(inner_color, multiplier * quantity)
        return total_bags

    # Start exploration from the outermost "shiny gold" container
    return explore_paths(outer_container)


if __name__ == "__main__":
    P1TEST, P2TEST = 4, 126
    test_input, test_2_input, input = parse_file("7test.txt"), parse_file("7test2.txt"), parse_file("7.txt")
    print(f"Part 1 Test: {part_one(test_input)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_2_input)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    print(f"Part 2: {part_two(input)}")
    
    ### COLLAB CREDITS: ChatGPT4