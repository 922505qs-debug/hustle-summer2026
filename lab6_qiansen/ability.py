import random

class Ability:
    def __init__(self, name, max_attack):
        self.name = name
        self.max_attack = max_attack

    def attack(self):
        return random.randint(0, self.max_attack)

if __name__ == "__main__":
    ability_1 = Ability ("Really Strong Punch", 30)
    print (ability_1.name)
    print (ability_1.max_attack)
    ability_1.attack()
