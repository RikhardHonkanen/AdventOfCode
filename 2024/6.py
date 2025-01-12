###################################
####### SPOILERS FOR DAY 06 #######
###################################

import os, sys, copy

FACING     = ["UP", "RIGHT", "DOWN", "LEFT"]
DIRECTIONS = {"UP": '^', "RIGHT": '>', "DOWN": 'v', "LEFT": '<'}
MOVE       = {"UP": (-1, 0), "RIGHT": (0, 1), "DOWN": (1, 0), "LEFT": (0, -1)}

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def get_position(lab_map, facing):
    for idx, row in enumerate(lab_map):
        if facing in row:
            return (idx, row.index(facing))
        
def set_data(lab_map):
    facing = FACING[0]
    position  = get_position(lab_map, DIRECTIONS[facing])
    rows = len(lab_map)
    row_length = len(lab_map[0])
    return facing, position, rows, row_length
        
def turn_right(facing):
    current_index = FACING.index(facing)
    next_index = (current_index + 1) % len(FACING)
    return FACING[next_index]

def out_of_bounds(position, rows, row_length):
    if position[0] < 0 or position[0] >= rows:
        return True
    if position[1] < 0 or position[1] >= row_length:
        return True
    return False

def part_one(lab_map):
    facing, position, rows, row_length = set_data(lab_map)
    visited = copy.deepcopy(lab_map)
    
    while(True):
        maybe_move_to = tuple(a + b for a, b in zip(position, MOVE[facing]))
        if out_of_bounds(maybe_move_to, rows, row_length):
            visited[position[0]] = visited[position[0]][:position[1]] + 'X' + visited[position[0]][position[1] + 1:]
            break
        if (lab_map[maybe_move_to[0]][maybe_move_to[1]] == '#'):
            facing = turn_right(facing)
        else:
            visited[position[0]] = visited[position[0]][:position[1]] + 'X' + visited[position[0]][position[1] + 1:]
            position = maybe_move_to
    return sum(s.count('X') for s in visited)

def part_two(lab_map):
    init_facing, init_position, rows, row_length = set_data(lab_map)
    loops = 0
    for ridx, row in enumerate(lab_map):
        for cidx, c in enumerate(row):
            if c == '#':  # Skip obstacles
                continue
            
            position = init_position
            facing = init_facing
            visited = {}
            visited[position] = {facing}
            temp_map = [list(r) for r in lab_map]
            temp_map[ridx][cidx] = '#'
            while True:
                maybe_move_to = tuple(a + b for a, b in zip(position, MOVE[facing]))
                if out_of_bounds(maybe_move_to, rows, row_length):
                    break
                if temp_map[maybe_move_to[0]][maybe_move_to[1]] == '#':
                    facing = turn_right(facing)
                else:
                    if maybe_move_to in visited and facing in visited[maybe_move_to]:
                        loops += 1
                        break
                    if maybe_move_to not in visited:
                        visited[maybe_move_to] = {facing}
                    else:
                        visited[maybe_move_to].add(facing)
                    position = maybe_move_to  # Move to the next position

    return loops

if __name__ == "__main__":
    P1TEST, P2TEST = 41, 6
    test_input, input = parse_file("6test.txt"), parse_file("6.txt")
    print(f"Part 1 Test: {part_one(test_input)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_input)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    print(f"Part 2: {part_two(input)}")