# ~~~ App's main code block ~~~
# 1. Get and validate user's input
# dice.py
import random

MAX_DICE = 10

def roll_dice(num_dice):
    """Return a list of integers with length `num_dice`.

    Each integer in the returned list is a random number between
    1 and 6, inclusive.
    """
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results

def do_stuff(input_string):
    """Return `input_string` as an integer between 1 and MAX_DICE.

    Check if `input_string` is an integer number between 1 and MAX_DICE.
    If so, return an integer with the same value. Otherwise, tell
    the user to enter a valid number and quit the program.
    """
    if int(input_string.strip()) in range(1, MAX_DICE):
        return int(input_string.strip())
    else:
        print(f"Please enter a number from 1 to {MAX_DICE}.")
        raise SystemExit(1)

num_dice_input = input(f"How many d6 dice do you want to roll? [1-{MAX_DICE}] ")
num_dice = do_stuff(num_dice_input)

roll_results = roll_dice(num_dice)

extra_roll = None
print(roll_results)

if roll_results[0] == 6:
    extra_roll = random.randint(1, 6)
    roll_results.append(extra_roll)
    while extra_roll == 6:
        extra_roll = random.randint(1, 6)
        roll_results.append(extra_roll)
elif roll_results[0] == 1:
    roll_results.append(-(max(roll_results)))
    roll_results.append(-1)

# Python program to find sum of elements in list
total = 0

# Iterate each element in list
# and add them in variable total
for ele in range(0, len(roll_results)):
    total = total + roll_results[ele]

print(roll_results)  # Remove this line after testing the app
print("Sum of all elements in given list: ", total)

#comment test