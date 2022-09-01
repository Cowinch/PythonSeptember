import random
class Character:

    def __init__( self):
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.defense=5

    def show_stats( self ):
        print(f"Strength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nDefense: {self.defense}")
        print('')

    def attack( self , target ):
        print("attacking now!")
        print('')
        target.defend(self.strength)
        return self

    def defend(self, damage):
        actual_damage=random.randint(damage/2,damage)-self.defense
        self.health-=actual_damage
        return self

    def healing(self):
        print("recuperating")
        print('')
        self.health=(self.health*.05)+self.health+5

