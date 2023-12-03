#################
### SPOILERS  ###
### FOR DAY 2 ###
### OF AOC    ###
#################

import os, sys
import re

cube_colors = ["red", "green", "blue"]
        
def populate_results(games):
    for game in games:
        # result = product of minimum blue red and green required
        result = check_single_game_b(game)
        results.append(result)
        pass
    
def get_grb_values(roll):
    grb_values = {"blue": 0, "red": 0, "green": 0}    
    roll_cubes = roll.split(',')
    for cube_color in roll_cubes:
        number = int(re.search(r'\d+', cube_color).group())
        for color in cube_colors:
            if (color in cube_color):
                grb_values[color] = number
    return(grb_values)

def compare_to_maxes(maxes, current):
    for color in maxes.keys():
        if current[color] > maxes[color]:
            maxes[color] = current[color]
    return maxes

def get_product_of_maxes(maxes):
    answer = 1
    for color in maxes.keys():
            answer = answer * maxes[color]
    return answer
        
def clean_up_single_game(g):
    index = g.index(':')
    return g[index + 1:len(g)]
           
def check_single_game_b(g):
    maxes = {"blue": 0, "red": 0, "green": 0}
    input = clean_up_single_game(g)
    rolls = input.split(';')
    for roll in rolls:
        current = get_grb_values(roll)
        maxes = compare_to_maxes(maxes, current)        
    return get_product_of_maxes(maxes)

def parse_file(path):
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path), "r") as f:
		parsed_input = f.read().split("\n")
	return parsed_input

def add_all_results(results):
    sum = 0
    for res in results:
        sum += int(res)
    return sum

results = []
games = parse_file('2.txt')
populate_results(games)
answer = add_all_results(results)
print(answer)