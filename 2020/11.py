###################################
####### SPOILERS FOR DAY 11 #######
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
        
def get_boundaries(r_idx, s_idx, seat_map):
        start_row = r_idx - 1 if r_idx > 0 else 0
        end_row = r_idx + 1 if r_idx < len(seat_map) - 1 else r_idx
        start_seat = s_idx - 1 if s_idx > 0 else 0
        end_seat = s_idx + 1 if s_idx < len(seat_map[0]) - 1 else s_idx
        
        return start_row, end_row, start_seat, end_seat
    
def can_take_seat(r_idx, s_idx, seat_map):
    start_row, end_row, start_seat, end_seat = get_boundaries(r_idx, s_idx, seat_map)
    
    for i in range(start_row, end_row + 1):
        for j in range(start_seat, end_seat + 1):
            if seat_map[i][j] == '#':
                return False        
    return True

def can_take_seat_strict(r_idx, s_idx, seat_map):
    start_row, end_row, start_seat, end_seat = get_boundaries(r_idx, s_idx, seat_map)
    
    def get_next_seat(i, j, direction):
        new_i, new_j = i + direction[0], j + direction[1]
        if new_i < 0 or new_i >= len(seat_map) or new_j < 0 or new_j >= len(seat_map[0]):
            return None
        if seat_map[new_i][new_j] == '.':
            return get_next_seat(new_i, new_j, direction)
        else:
            return seat_map[new_i][new_j]
    
    for i in range(start_row, end_row + 1):
        for j in range(start_seat, end_seat + 1):
            if seat_map[i][j] == '#':
                return False
            elif seat_map[i][j] == '.':
                direction = (i - r_idx, j - s_idx)
                next_seat = get_next_seat(i, j, direction)
                if next_seat == '#':
                    return False
    return True

def place_too_crowded(r_idx, s_idx, seat_map):
    start_row, end_row, start_seat, end_seat = get_boundaries(r_idx, s_idx, seat_map)
    
    other_people = 0
    for i in range(start_row, end_row + 1):
        for j in range(start_seat, end_seat + 1):                
            if seat_map[i][j] == '#':
                other_people += 1
                
                
    if other_people >= 5:       
        return True
    
    return False

def place_too_crowded_strict(r_idx, s_idx, seat_map):
    start_row, end_row, start_seat, end_seat = get_boundaries(r_idx, s_idx, seat_map)
    
    def get_next_seat(i, j, direction):
        new_i, new_j = i + direction[0], j + direction[1]
        if new_i < 0 or new_i >= len(seat_map) or new_j < 0 or new_j >= len(seat_map[0]):
            return None
        if seat_map[new_i][new_j] == '.':
            return get_next_seat(new_i, new_j, direction)
        else:
            return seat_map[new_i][new_j]
    
    other_people = 0
    for i in range(start_row, end_row + 1):
        for j in range(start_seat, end_seat + 1):  
            if seat_map[i][j] == '#':
                other_people += 1
            elif seat_map[i][j] == '.':
                direction = (i - r_idx, j - s_idx)
                if direction != (0, 0):
                    next_seat = get_next_seat(i, j, direction)
                    if next_seat == '#':
                        other_people += 1
                        
    if other_people >= 6:       
        return True
    
    return False

def part_one(input):
    # Adjacent = 8 positions: up, down, left, right, or diagonal from the seat.
    # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    # Otherwise, the seat's state does not change.
    seat_map = input
    updated_map = seat_map.copy()
    loop_count = 0
    while (True):            
        for r_idx, row in enumerate(seat_map):
            for s_idx, seat in enumerate(row):
                if seat == 'L':
                    if can_take_seat(r_idx, s_idx, seat_map):
                        updated_row = updated_map[r_idx][:s_idx] + '#' + updated_map[r_idx][s_idx+1:]
                        updated_map[r_idx] = updated_row
                elif seat == '#':
                    if place_too_crowded(r_idx, s_idx, seat_map):
                        updated_row = updated_map[r_idx][:s_idx] + 'L' + updated_map[r_idx][s_idx+1:]
                        updated_map[r_idx] = updated_row
                        
        if seat_map == updated_map:
            break
        else:
            seat_map = updated_map.copy()
            loop_count += 1
            
    return sum(s.count('#') for s in updated_map)

def part_two(input):
    # Same as part 1, but if adjacent seat == '.', keep looking in that direction until empty/occupied seat or map ends.
    seat_map = input
    updated_map = seat_map.copy()
    loop_count = 0
    while (True):            
        for r_idx, row in enumerate(seat_map):
            for s_idx, seat in enumerate(row):
                if seat == 'L':
                    if can_take_seat_strict(r_idx, s_idx, seat_map):
                        updated_row = updated_map[r_idx][:s_idx] + '#' + updated_map[r_idx][s_idx+1:]
                        updated_map[r_idx] = updated_row
                elif seat == '#':
                    if place_too_crowded_strict(r_idx, s_idx, seat_map):
                        updated_row = updated_map[r_idx][:s_idx] + 'L' + updated_map[r_idx][s_idx+1:]
                        updated_map[r_idx] = updated_row
                        
        if seat_map == updated_map:
            break
        else:
            seat_map = updated_map.copy()
            loop_count += 1
            
    return sum(s.count('#') for s in updated_map)

if __name__ == "__main__":
    P1TEST, P2TEST = 37, 26
    test_input, input = parse_file("11test.txt"), parse_file("11.txt")
    print(f"Part 1 Test: {part_one(test_input)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_input)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    print(f"Part 2: {part_two(input)}")