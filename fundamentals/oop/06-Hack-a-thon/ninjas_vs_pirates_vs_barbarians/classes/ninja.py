from classes.character import Character
import random

class Ninja(Character):
    def __init__(self):
        super().__init__()
        self.defense=53
        self.health=80
        self.strength=20
        self.special_name='Smoke bomb'
        self.name='Ninja'

    def special(self, target):
        print('Ninja used smoke bomb!! it does nothing becuase I ran out of time WHOOPS')
        print('')
        self.defense=self.defense*2
        return self