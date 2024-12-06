##############################
###### !!! SPOILERS !!! ######
##############################
############ DAY 5 ###########
##############################

import os, sys
from collections import defaultdict


def parse_file(path):
    with open(os.path.join(sys.path[0], path), "r") as file:
        raw_rules, raw_pages = file.read().split("\n\n")
    updates = [[int(page) for page in line.split(",")] for line in raw_pages.splitlines()]
    rules =   [[int(page) for page in line.split("|")] for line in raw_rules.splitlines()]
    rules_dict = defaultdict(list)
    for first_num, second_num in rules:
        rules_dict[first_num].append(second_num)
    return rules_dict, updates


def check_update(ordering_rules, update):
    for index, page in enumerate(update):
        for first_number, following_numbers in ordering_rules.items():
            if page == first_number:
                if any(page in following_numbers for page in update[:index]):
                    return 0
    return update[len(update)//2]


def fix_update(ordering_rules, update):
    index = 0
    while index < len(update):
        for first_number, following_numbers in ordering_rules.items():
            if update[index] == first_number:
                if any(page in following_numbers for page in update[:index]):
                    update[index], update[index-1] = update[index-1], update[index]
                    index = 0
                    break
        index += 1
    return update[len(update)//2]


def part_one(ordering_rules, updates):
    total = 0
    for update in updates:
        total += check_update(ordering_rules, update)
    return total


def part_two(ordering_rules, updates):
    total = 0
    for update in updates:
        if check_update(ordering_rules, update) == 0:
            total += fix_update(ordering_rules, update)
    return total


if __name__ == "__main__":
    P1TEST, P2TEST = 143, 123
    test_input, input = parse_file("5test.txt"), parse_file("5.txt")
    print(f"Part 1 Test: {part_one(*test_input)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(*test_input)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(*input)}")
    print(f"Part 2: {part_two(*input)}")
    
## Working solution stolen from Ari Maeda