from classes.character import Character
import random

class Pirate(Character):
    def __init__(self):
        super().__init__()
        self.defense=8
        self.health=85
        self.special_name='trick shot'
        self.name='Pirate'

    def special(self, target):
        print('Pirate used Trick shot!')
        print('')
        roll=random.randint(1,100)
        if roll>=60:
            self.strength=self.strength*2
            self.attack(target)
            self.health-=10
            self.strength=self.strength/2
            print('Trick shot was a success!')
            print('')
        else:
            print('Trickshot was a failure :(')
            print('')
        return self

