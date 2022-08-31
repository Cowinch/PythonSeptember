from game_classes.character import Character

class Pokemon(Character):
    def __init__(self, type, hp) -> None:
        super().__init__()
        self.type=type
        self.health=hp

    def evolve(self):
        self.level+=1
        self.strength=self.strength+(self.strength*.05)
        self.defence=self.defence+(self.defence*.1)
        return self

    def print_info(self):
        super().print_info()
        print(self.type)