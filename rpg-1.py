"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Character:
    def __init__(self):
        self.health = 0
        self.power = 0
        self.name = ""
    def __str__(self):
        return self.name
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"{self.name} does {self.power} to {enemy.name}")
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def print_status(self):
        print(f"{self.name} Health: {self.health} Power:{self.power}")

class Hero(Character):
    def __init__(self):
        self.health = 10
        self.power = 5
        self.name = "Hero"
class Goblin(Character):
    def __init__(self):
        self.health = 6
        self.power = 2
        self.name = "Goblin"
class Zombie(Character):
    def __init__(self):
        self.health = 9999
        self.power = 3
        self.name = "Zombie"
    def print_status(self):
        print("You cannot kill the zombie!!")
        self.health = 9999



def main():
    mhero = Hero()
    enemy = Zombie()


    while enemy.alive() & mhero.alive():
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
            if enemy.alive() != True:
                print(f"The {enemy} is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if enemy.alive():
            # Goblin attacks hero
            enemy.attack(mhero)
            if mhero.alive() != True:
                print("You are dead.")

main()
