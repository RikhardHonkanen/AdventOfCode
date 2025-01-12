###################################
####### SPOILERS FOR DAY 09 #######
###################################

import os, sys

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def expand_input(input):
    block_count = 0
    expanded_input = []
    for idx, c in enumerate(input):
        c = int(c)
        if idx % 2 == 0:
            if c > 0:
                expanded_input.append([block_count] * c)
                block_count += 1
        else:
            if c > 0:
                expanded_input.append(['.'] * c)
    return block_count, expanded_input

def add_block_to_output(block):
    output = []
    for id in block:
        output.append(int(id))
    return output

def scan_for_block_to_move(mem, working_idx, block_id):
        if(mem[working_idx][0] == block_id):  # Correct block
            return working_idx
        else:
            working_idx -= 1
            return scan_for_block_to_move(mem, working_idx, block_id)
        
def scan_for_open_mem_block(mem, block_size, idx):
    while idx < len(mem):
        if mem[idx][0] == '.':
            if len(mem[idx]) >= block_size:
                return idx
        idx += 1
    return -1  # No large enough available memory region

def move_block_to_free_memory(mem, block_index, free_index):
    block = mem.pop(block_index)
    mem.insert(block_index, ['.'] * len(block))
    
    if (len(mem[free_index][len(block):]) > 0):    
        mem[free_index] = mem[free_index][len(block):]
    else:
        mem.pop(free_index)
    mem.insert(free_index, block)
    return mem

def part_one(input):
    _, mem = expand_input(input)
    output = []
    while(len(mem) > 0):
        if isinstance(mem[0][0], int):
            output.append(add_block_to_output(mem[0]))
            del mem[0]
            continue
        else:  # Open memory region
            if isinstance(mem[-1][0], int):  # Move trailing region to open memory
                available_space = len(mem[0])
                required_space = len(mem[-1])
                if available_space == required_space:  # Ideal case
                    output.append(add_block_to_output(mem[-1]))
                    del mem[0]
                    del mem[-1]
                    continue
                elif available_space > required_space:
                    output.append(add_block_to_output(mem[-1]))
                    mem[0] = mem[0][:available_space - required_space]  # Shrink memory region by trailing region size
                    del mem[-1]
                    continue
                else:
                    output.append(add_block_to_output(mem[-1][:available_space]))
                    mem[-1] = mem[-1][available_space:]  # Shrink trailing region by the amount we were able to squeeze into earlier memory
                    del mem[0]
                    continue
            else:  # Get rid of trailing empty memory, try again
                del mem[-1]
                continue
                
    flattened_output = [i for sl in output for i in sl]
    checksum = sum(idx * n for idx, n in enumerate(flattened_output))
        
    return checksum

def part_two(input):
    block_count, mem = expand_input(input)
    working_idx = len(mem) - 1
    for block_id in range(block_count - 1, 0, -1):
        working_idx = scan_for_block_to_move(mem, working_idx, block_id)
        block_size = len(mem[working_idx])
        free_mem_idx = scan_for_open_mem_block(mem, block_size, 0)
        
        if free_mem_idx == -1 or free_mem_idx > working_idx:
            continue  # Cannot move block, proceed
        
        mem = move_block_to_free_memory(mem, working_idx, free_mem_idx)
        
    flattened_output = [i for sl in mem for i in sl]
    checksum = sum(idx * n for idx, n in enumerate(flattened_output) if isinstance(n, int))
        
    return checksum

if __name__ == "__main__":
    P1TEST, P2TEST = 1928, 2858
    test_input, input = parse_file("9test.txt"), parse_file("9.txt")
    print(f"Part 1 Test: {part_one(test_input[0])} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_input[0])} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input[0])}")
    print(f"Part 2: {part_two(input[0])}")