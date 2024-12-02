###################################
####### SPOILERS FOR DAY 02 #######
###################################
##### RICHARD RAPPORT IS SAFE #####
###################################

import os, sys

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split('\n')
	return parsed_input

def report_is_safe(report):
    if len(report) < 2 or report[1] == report[0]:
        return 0

    increasing = report[1] > report[0] # Set the trend
    for n in range(1, len(report)):
        diff = report[n] - report[n - 1]
        if (increasing and (diff <= 0 or abs(diff) > 3)) or \
           (not increasing and (diff >= 0 or abs(diff) > 3)):
            return 0

    return 1

def part_one(input):
    reports = [list(map(int, s.split())) for s in input]
    
    safe_reports = 0    
    for report in reports:
        safe_reports += report_is_safe(report)
        
    return safe_reports

def part_two(input):
    reports = [list(map(int, s.split())) for s in input]
    
    safe_reports = 0    
    for report in reports:
        if report_is_safe(report) == 1:
            safe_reports += 1
        else:
            for idx, _ in enumerate(report):
                modified_report = report[:idx] + report[idx+1:]
                if report_is_safe(modified_report) == 1:
                    safe_reports += 1
                    break
            
    return safe_reports

if __name__ == "__main__":
    P1TEST, P2TEST = 2, 4
    test_input, input = parse_file("2test.txt"), parse_file("2.txt")
    print(f"Part 1 Test: {part_one(test_input)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_input)} (expected {P2TEST})")
    print()
    print(f"Part 1: {part_one(input)}")
    print(f"Part 2: {part_two(input)}")