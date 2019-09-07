"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
from random import randint 

class Character:
    def __init__(self):
        self.health = 0
        self.power = 0
        self.name = ""
        self.heldgold = 0
    def __str__(self):
        return self.name
    def attack(self, enemy):
        print(f"{self.name} does {self.power} to {enemy.name}")
        enemy.takedmg(self.power)
    def takedmg(self, amount):
        self.health -= amount
    def alive(self, enemy):
        if self.health > 0:
            return True
        else:
            print(f"{self.name} dropped {self.heldgold} gold!")
            enemy.heldgold+=self.heldgold
            return False
    def print_status(self):
        print(f"{self.name} Health: {self.health} Power:{self.power}")

class Hero(Character):
    def __init__(self):
        self.health = 10
        self.power = 5
        self.name = "Hero"
        self.heldgold = 1
    def attack(self, enemy):
        if randint(1,5) == 5:
            enemy.health -= self.power*2
            print(f"CRITICAL HIT!!!! {self.name} does {self.power} to {enemy.name}")
        else:    
            enemy.health -= self.power
            print(f"{self.name} does {self.power} to {enemy.name}")

class Medic(Character):
    def __init__(self):
        self.health = 12
        self.power = 4
        self.name = "Medic"
        self.heldgold = 1
    def takedmg(self, amount):
        self.health-=amount
        if(self.health<11 & randint(1,5) == 5):
            self.health+=2
            print(f"{self.name} regained 2 health!")

class Shadow(Character):
    def __init__(self):
        self.health = 1
        self.power = 5
        self.name = "Shadow"
        self.heldgold = 1
    def takedmg(self,amount):
        if randint(1,10)==10:
            self.health-=amount
        else:
            print("Shadow dodged the attack!")
            

class Goblin(Character):
    def __init__(self):
        self.health = 6
        self.power = 2
        self.name = "Goblin"
        self.heldgold = 5

class Zombie(Character):
    def __init__(self):
        self.health = 3
        self.power = 3
        self.name = "Zombie"
        self.heldgold = 100
    def alive(self, enemy):
        return True
class Wizard(Character):
    def __init__(self):
        self.health = 8
        self.power = 4
        self.name = "Wizard"
        self.heldgold = 9
        self.extralife = True
    def alive(self, enemy):
        if self.health > 0:
            return True
        elif self.extralife:
            print("The wizard springs back to life!")
            self.health = 6
            self.extralife = False
            return True
        else:
            print(f"{self.name} dropped {self.heldgold} gold!")
            enemy.heldgold+=self.heldgold
            return False

class Thief(Character):
    def __init__(self):
        self.health = 8
        self.power = 2
        self.name = "Thief"
        self.heldgold = 2
    def attack(self, enemy):
        print(f"{self.name} does {self.power} to {enemy.name}")
        enemy.takedmg(self.power)
        if(enemy.gold>1):
            print("Thief stole some gold!")
            enemy.heldgold-=2
            self.heldgold+=2




def main():
    mhero = Hero()
    enemy = Zombie()


    while enemy.alive(mhero) & mhero.alive(enemy):
        mhero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {enemy}")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            mhero.attack(enemy)
            if enemy.alive(mhero) != True:
                print(f"The {enemy} is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if enemy.alive(mhero):
            # Goblin attacks hero
            enemy.attack(mhero)
            if mhero.alive(enemy) != True:
                print("You are dead.")

main()
