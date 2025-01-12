# ###################################
# ####### SPOILERS FOR DAY 07 #######
# ###################################

# import os, sys, copy

# def parse_file(path):    
# 	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
# 		parsed_input = f.read().split('\n')
# 	return parsed_input

# def calculate(operands):
#     # print(operands)
#     operator = '+'
#     result = 0
#     for o in operands:
#         if isinstance(o, int):
#             result = result + o if operator == '+' else result * o
#         else:
#             operator = o
#     return result

# def get_equation_parts(equation):
#     parts = equation.split(':')
#     test_value = int(parts[0])
#     operands = list(map(int, parts[1].strip().split(' ')))
#     for i in range(1, len(operands) * 2 - 1, 2):    # Add a '+' as every other index
#         operands.insert(i, '+')
#     return test_value, operands

# def merge_at_operator(lst, operator_index):
#     new_int = int(str(lst[operator_index - 1]) + str(lst[operator_index + 1]))
#     return lst[:operator_index - 1] + [new_int] + lst[operator_index + 2:]

# def equation_possible(target, operands, index, part2=True):
#     if part2 == True and len(operands) > 2:
#         for oidx, o in enumerate(operands):
#             if isinstance(o, str):
#                 if target == 7290:
#                     print("We're here, we're square")
#                     print(operands)
#                 if target == 192:
#                     print("Looking for 192:")
#                     print(operands)
#                 thingy1 = str(calculate(operands[:oidx]))
#                 thingy2 = str(calculate(operands[oidx + 1:]))
#                 thingy = int(thingy1 + thingy2)
#                 if target == 192:
#                     print(f"Thingy one: {thingy1}, Thingy two: {thingy2}")
#                     print(f"Thingy: {thingy}")
#                 if thingy == target:
#                     return True
#     if target == 192:
#         print("Looking for 192 start:")
#         print(operands)
#     # Check base cases
#     if calculate(operands) == target:
#         return True
#     if index >= len(operands):
#         return False
    
#     # Recurse, swapping out operators
#     for i in range(index, len(operands)):
#         if operands[i] == '+':
#             new_operands = copy.deepcopy(operands)
#             new_operands[i] = '*'
            
#             if equation_possible(target, new_operands, i + 1, part2):
#                 return True
#     return False

# def part_one(input):
#     sum = 0
#     for equation in input:
#         test_value, operands = get_equation_parts(equation)
#         if equation_possible(test_value, operands, 0, False):
#             sum += test_value
#     return sum

# def part_two(input):
#     sum = 0
#     for equation in input:
#         test_value, operands = get_equation_parts(equation)
#         if equation_possible(test_value, operands, 0, True):
#             sum += test_value
#     return sum

# if __name__ == "__main__":
#     P1TEST, P2TEST = 3749, 11387
#     test_input, input = parse_file("7test.txt"), parse_file("7.txt")
#     # print(f"Part 1 Test: {part_one(test_input)} (expected {P1TEST})")
#     print(f"Part 2 Test: {part_two(test_input)} (expected {P2TEST})")
#     # print()
#     # print(f"Part 1: {part_one(input)}")
#     # print(f"Part 2: {part_two(input)}")
    
    
##############################
###### !!! SPOILERS !!! ######
##############################
############ DAY 7 ###########
##############################

import os, sys
import re


def parse_file(path):
    with open(os.path.join(sys.path[0], path), "r") as file:
        split_input = file.read().splitlines()
    list_of_equations = [[int(number) for number in re.findall("\d+", line)] for line in split_input]
    return list_of_equations  # [[190, 10, 19], ...]


def find_valid_equations(test_value, total, remaining_operands, operator=None, part2=False, count=0):
    if remaining_operands == []:
        if total == test_value:
            return 1
        return 0

    if operator == None:   total =  remaining_operands[0]  # To set up the first iteration.
    elif operator == "+":  total += remaining_operands[0]
    elif operator == "*":  total *= remaining_operands[0]
    elif operator == "||": total = int(str(total) + str(remaining_operands[0]))

    if total > test_value:
        return 0
    
    count += find_valid_equations(test_value, total, remaining_operands[1:], "+", part2)
    count += find_valid_equations(test_value, total, remaining_operands[1:], "*", part2)
    count += find_valid_equations(test_value, total, remaining_operands[1:], "||", part2) if part2 else 0
    return count


def both_parts(list_of_equations, part2=False):
    total = 0
    for equation in list_of_equations:
        test_value, operands = equation[0], equation[1:]
        if find_valid_equations(test_value, 0, operands, part2=part2) > 0:
            total += test_value
    return total


if __name__ == "__main__":
    P1TEST, P2TEST = 3749, 11387
    test_input, input = parse_file("7test.txt"), parse_file("7.txt")
    print(f"Part 1 Test: {both_parts(test_input)} (expected {P1TEST})")
    print(f"Part 2 Test: {both_parts(test_input, True)} (expected {P2TEST})")
    print()
    print(f"Part 1: {both_parts(input)}")
    print(f"Part 2: {both_parts(input, True)}")

# Credits to Ari Maeda for working solution, got stuck debugging my own and wanted to move on for now. His notes:

# #  This makes for three easy days in a row, so I'm very scared for tomorrow! Part 1 was a straightforward recursive
# #  search through all of the possible combinations of equations. I struggled a bit with an oversight where I was
# #  returning 1 if the total matched the test value even with operands remaining, so I got the correct test answer but
# #  not the actual, which is fun. Part 2 was a gimme, just requiring an extra operator and a flag to enable it.
# #
# #  Takes 9 seconds to run without debugger.