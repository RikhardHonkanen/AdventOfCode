###################################
####### SPOILERS FOR DAY 17 #######
###################################
########  TAKE YOUR BRAIN  ########
###### TO ANOTHER DIMENSION. ######
###################################

import os, sys

debug = False

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def print_debug(string):
    if (debug):
        print(string)
        
def expand_layers(layer_maps, min_z, max_z, inactive='.'):
    # Get the dimensions of the grid from one of the layers (assuming all layers are same size)
    x_size = len(layer_maps[0][0])  # Number of columns in each row
    y_size = len(layer_maps[0])     # Number of rows
    
    # Add new layers (entirely filled with inactive cubes)
    layer_maps[min_z - 1] = [inactive * (x_size + 2)] * (y_size + 2)  # New layer at z=min_z-1
    layer_maps[max_z + 1] = [inactive * (x_size + 2)] * (y_size + 2)  # New layer at z=max_z+1
    
    # Pad each existing layer
    for z, layer in layer_maps.items():
        if z == min_z - 1 or z == max_z + 1:
            continue
        # Pad the rows of the current layer
        layer_maps[z] = [inactive * (x_size + 2)] + [inactive + row + inactive for row in layer] + [inactive * (x_size + 2)]
        
    return layer_maps

def count_neighbours(layer_maps, _z, ridx, cidx):
    z_min = _z - 1 if _z - 1 in layer_maps else _z
    z_max = _z + 1 if _z + 1 in layer_maps else _z
    r_min = ridx - 1 if ridx > 0 else 0
    r_max = ridx + 1 if ridx < len(layer_maps) else ridx
    current_row_length = len(next(iter(layer_maps.values()))[0])
    c_min = cidx - 1 if cidx > 0 else 0
    c_max = cidx + 1 if cidx + 1 < current_row_length else cidx
    
    neighbours = 0
    
    # print(f"LAYER: {_z}, ROW: {ridx}, CUBE: {cidx}")    
    # print(f"Checking layers {z_min} to {z_max}")
    # print(f"Checking rows {r_min} to {r_max}")
    # print(f"Checking cubes {c_min} to {c_max}")
    
    for z in range(z_min, z_max + 1):
        for r in range(r_min, r_max + 1):
            for c in range(c_min, c_max + 1):
                # Make sure we're not counting the cube we're looking at itself
                if not (z == _z and r == ridx and c == cidx):
                    if layer_maps[z][r][c] == '#':
                        if (_z == -1 and ridx == 1 and cidx == 5):
                            print(f"found active neighbour at") 
                            print(f"Level: {z}, Row: {r}, Cube: {c}") 
                        neighbours += 1        
                        
    if (_z == -1 and ridx == 1 and cidx == 5):
        print(neighbours) 
    
    return neighbours

def part_one(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    boot_cycles = 1
    layer_maps = {0: input}
    after_cycle_maps = {}
    
    for _ in range(boot_cycles):
        # Add new layers and pad the existing ones
        min_z = min(layer_maps.keys())
        max_z = max(layer_maps.keys())
        layer_maps = expand_layers(layer_maps, min_z, max_z)
        # print(layer_maps)
        
        for z in range(min_z - 1, max_z + 2):
            new_layer = []
            for ridx, row in enumerate(layer_maps[z]):
                new_row = ""
                for cidx, c in enumerate(row):
                    neighbours = count_neighbours(layer_maps, z, ridx, cidx)
                    if c == '.':
                        if neighbours == 3:
                            new_row += '#'
                        else:
                            new_row += '.'
                    else:  # c == '#'
                        if not (neighbours == 2 or neighbours == 3):
                            new_row += '.'
                        else:
                            new_row += '#'
                new_layer.append(new_row)
            after_cycle_maps[z] = new_layer

        # Update layer_maps for the next cycle
        layer_maps = after_cycle_maps.copy()
        
    for r in range(min(layer_maps.keys()), max(layer_maps.keys()) + 1):
        for s in layer_maps[r]:
            print(s)
        print()
    exit()
    
    return sum(row.count('#') for layer in layer_maps.values() for row in layer)

def part_two(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    answer = 'Part two'            
    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 112, 0
    test_input, input = parse_file("17test.txt"), parse_file("17.txt")
    # print(f"Part 1 Test: {part_one(test_input, False)} (expected {P1TEST})")
    # print(f"Part 2 Test: {part_two(test_input, False)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    # print(f"Part 2: {part_two(input)}")