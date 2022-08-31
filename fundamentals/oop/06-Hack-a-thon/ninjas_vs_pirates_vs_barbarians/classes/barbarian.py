from classes.character import Character
import random

class Barbarian(Character):
    def __init__(self):
        super().__init__()
        self.defense=0
        self.health=125
        self.special_name='war cry'
        self.name='Barbarian'

    def special(self, target):
        print('the Barbarian lets out a massive shout, striking harder but losing health in the process')
        print('')
        self.strength=self.strength*2
        self.attack(target)
        self.health-=10
        self.strength=self.strength/2
        return self