#Character Sheet
character_description = {
    "character_name": "Jean",
    "move": 10,
    "force_sensitive": True,
    "dark_side_points": 0,
    "character_points": 5,
}

attributes_skills = {
    "Dexterity": {"Default": {4,0}, "Blaster": {6,0}, "Dodge": {5,0}, "Melee Combat": {5,0}, "Melee Parry": {5,0}},
    "Perception": {"Default": {2,0}, "Search": {3,0}},
    "Knowledge": {"Default": {3,0}},
    "Strength": {"Default": {3:1}, "Brawling": {4: 1}},
    "Mechanical": {"Default": {2,2}},
    "Technical": {"Default": {3,0}, "Blaster Repair": {3:1}}
}

weapons = {
    "Heavy Blaster Pistol": {"attack": {5:0}, "damage": {5:0}},
    "Vibro Dagger": {"attack": {5:1}, "damage": {attributes_skills["Strength" + 3]}},
    "Vibro Blade": {"attack": {6:0}, "damage": {attributes_skills["Strength" + 3]}}
}

armor = {
    "Hide Vest": {"physical": {1:2}, "energy": {0:2}}
}

print(attributes_skills)
print(weapons)
print(armor)

