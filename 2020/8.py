###################################
####### SPOILERS FOR DAY 08 #######
###################################
############# GANDALF #############
###################################

import os, sys

# instructions are line by line: "argument x", where x is any integer
# break the program before running any instruction (unique line) a second time and report back value of accumulator

# arguments:
# acc - add x to accumulator 
# jmp - jump x lines
# nop - no operation, skip to next instruction

debug = False

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def print_debug(string):
    if (debug):
        print(string)
        
def run_program(instructions):
    """ Helper function to run the program and detect termination or loop """
    accumulator = 0
    line_idx = 0
    visited_lines = set()
    
    while line_idx < len(instructions):
        if line_idx in visited_lines:
            # Infinite loop detected
            return False, accumulator
        
        visited_lines.add(line_idx)
        instruction, x = instructions[line_idx].split(' ')
        x = int(x)
        
        if instruction == "acc":
            accumulator += x
            line_idx += 1
        elif instruction == "jmp":
            line_idx += x
        elif instruction == "nop":
            line_idx += 1
    
    # If we finish the loop, the program terminated correctly
    return True, accumulator

def part_one(input, _debug = False):            
    if (_debug):
        global debug
        debug = True
        
    accumulator = 0
    line_idx = 0
    visited_lines = set()
    while(True):
        # If we have visited the line before, break and return accumulator
        if line_idx in visited_lines:
            break
        
        visited_lines.add(line_idx)
        instruction, x = input[line_idx].split(' ')
        if instruction == "acc":
            accumulator += int(x)
            line_idx += 1
        elif instruction == "jmp":
            line_idx += int(x)
        elif instruction == "nop":
            line_idx += 1
        else:
            print("INVALID INSTRUCTION")
    
    return accumulator


def part_two(input, _debug = False):
    if _debug:
        global debug
        debug = True
    
    # Try modifying each "jmp" or "nop" instruction
    for i in range(len(input)):
        # Copy the original instructions
        modified_instructions = input[:]
        instruction, x = modified_instructions[i].split(' ')
        
        # Swap "jmp" and "nop"
        if instruction == "jmp":
            modified_instructions[i] = "nop " + x
        elif instruction == "nop":
            modified_instructions[i] = "jmp " + x
        else:
            continue  # Skip "acc" instructions
        
        # Run the modified program
        terminated, accumulator = run_program(modified_instructions)
        
        if terminated:
            return accumulator  # Return the accumulator if the program terminates
    
    return None  # If no solution is found

if __name__ == "__main__":
    P1TEST, P2TEST = 5, 8
    test_input, input = parse_file("8test.txt"), parse_file("8.txt")
    print(f"Part 1 Test: {part_one(test_input, False)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_input, False)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    print(f"Part 2: {part_two(input)}")