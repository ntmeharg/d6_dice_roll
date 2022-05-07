import characters

check_character_input = input("Which roll do you want to use? ")
num_dice_input = characters.weapons.get(check_character_input)[0]
modifier = characters.weapons.get(check_character_input)[1]
print(num_dice_input)
print(modifier)