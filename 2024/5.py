###################################
####### SPOILERS FOR DAY 05 #######
###################################

import os, sys
from collections import defaultdict, deque, Counter

def parse_file(path):
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def validate_update(rules, update) -> int:
    for rule in rules:
        a, b = map(int, rule.split('|'))
        if (a in update and b in update):
            if update.index(a) > update.index(b):
                return 0

    middle_value = int(len(update)/2)
    return update[middle_value]

# def reconcile_rules(rules):
#     # Step 1: Build the graph and indegree dictionary
#     graph = defaultdict(list)
#     indegree = defaultdict(int)
#     nodes = set()

#     for rule in rules:
#         a, b = map(int, rule.split('|'))
#         graph[a].append(b)
#         indegree[b] += 1
#         nodes.add(a)
#         nodes.add(b)
#         if a not in indegree:
#             indegree[a] = 0  # Ensure 'a' is present in indegree dictionary

#     # Step 2: Resolve ordering with heuristic if no 0-indegree nodes exist
#     ordered_rules = []
#     remaining_nodes = set(nodes)  # Track unprocessed nodes

#     while remaining_nodes:
#         # Find a node with minimal indegree as a heuristic tie-breaker
#         current = min(remaining_nodes, key=lambda node: indegree[node])
#         ordered_rules.append(current)
#         remaining_nodes.remove(current)

#         # Decrement indegree for its neighbors
#         for neighbor in graph[current]:
#             indegree[neighbor] -= 1

#     # Verify that all rules are satisfied
#     for rule in rules:
#         a, b = map(int, rule.split('|'))
#         if ordered_rules.index(a) > ordered_rules.index(b):
#             print(f"Rule broken: {a} -> {b}")

#     return ordered_rules

# def reconcile_rules(rules):
#     ordered_rules = [int(rule) for rule in rules[0].split('|')]
#     any = True
#     while(any):
#         any = False
#         for i in range (1, len(rules)):
#             a, b = map(int, rules[i].split('|'))
#             a_exists, b_exists = a in ordered_rules, b in ordered_rules
#             if (a_exists and b_exists):
#                 aidx, bidx = ordered_rules.index(a), ordered_rules.index(b)
#                 if aidx > bidx:
#                     any = True
#                     move = ordered_rules.pop(aidx)
#                     ordered_rules.insert(bidx, move)
#             elif (a_exists):
#                 ordered_rules.append(b)
#             else:
#                 ordered_rules.insert(0, a)
#     return ordered_rules

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

def part_one(input):
    split = input.index("")
    rules, updates = input[:split], input[split + 1:]

    middle_pages_sum = 0
    for update in updates:
        middle_pages_sum += validate_update(rules, list(map(int, update.split(','))))

    return middle_pages_sum

def part_two(input):
    print(input)
    exit()
    split = input.index("")
    rules, updates = input[:split], input[split + 1:]

    bad_updates = []
    for update in updates:
        if (validate_update(rules, list(map(int, update.split(',')))) == 0):
            bad_updates.append(update)

    middle_pages_sum = 0
    # top_sorted = reconcile_rules(rules)
    for bad_update in bad_updates:
        # bad_update = list(map(int, bad_update.split(',')))
        # sorted_update = [num for num in top_sorted if num in bad_update]
        # print(sorted_update)
        # middle_value = int(len(sorted_update)/2)
        d_rules = input.split('\n')
        print(d_rules[0])
        dict_rules = [[int(page) for page in line.split("|")] for line in d_rules.splitlines()]
        rules_dict = defaultdict(list)
        for first_num, second_num in rules:
            dict_rules[first_num].append(second_num)
        middle_pages_sum += fix_update(rules_dict, bad_update)

    return middle_pages_sum

if __name__ == "__main__":
    P1TEST, P2TEST = 143, 123
    test_input, input = parse_file("5test.txt"), parse_file("5.txt")
    # print(f"Part 1 Test: {part_one(test_input)} (expected {P1TEST})")
    # print(f"Part 2 Test: {part_two(test_input)} (expected {P2TEST})")
    # print()
    # print(f"Part 1: {part_one(input)}")
    print(f"Part 2: {part_two(input)}")