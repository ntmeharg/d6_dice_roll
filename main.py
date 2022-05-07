# ~~~ App's main code block ~~~
# 1. Get and validate user's input
# dice.py
import random
import characters

MAX_DICE = 12

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

def check_number_of_dice(input_string):
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

def total_dice_roll(total,roll_results, modifier):
    """Return 'total' to sum up roll results plus modifier

       loop through roll_results to get total plus modifier
        """
    # Iterate each element in list
    # and add them in variable total
    for ele in range(0, len(roll_results)):
        total = total + roll_results[ele]
    total = total + modifier
    print(roll_results)
    return total

#Set variables for dice roll
total = 0
modifier = 0

#Ask which character roll they want to use
check_character_input = input("Which roll do you want to use? ")
if check_character_input in characters.attributes_skills:
    skill_input = input("Which skill would you like to use? ")
    if skill_input in characters.attributes_skills[check_character_input]:
        num_dice = characters.attributes_skills[check_character_input][skill_input][0]
        modifier = characters.attributes_skills[check_character_input][skill_input][1]
    else:
        print("Sorry skill doesn't exist we will roll the attribute")
        num_dice = characters.attributes_skills[check_character_input]["Default"][0]
        modifier = characters.attributes_skills[check_character_input]["Default"][1]
elif check_character_input in characters.weapons:
    num_dice = characters.weapons.get(check_character_input)[0]
    modifier = characters.weapons.get(check_character_input)[1]
elif check_character_input in characters.armor:
    num_dice = characters.armor.get(check_character_input)[0]
    modifier = characters.armor.get(check_character_input)[1]
else:
    num_dice_input = input(f"How many d6 dice do you want to roll? [1-{MAX_DICE}] ")
    num_dice = check_number_of_dice(num_dice_input)
    modifier_input = input("Do you have any modifiers you would like to add? y/n ")
    if modifier_input[0] == "y":
        modifier = input("How much do you want to add? ")
        modifier = int(modifier)

roll_results = roll_dice(num_dice)

total = total_dice_roll(total,roll_results,modifier)

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

total = 0
total = total_dice_roll(total,roll_results,modifier)

print("Crit Total: ", total)

# print("Crit Total: ", total)