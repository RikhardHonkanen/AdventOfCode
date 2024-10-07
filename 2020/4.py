###################################
####### SPOILERS FOR DAY 04 #######
###################################
# DARTH VADER IS NOT YOUR FATHER. #
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
        
def check_single_passport(current):
    keys = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
    for key in keys:
        if key not in current:
            return False 
    return True

def check_and_validate_single_passport(current):
    def get_property(key):
        idx = current.find(key)
        if idx == -1: return False
        return current[idx:].split(' ')[0].split(':')[1]        
        
    byr = get_property("byr:")
    if not byr or not (int(byr) >= 1920 and int(byr) <= 2002): return False    
    iyr = get_property("iyr:")
    if not iyr or not (int(iyr) >= 2010 and int(iyr) <= 2020): return False    
    eyr = get_property("eyr:")
    if not eyr or not (int(eyr) >= 2020 and int(eyr) <= 2030): return False
    
    hgt = get_property("hgt:")
    if not hgt: return False
    unitidx = hgt.find("in")
    if unitidx == -1:
        unitidx = hgt.find("cm")
        if unitidx == -1: return False
        h = hgt[:unitidx]
        if not (int(h) >= 150 and int(h) <= 193): return False
    else:
        h = hgt[:unitidx]
        if not (int(h) >= 59 and int(h) <= 76): return False
    
    hcl = get_property("hcl:")
    if not hcl or hcl[0] != '#': return False
    test = re.search("[0-9a-fA-F]+", hcl[1:])
    if test == None or test.span() != (0, 6): return False
    
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    ecl = get_property("ecl:")
    if not ecl or ecl not in colors: return False
    
    pid = get_property("pid:")
    if not pid: return False
    test = re.search("[0-9]+", pid)
    if test == None or test.span() != (0, 9): return False
    
    return True
        
def count_valid_passports(input):
    count = 0
    current = ""
    for idx, line in enumerate(input):
        if (line == ""):
            if (check_single_passport(current)):
                count += 1
            current = ""
        elif (idx == len(input) - 1):
            current += line
            if (check_single_passport(current)):
                count += 1
        else:
            current += line       
    
    return count

def count_valider_passports(input):
    count = 0
    current = ""
    for idx, line in enumerate(input):
        if (line == ""):
            if (check_and_validate_single_passport(current)):
                count += 1
            current = ""
        elif (idx == len(input) - 1):
            current += " " + line
            if (check_and_validate_single_passport(current)):
                count += 1
        else:
            current += " " + line       
    
    return count

def part_one(input, _debug = False):
    if (_debug):
        global debug
        debug = True 
                
    answer = count_valid_passports(input)
    return answer

def part_two(input, _debug = False):
    if (_debug):
        global debug
        debug = True 
        
    answer = count_valider_passports(input)        
    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 2, 0
    test_input, input = parse_file("4test.txt"), parse_file("4.txt")
    print(f"Part 1 test: {part_one(test_input, False)} (expected {P1TEST})")
    print(f"Part 2 test: {part_two(test_input, False)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input, False)}")
    print(f"Part 2: {part_two(input)}")