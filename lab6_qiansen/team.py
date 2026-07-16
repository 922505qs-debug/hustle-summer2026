import random

from hero import Hero


class Team:
    self.name = name
    self.heros = []

    def add_hero(self, hero):
        self.heros.append(hero)

    def remove_hero(self, name):
        for hero in self.heros:
            if hero.name == name:
                self.heros.remove(hero)
                return True
        return False
    
    def view_all_heroes(self):
        for hero in self.heros:
            print(hero.name)
        
    def team_kills(self):
        total_kills = 0
        for hero in self.heros:
            total_kills += hero.kills
        return total_kills
    
    def team_deaths(self):
        total_deaths = 0
        for hero in self.heros:
            total_deaths += hero.deaths
        return total_deaths

    def team_attack(self):
        total_damage = 0
        for hero in self.heros:
            total_damage += hero.attack()
        return total_damage

    def team_revive(self):
        for hero in self.heros:
            hero.current_health = hero.starting_health