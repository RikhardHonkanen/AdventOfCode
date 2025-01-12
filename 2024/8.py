###################################
####### SPOILERS FOR DAY 08 #######
###################################

import os, sys, copy

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def get_antenna_coordinates(antenna_map):
    antenna_coords = {}
    for ridx, row in enumerate(antenna_map):
        for cidx, c in enumerate(row):
            if c == '.':
                continue
            if c in antenna_coords:
                antenna_coords[c] += [(ridx, cidx)]
            else:
                antenna_coords[c] = [(ridx, cidx)]
    return antenna_coords

def get_antinodes_by_type(antenna_coords_single_type, MAX_ROW, MAX_CHR, part2):
    if len(antenna_coords_single_type) <= 1:
        return set()
    type_antinodes = set()
    for coord in antenna_coords_single_type:
        for compare_coord in antenna_coords_single_type:
            if coord == compare_coord:
                if part2:
                    type_antinodes.add(coord) # Add the position of the antenna itself, always has antinode
                continue
            delta = tuple(a - b for a, b in zip(compare_coord, coord))
            antinode = tuple(a + b for a, b in zip(compare_coord, delta))
            if 0 <= antinode[0] < MAX_ROW and 0 <= antinode[1] < MAX_CHR:
                type_antinodes.add(antinode)
            while(part2): # Keep adding in-bound antinodes
                next_antinode = tuple(a + b for a, b in zip(antinode, delta))
                if 0 <= next_antinode[0] < MAX_ROW and 0 <= next_antinode[1] < MAX_CHR:
                    type_antinodes.add(next_antinode)
                    antinode = next_antinode
                else:
                    break
    return type_antinodes

def both_parts(antenna_map, part2=False):
    MAX_ROW = len(antenna_map)
    MAX_CHR = len(antenna_map[0])
    antenna_coords = get_antenna_coordinates(antenna_map)
    antinodes = set()
    for antenna_type in antenna_coords:
        antinodes.update(get_antinodes_by_type(antenna_coords[antenna_type], MAX_ROW, MAX_CHR, part2))
        
    return len(antinodes)

if __name__ == "__main__":
    P1TEST, P2TEST = 14, 34
    test_input, input = parse_file("8test.txt"), parse_file("8.txt")
    print(f"Part 1 Test: {both_parts(test_input)} (expected {P1TEST})")
    print(f"Part 2 Test: {both_parts(test_input, True)} (expected {P2TEST})")
    print()
    print(f"Part 1: {both_parts(input)}")
    print(f"Part 2: {both_parts(input, True)}")