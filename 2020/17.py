# ###################################
# ####### SPOILERS FOR DAY 17 #######
# ###################################
# ########  TAKE YOUR BRAIN  ########
# ###### TO ANOTHER DIMENSION. ######
# ###################################

# import os, sys, copy

# debug = False

# def parse_file(path):    
# 	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
# 		parsed_input = f.read().split('\n')
# 	return parsed_input

# def print_debug(string):
#     if (debug):
#         print(string)
        
# def expand_layers(layer_maps, min_z, max_z, inactive='.'):
#     # Get the dimensions of the grid from one of the layers (assuming all layers are same size)
#     x_size = len(layer_maps[0][0])  # Number of columns in each row
#     y_size = len(layer_maps[0])     # Number of rows
    
#     # Add new layers (entirely filled with inactive cubes)
#     layer_maps[min_z - 1] = [inactive * (x_size + 2) for _ in range(y_size + 2)]
#     layer_maps[max_z + 1] = [inactive * (x_size + 2) for _ in range(y_size + 2)]
    
#     # Pad each existing layer
#     for z, layer in layer_maps.items():
#         if z == min_z - 1 or z == max_z + 1:
#             continue
#         # Pad the rows of the current layer
#         layer_maps[z] = [inactive * (x_size + 2)] + [inactive + row + inactive for row in layer] + [inactive * (x_size + 2)]
        
#     return layer_maps

# def count_neighbours(layer_maps, _z, ridx, cidx):
#     z_min = _z - 1 if _z - 1 in layer_maps else _z
#     z_max = _z + 1 if _z + 1 in layer_maps else _z
#     r_min = ridx - 1 if ridx > 0 else 0
#     r_max = ridx + 1 if ridx < len(layer_maps) else ridx
#     current_row_length = len(next(iter(layer_maps.values()))[0])
#     c_min = cidx - 1 if cidx > 0 else 0
#     c_max = cidx + 1 if cidx + 1 < current_row_length else cidx
    
#     neighbours = 0
    
#     # print(f"LAYER: {_z}, ROW: {ridx}, CUBE: {cidx}")    
#     # print(f"Checking layers {z_min} to {z_max}")
#     # print(f"Checking rows {r_min} to {r_max}")
#     # print(f"Checking cubes {c_min} to {c_max}")
    
#     for z in range(z_min, z_max + 1):
#         for r in range(r_min, r_max + 1):
#             for c in range(c_min, c_max + 1):
#                 # Make sure we're not counting the cube we're looking at itself
#                 if not (z == _z and r == ridx and c == cidx):
#                     if layer_maps[z][r][c] == '#':
#                         neighbours += 1        
#                         # if (_z == -1 and ridx == 1 and cidx == 5):
#                         #     print(f"found active neighbour at") 
#                         #     print(f"Level: {z}, Row: {r}, Cube: {c}") 
                        
#     # if (_z == -1 and ridx == 1 and cidx == 5):
#     #     print(neighbours) 
    
#     return neighbours

# def part_one(input, _debug = False):
#     if (_debug):
#         global debug
#         debug = True
        
#     boot_cycles = 6
#     layer_maps = {0: input}
#     after_cycle_maps = {}
    
#     for _ in range(boot_cycles):
#         # Add new layers and pad the existing ones
#         min_z = min(layer_maps.keys())
#         max_z = max(layer_maps.keys())
#         layer_maps = expand_layers(layer_maps, min_z, max_z)
#         # print(layer_maps)
        
#         for z in range(min_z - 1, max_z + 2):
#             new_layer = []
#             for ridx, row in enumerate(layer_maps[z]):
#                 new_row = ""
#                 for cidx, c in enumerate(row):
#                     neighbours = count_neighbours(layer_maps, z, ridx, cidx)
#                     if c == '.':
#                         if neighbours == 3:
#                             new_row += '#'
#                         else:
#                             new_row += '.'
#                     else:  # c == '#'
#                         if not (neighbours == 2 or neighbours == 3):
#                             new_row += '.'
#                         else:
#                             new_row += '#'
#                 new_layer.append(new_row)
#             after_cycle_maps[z] = new_layer

#         # Update layer_maps for the next cycle
#         layer_maps = copy.deepcopy(after_cycle_maps)
        
#     # for r in range(min(layer_maps.keys()), max(layer_maps.keys()) + 1):
#     #     for s in layer_maps[r]:
#     #         print(s)
#     #     print()
    
#     return sum(row.count('#') for layer in layer_maps.values() for row in layer)

# def part_two(input, _debug = False):
#     if (_debug):
#         global debug
#         debug = True
        
#     answer = 'Part two'            
#     return answer

# if __name__ == "__main__":
#     P1TEST, P2TEST = 112, 0
#     test_input, input = parse_file("17test.txt"), parse_file("17.txt")
#     # print(f"Part 1 Test: {part_one(test_input, False)} (expected {P1TEST})")
#     # print(f"Part 2 Test: {part_two(test_input, False)} (expected {P2TEST})")
#     print()
#     print(f"Part 1: {part_one(input)}")
#     # print(f"Part 2: {part_two(input)}")

### TODO: fix or redo implementation above, some nasty bug causing part_one to output 262, correct is 295 (test case correctly outputs 112)
### borrowed solution from https://github.com/elvinyhlee/advent-of-code-2020-python/blob/master/day17.py

import os, sys, copy, itertools

ACTIVE = '#'
INACTIVE = '.'

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def part_one(data):
    # Initialize grid
    rows = len(data)
    columns = len(data[0])
    loops = 6
    expanded = loops * 2

    grid = [[['.' for _ in range(columns + expanded)] for _ in range(rows + expanded)] for _ in range(1 + expanded)]
    for ix, i in enumerate(data):
        for jx, j in enumerate(i):
            grid[loops][ix + loops][jx + loops] = j

    # Run 6 cycles
    si = sj = sk = loops - 1  # s means start from

    for loop in range(loops):
        grid_clone = copy.deepcopy(grid)

        range_expanded = 2 * (loop + 1)
        for i in range(1 + range_expanded):
            for j in range(rows + range_expanded):
                for k in range(columns + range_expanded):
                    count_active = 0
                    for z in itertools.product([0, 1, -1], repeat=3):
                        if not(z == (0, 0, 0))\
                                and (0 <= i + si + z[0] < 1 + expanded) \
                                and (0 <= j + sj + z[1] < rows + expanded) \
                                and (0 <= k + sk + z[2] < columns + expanded) \
                                and (grid[i + si + z[0]][j + sj + z[1]][k + sk + z[2]] == ACTIVE):
                            count_active += 1

                    if (grid[i + si][j + sj][k + sk] == ACTIVE) and (not(2 <= count_active <= 3)):
                        grid_clone[i + si][j + sj][k + sk] = INACTIVE

                    if (grid[i + si][j + sj][k + sk] == INACTIVE) and (count_active == 3):
                        grid_clone[i + si][j + sj][k + sk] = ACTIVE
        grid = grid_clone
        si, sj, sk = si - 1, sj - 1, sk - 1

    # Count active cubes
    active = 0
    for i in range(1 + expanded):
        for j in range(rows + expanded):
            for k in range(columns + expanded):
                if grid[i][j][k] == ACTIVE:
                    active += 1
    return active


def part_two(data):
    # Initialize grid
    rows = len(data)
    columns = len(data[0])
    loops = 6
    expanded = loops * 2

    grid = [[[['.' for _ in range(columns + expanded)] for _ in range(rows + expanded)]
             for _ in range(1 + expanded)] for _ in range(1 + expanded)]
    for ix, i in enumerate(data):
        for jx, j in enumerate(i):
            grid[loops][loops][ix + loops][jx + loops] = j

    # Run 6 cycles
    si = sj = sk = sl = loops - 1  # s means start from

    for loop in range(loops):
        grid_clone = copy.deepcopy(grid)

        range_expanded = 2 * (loop + 1)
        for i in range(1 + range_expanded):
            for j in range(1 + range_expanded):
                for k in range(rows + range_expanded):
                    for l in range(columns + range_expanded):
                        count_active = 0
                        for z in itertools.product([0, 1, -1], repeat=4):
                            if not(z == (0, 0, 0, 0))\
                                    and (0 <= i + si + z[0] < 1 + expanded) \
                                    and (0 <= j + sj + z[1] < 1 + expanded) \
                                    and (0 <= k + sk + z[2] < rows + expanded) \
                                    and (0 <= l + sl + z[3] < columns + expanded) \
                                    and (grid[i + si + z[0]][j + sj + z[1]][k + sk + z[2]][l + sl + z[3]] == ACTIVE):
                                count_active += 1

                        if (grid[i + si][j + sj][k + sk][l + sl] == ACTIVE) and (not(2 <= count_active <= 3)):
                            grid_clone[i + si][j + sj][k + sk][l + sl] = INACTIVE

                        if (grid[i + si][j + sj][k + sk][l + sl] == INACTIVE) and (count_active == 3):
                            grid_clone[i + si][j + sj][k + sk][l + sl] = ACTIVE
        grid = grid_clone
        si, sj, sk, sl = si - 1, sj - 1, sk - 1, sl - 1

    # Count active cubes
    active = 0
    for i in range(1 + expanded):
        for j in range(1 + expanded):
            for k in range(rows + expanded):
                for l in range(columns + expanded):
                    if grid[i][j][k][l] == ACTIVE:
                        active += 1
    return active


if __name__ == "__main__":
    P1TEST, P2TEST = 0, 0
    test_input, input = parse_file("17test.txt"), parse_file("17.txt")
    print(f"Part 1 Test: {part_one(test_input)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_input)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    print(f"Part 2: {part_two(input)}")