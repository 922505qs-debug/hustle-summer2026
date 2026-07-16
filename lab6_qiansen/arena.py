from ability import Ability
from weapons import Weapons
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input("Enter ability name: ")
        max_damage = int(input("Enter max damage value: "))
        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("Enter weapon name: ")
        max_damage = int(input("Enter max damage value: "))
        return Weapons(name, max_damage)
        pass 

    def create_armor(self):
        name = input("Enter armor name: ")
        max_block = int(input("Enter max block value: "))
        return Armor(name, max_block)
        pass
    
    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero

    def build_team_one(self):
        team_name = input("Enter Team 1's name: ")
        self.team_one = Team(team_name)
        numOfTeamMembers = int(input(f"How many heroes for {team_name}? "))
        for _ in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)
    
    def build_team_two(self):
        team_name = input("Enter Team 2's name: ")
        self.team_two = Team(team_name)
        numOfTeamMembers = int(input(f"How many heroes for {team_name}? "))
        for _ in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)
        pass

    def team_battle(self):
        self.team_one.attack(self.team_two)
        self.team_two.attack(self.team_one)
        pass
    
    def show_stats(self):
         print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
         print(self.team_two.name + " statistics: ")
         self.team_two.stats()
        print("\n")
         team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
         if team_deaths == 0:
             team_deaths = 1
    print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)
                game_is_running = True 

arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()
    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")
        if play_again.lower() == "n":
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

