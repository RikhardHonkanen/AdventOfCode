#################
### SPOILERS  ###
### FOR DAY 2 ###
### OF AOC    ###
#################

## red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

##  once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

##  which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

import os, sys
import re

available_cubes = {
    "red": "12",
    "green": "13",
    "blue": "14",
}

def check_if_roll_is_possible(roll):
    roll_cubes = roll.split(',')
    for cube_color in roll_cubes:
        number = int(re.search(r'\d+', cube_color).group())
        for key in available_cubes.keys():
            if (key in cube_color):
                if (int(available_cubes[key]) < number):
                    return False
    return True
        
def populate_possible_games(games):
    for idx, g in enumerate(games):
        if(check_single_game(g)):
            possible_games.append(idx + 1)
        
def clean_up_single_game(g):
    index = g.index(':')
    return g[index + 1:len(g)]
           
def check_single_game(g):
    input = clean_up_single_game(g)
    rolls = input.split(';')
    for roll in rolls:
        if(not check_if_roll_is_possible(roll)):
            return False
    return True

def parse_file(path):
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split("\n")
	return parsed_input

def reverse_string(input):
  return input[::-1]

def add_all_possible_games(possible_games):
    sum = 0
    for res in possible_games:
        sum += int(res)
    return sum

# print(check_if_roll_is_possible('17 red, 2 green'))
# exit()

possible_games = []
games = parse_file('2.txt')
populate_possible_games(games)
answer = add_all_possible_games(possible_games)
print(answer)