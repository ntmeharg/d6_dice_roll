# ~~~ App's main code block ~~~
# 1. Get and validate user's input
# dice.py
import random

MAX_DICE = 12
total = 0

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
    if int(input_string.strip()) in range(MAX_DICE + 1):
        return int(input_string.strip())
    else:
        print(f"Please enter a number from 1 to {MAX_DICE}.")
        raise SystemExit(1)

num_dice_input = input(f"How many d6 dice do you want to roll? [1-{MAX_DICE}] ")
num_dice = do_stuff(num_dice_input)

#Set variables for dice roll
roll_results = roll_dice(num_dice)
extra_roll = None

##TODO: write something since I duplicate this twice
total = 0
# Iterate each element in list
# and add them in variable total
for ele in range(0, len(roll_results)):
    total = total + roll_results[ele]
print(roll_results)
print("Total: ", total)

#d6 crit success/crit fail
#If 1st die is 6 you roll an extra dice and as long as the extra dice is 6 you keep rerolling
#If 1st die is 1 you subtract it and the highest die
if roll_results[0] == 6:
    extra_roll = random.randint(1, 6)
    roll_results.append(extra_roll)
    while extra_roll == 6:
        extra_roll = random.randint(1, 6)
        roll_results.append(extra_roll)
elif roll_results[0] == 1 and len(roll_results) == 1:
    roll_results.clear()
elif roll_results[0] == 1:
    roll_results.remove(max(roll_results))
    roll_results.pop(0)

# Python program to find sum of elements in list
##TODO: write something since I duplicate this twice
total = 0

# Iterate each element in list
# and add them in variable total
for ele in range(0, len(roll_results)):
    total = total + roll_results[ele]

modifier_input = input("Do you have any modifiers you would like to add? y/n ")
if modifier_input[0] == "y":
    modifier = input("How much do you want to add? ")
    modifier = int(modifier)
    total = total + modifier

print(roll_results)
print("Crit Total: ", total)