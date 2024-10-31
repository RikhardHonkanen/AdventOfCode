###################################
####### SPOILERS FOR DAY 14 #######
###################################
### BIT BY BIT BY BIT BY BIT BY ###
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
        
def extract_values(s):
    match = re.search(r"mem\[(\d+)\] = (\d+)", s)
    if match:
        address = int(match.group(1))
        value = int(match.group(2))
        return address, value
    return None, None

def apply_mask(binary, mask):
    result = ""
    for idx, c in enumerate(binary):
        if mask[idx] != 'X':
            result += mask[idx]
        else:
            result += c
    return result

def get_all_values(binary, mask):
    pass

def part_one(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    mask = ""
    mem = {}                #{address: value}
    for line in input:
        if "mask" in line:
            mask = line.split('=')[1].strip()
            continue
        
        address, value = extract_values(line)
        _binary = bin(value).replace("0b", "")
        binary = ''.zfill(len(mask) - len(_binary)) + _binary
        
        to_mem = apply_mask(binary, mask)
        mem[address] = to_mem
            
    return sum(int(x, 2) for x in mem.values())

def part_two(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    mask = ""
    mem = {}                #{address: [values]}
    for line in input:
        if "mask" in line:
            mask = line.split('=')[1].strip()
            continue
        
        address, value = extract_values(line)
        _binary = bin(value).replace("0b", "")
        binary = ''.zfill(len(mask) - len(_binary)) + _binary
        
        to_mem = get_all_values(binary, mask) # <- fix this
        mem[address] = to_mem
            
    return sum(int(x, 2) for x in mem.values()) # <- fix this
        

if __name__ == "__main__":
    P1TEST, P2TEST = 165, 0
    test_input, input = parse_file("14test.txt"), parse_file("14.txt")
    print(f"Part 1 Test: {part_one(test_input, False)} (expected {P1TEST})")
    # print(f"Part 2 Test: {part_two(test_input, False)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    # print(f"Part 2: {part_two(input)}")