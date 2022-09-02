from classes.character import Character
import random

class Barbarian(Character):
    def __init__(self):
        super().__init__()
        self.defense=0
        self.health=135
        self.special_name='war cry'
        self.name='Barbarian'

    def special(self, target):
        print('the Barbarian lets out a massive shout, striking harder but losing health in the process')
        print('')
        self.strength=self.strength*3
        self.attack(target)
        self.health-=20
        self.strength=self.strength/3
        return self