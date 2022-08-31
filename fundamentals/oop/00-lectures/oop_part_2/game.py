# from game classes import character
from game_classes.character import Character
from game_classes.pokemon import Pokemon
import random

bob=Character()
bulbasaur=Pokemon('grass', 50)

while(bob.health >0 and bulbasaur.health >0):
    response = input("You're bob, will you attack or recuperate? \n 1) attack \n 2) heal \n")
    if response == '1':
        bob.attack(bulbasaur)
    elif response=='2':
        bob.heal()
    else:
        while(response != '1' and response != '2'):
            print('Please pick a valid option')
            response = input("You're bob, will you attack or recuperate? \n 1) attack \n 2) heal \n")
    
    response = input("You're bulbasaur, will you attack or recuperate? \n 1) attack \n 2) heal \n")
    if response == '1':
        bulbasaur.attack(bob)
    elif response=='2':
        bulbasaur.heal()
    else:
        while(response != '1' and response != '2'):
            print('Please pick a valid option')
            response = input("You're bulbasaur, will you attack or recuperate? \n 1) attack \n 2) heal \n")
    
    # roll = random.randint(1,4)
    # if roll==1:
    #     bulbasaur.attack(bob)
    #     print("bulbasaur attacks")
    # elif roll==2:
    #     bulbasaur.heal()
    #     print("bulbsaur heals")
    # elif roll==3:
    #     bulbasaur.evolve()
    #     print("Bulbasaur evolved!")
    # elif roll==4:
    #     print('Bulbasaur did nothing lmao')

    print('')
    print("Bob: ")
    bob.print_info()
    print('')
    print("Bulba: ")
    bulbasaur.print_info()

if bulbasaur.health>0:
    print('')
    print('Bulba has defeated bob!!!')
    print('')
if bob.health>0:
    print('')
    print("Bob has defeated bulba!!!")
    print('')
if bob.health<=0 and bulbasaur.health <=0:
    print('')
    print('They knocked each other out!!!')
    print('')
