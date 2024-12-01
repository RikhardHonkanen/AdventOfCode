###################################
####### SPOILERS FOR DAY 01 #######
###################################
## IT'S FREAKING DECEMBER AGAIN. ##
###################################

import os, sys
from bisect import bisect_left, bisect_right

debug = False

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def print_debug(string):
    if (debug):
        print(string)
        
def count_occurrences(sorted_list, number):
    left = bisect_left(sorted_list, number)
    right = bisect_right(sorted_list, number)
    return right - left

def part_one(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    list1, list2 = zip(*[map(int, s.split()) for s in input])
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    
    answer = 0
    for idx, n in enumerate(sorted_list1):
        answer += abs(n - sorted_list2[idx])

    return answer

def part_two(input, _debug = False):
    if (_debug):
        global debug
        debug = True
        
    list1, list2 = zip(*[map(int, s.split()) for s in input])
    sorted_list2 = sorted(list2)
    
    answer = 0
    for n in list1:
        answer += n * count_occurrences(sorted_list2, n)

    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 11, 31
    test_input, input = parse_file("1test.txt"), parse_file("1.txt")
    print(f"Part 1 Test: {part_one(test_input, False)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_input, False)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    print(f"Part 2: {part_two(input)}")