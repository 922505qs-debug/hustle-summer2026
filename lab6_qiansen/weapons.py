import random

from ability import Ability

class Weapons(Ability):
    def attack(self):
        half_damage = self.max_attack // 2
        return random.randint(half_damage, self.max_attack)

if __name__ == "__main__":
    weapon_1 = Weapons ("Really Strong Sword", 30)
    print (weapon_1.name)
    print (weapon_1.max_attack)
    weapon_1.attack()