import random

from numpy import character
#print(random.randint(1,20))

def roll_dice(number_dice=0,number_sides=1,bonus=0):
    output = 0
    for x in range(0,number_dice):
        output +=random.randint(1,number_sides)
    return output + bonus

# x = roll_dice()
# print (x)
# print(roll_dice(2,6,1))
# print(roll_dice(2,6,bonus = 1))
# print(roll_dice(number_dice = 2,number_sides = 6,bonus = 1))
# print(roll_dice(bonus = 1 ,number_dice = 2,number_sides = 6)) 
#just apply to the first object
# print(roll_dice(6))



# create a character in game
# strength, constitution, dexterity, intelligence, wisdom, charisma
# value range is 3 - 18

# def generate_classic_character():

#     character = {}
#     stats = ['STR', 'CON', 'DEX', 'INT', 'WIS', 'CHA']

#     character[stats[0]] = roll_dice(3,6)
#     character[stats[1]] = roll_dice(3,6)
#     character[stats[2]] = roll_dice(3,6)
#     character[stats[3]] = roll_dice(3,6)
#     character[stats[4]] = roll_dice(3,6)
#     character[stats[5]] = roll_dice(3,6)
    
#     return character


# def generate_classic_character():

#     character = {}
#     stats = ['STR', 'CON', 'DEX', 'INT', 'WIS', 'CHA']

#     for stat in stats:
#         character[stat] = roll_dice(3,6)
    
#     return character



def generate_classic_character(die=(3,6), stats = ['STR', 'CON', 'DEX', 'INT', 'WIS', 'CHA']):

    character = {}

    for stat in stats:
        character[stat] = roll_dice(die[0], die[1])
    
    return character

print(generate_classic_character())