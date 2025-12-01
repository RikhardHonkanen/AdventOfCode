###################################
####### SPOILERS FOR DAY 05 #######
###################################

import os, sys

def parse_file(path):    
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_data = f.read().split('\n')
	return parsed_data

def part_one(data: list[str]) -> int:
    nice: int = 0
    vowels: list[str] = ['a', 'e', 'i', 'o', 'u']
    bad_words: list[str] = ["ab", "cd", "pq", "xy"]
    
    for line in data:
        naughty: bool = False
        vowel_count: int = 0
        previous: str = ' ' # char
        has_double: bool = False
        for c in line:
            subword: str = previous + c 
            if subword in bad_words:
                naughty = True
                break
            if c == previous:
                has_double = True
            if c in vowels:
                vowel_count += 1
            previous = c
        if not naughty and vowel_count >= 3 and has_double:
            nice += 1
            
    return nice

# qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
# xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
# uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
# ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
def part_two(data: list[str]) -> int:
    nice: int = 0
    for line in data:
        print(line)
    return "answer"

if __name__ == "__main__":
    P1TEST, P2TEST = 2, 2
    test_data, test_2_data, data = parse_file("5test.txt"), parse_file("5test2.txt"), parse_file("5.txt")
    # print(f"Part 1 Test: {part_one(test_data)} (expected {P1TEST})")
    print(f"Part 2 Test: {part_two(test_2_data)} (expected {P2TEST})")
    print()
    # print(f"Part 1: {part_one(data)}")
    # print(f"Part 2: {part_two(data)}")