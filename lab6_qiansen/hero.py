import random
from ability import Ability
from armor import Armor
from weapons import Weapons
from team import Team

class Hero: 
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilites = []
        self.armors = []
        self.weapons = []

    def battle (self, opponent):
        my_list = [self.name, opponent.name]
        print (random.choice ([self.name, opponent.name]))

    def add_ability (self, ability):
        self.abilites.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilites:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        blocked = self.defend()
        damage_taken = max(damage - blocked, 0)
        self.current_health -= damage_taken
        if self.current_health < 0:
            self.current_health = 0
        return damage_taken
    
    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def attack_with_weapon(self):
        total_damage = 0
        for weapon in self.weapons:
            total_damage += weapon.attack()
        return total_damage

    

if __name__ == "__main__":
    my_hero = Hero ("hero1", 150)
   # print (my_hero.name)
   # print (my_hero.current_health)
   # my_opponent = Hero ("hero2", 200)
   # my_hero.battle(my_opponent)
   # my_hero.add_ability(Ability("Sleep", 30))
   # my_hero.add_ability(Ability("Punch", 20))
   # my_hero.attack()
  # my_hero.add_armor(Armor("tall hat", 10))
  # my_hero.add_armor(Armor("short hat", 5))
  # my_hero.take_damage(40)
   my_hero.add_weapon(Weapons("big sword", 20))
   my_hero.add_weapon(Weapons("small sword", 10))