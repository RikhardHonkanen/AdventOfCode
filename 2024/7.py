###################################
####### SPOILERS FOR DAY 07 #######
###################################
### MESSAGE OF THE DAY IS: COW. ###
###################################

import os, sys, copy

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def calculate(operands):
    operator = '+'
    result = 0
    for o in operands:
        if isinstance(o, int):
            result = result + o if operator == '+' else result * o
        else:
            operator = o
    return result

def equation_possible(target, operands, index):
    # Check base cases
    if calculate(operands) == target:
        return True
    if index >= len(operands):
        return False
    
    # Recurse, swapping out operators
    for i in range(index, len(operands)):
        if operands[i] == '+':
            new_operands = copy.deepcopy(operands)
            new_operands[i] = '*'
            if equation_possible(target, new_operands, i + 1):
                return True
    return False

def part_one(input):
    sum = 0
    for equation in input:
        parts = equation.split(':')
        test_value = int(parts[0])
        operands = list(map(int, parts[1].strip().split(' ')))
        for i in range(1, len(operands) * 2 - 1, 2):    # Add a '+' as every other index
            operands.insert(i, '+')
        if equation_possible(test_value, operands, 0):
            sum += test_value
    return sum

def part_two(input):
    answer = 'Part two'            
    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 3749, 0
    test_input, input = parse_file("7test.txt"), parse_file("7.txt")
    print(f"Part 1 Test: {part_one(test_input)} (expected {P1TEST})")
    # print(f"Part 2 Test: {part_two(test_input)} (expected {P2TEST})")
    # print()
    print(f"Part 1: {part_one(input)}")
    # print(f"Part 2: {part_two(input)}")