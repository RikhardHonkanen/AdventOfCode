import random
num_dice = 2
list_words = ["num", "py", "leaden", "omni", "colors", "numpty"]

def roll_dice(num_dice):
    """Return a list of integers with length `num_dice`.

    Each integer in the returned list is a random number between
    1 and 6, inclusive.
    """
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        index = random.randint(0, len(list_words) - 1)

        roll_results.append(str(roll) + list_words[index])
    return roll_results

roll_results = roll_dice(num_dice)

print(roll_results) 