import random

class Character:
    def __init__(self) -> None:
        self.health=100
        self.strength=10
        self.level=1
        self.defence=5
        self.recuperate=10

    def attack(self, target):
        print("attacking")
        target.defend(self.strength)
        return self

    def defend(self, damage):
        actual_damage=damage-self.defence
        self.health-=actual_damage
        return self
    
    def heal(self):
        self.health+=self.recuperate

    def print_info(self):
        print(f'health {self.health} strength {self.strength} level {self.level} defence {self.defence}')