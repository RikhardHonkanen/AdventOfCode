###################################
####### SPOILERS FOR DAY 06 #######
###################################

import os, sys

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input
        
def collate_single_group(group):
    questions_answered_yes = {""}
    questions_answered_yes.remove("")
    for p in group:
        for a in p:
            questions_answered_yes.add(a)
    
    return len(questions_answered_yes)

def collate_single_group_strict(group):
    questions_answered_yes = set()
    for idx, p in enumerate(group):
        questions_still_in_running = set()
        if idx == 0:
            for a in p:
                questions_answered_yes.add(a)
        else:
            for a in p:
                if a in questions_answered_yes:
                    questions_still_in_running.add(a)
            questions_answered_yes = questions_still_in_running 
            
    ### DEBUG            
    # print("Group: ", group)
    # print("Questions answered yes: ", questions_answered_yes)           
    # print(len(questions_answered_yes))
    ### END DEBUG            
    
    return len(questions_answered_yes)
        
def collate_answers(input, strict = False):
    current = []
    total_count = 0
    for idx, line in enumerate(input):
        if (line == ""):
            if strict: 
                total_count += collate_single_group_strict(current)
            else: 
                total_count += collate_single_group(current)
            current = []
        elif (idx == len(input) - 1):
            current.append(line)
            if strict: 
                total_count += collate_single_group_strict(current)
            else: 
                total_count += collate_single_group(current)
        else:
            current.append(line)
    
    return total_count

def part_one(input):
    answer = collate_answers(input)
    return answer

def part_two(input):
    answer = collate_answers(input, True)
    return answer

if __name__ == "__main__":
    P1TEST, P2TEST = 11, 6
    test_input, input = parse_file("6test.txt"), parse_file("6.txt")
    print(f"Part 1 Test: {part_one(test_input)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_input)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    print(f"Part 2: {part_two(input)}")