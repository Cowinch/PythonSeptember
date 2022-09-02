from classes.character import Character
from classes.pirate import Pirate
from classes.barbarian import Barbarian
from classes.ninja import Ninja
import random

player1 = Character()

player2 = Character()

def randomRoll():
    rand=random.randint(1,3)

player1ready=False
player2ready=False
while(player1ready==False):
    print('')
    response = input('Player 1, please decide a class:\n 1) Pirate \n 2) Barbarian\n 3) Ninja\n 4) Random \n')
    if response == '1':
        player1=Pirate()
        player1ready=True
    elif response=='2':
        player1=Barbarian()
        player1ready=True
    elif response=='3':
        player1=Ninja()
        player1ready=True
    elif response=='4':
        rand=random.randint(1,3)
        if rand==1:
            player1=Pirate()
            player1ready=True
        elif rand==2:
            player1=Barbarian()
            player1ready=True
        elif rand==3:
            player1=Ninja()
            player1ready=True
    else:
        while(response != '1' and response != '2' and response != '3' and response != '4'):
            print('')
            response = input('Player 1, please decide a class:\n 1) Pirate \n 2) Barbarian\n 3) Ninja\n 4) Random \n')

print('')
player1.show_stats()


while(player2ready==False):
    print('')
    response = input('Player 2, please decide a class:\n 1) Pirate \n 2) Barbarian\n 3) Ninja\n 4) Random \n')
    if response == '1':
        player2=Pirate()
        player2ready=True
    elif response=='2':
        player2=Barbarian()
        player2ready=True
    elif response=='3':
        player2=Ninja()
        player2ready=True
    elif response=='4':
        rand=random.randint(1,3)
        if rand==1:
            player2=Pirate()
            player2ready=True
        elif rand==2:
            player2=Barbarian()
            player2ready=True
        elif rand==3:
            player2=Ninja()
            player2ready=True
    else:
        while(response != '1' and response != '2' and response != '3' and response != '4'):
            print('')
            response = input('Player 2, please decide a class:\n 1) Pirate \n 2) Barbarian\n 3) Ninja\n 4) Random \n')

print('')
player2.show_stats()

while(player1.health >0 and player2.health >0):
    response = input(f"Player 1: {player1.name}, will you attack or recuperate, or use your special? \n 1) attack \n 2) recuperate \n 3) {player1.special_name}\n" )
    if response == '1':
        player1.attack(player2)
    elif response=='2':
        player1.healing()
    elif response=='3':
        player1.special(player2)
    else:
        while(response != '1' and response != '2' and response != '3'):
            print('Please pick a valid option')
            response = input(f"Player 1: {player1.name}, will you attack or recuperate, or use your special? \n 1) attack \n 2) recuperate \n 3) {player1.special_name}\n" )


    response = input(f"Player 2: {player2.name}, will you attack or recuperate, or use your special? \n 1) attack \n 2) recuperate \n 3) {player2.special_name}\n" )
    if response == '1':
        player2.attack(player1)
    elif response=='2':
        player2.healing()
    elif response=='3':
        player2.special(player1)
    else:
        while(response != '1' and response != '2'):
            print('Please pick a valid option')
            response = input(f"Player 2: {player2.name}, will you attack or recuperate, or use your special? \n 1) attack \n 2) recuperate \n 3) {player2.special_name}\n" )


    print('')
    print(f"Player 1: {player1.name} ")
    player1.show_stats()
    print('')
    print(f"Player 2: {player2.name} ")
    player2.show_stats()
    print('')


if player1.health>0:
    print('')
    print('Player 2 has defeated Player 1!!!')
    print('')
if player2.health>0:
    print('')
    print("Player 2 has defeated Player 1!!!")
    print('')
if player1.health<=0 and player2.health <=0:
    print('')
    print('They knocked each other out!!!')
    print('')
