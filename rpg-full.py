"""
In this simple RPG game, the hero fights random enemies to gather gold
He can increase his strength at the merchant
TODO add final boss!

"""
from random import randint 
from characters import *


def mainmenu():
    print()
    print(f"You're a hero currently carrying {mhero.heldgold} gold.")
    print("What do you want to do?")
    print(f"1. Go fight a monster")
    print("2. Visit the merchant")
    print("3. Quit the game")
    print("> ",)   
    user_input = input()
    if user_input=="1":
        fight()
    if user_input=="2":
        merchant()
    if user_input=="3":
        exit()

def merchant():
    print()
    print(f"You're a hero currently carrying {mhero.heldgold} gold.")
    print("Welcome, what can I do for you?")
    print(f"1. 20gp: Buy a potion to increase your health")
    print("2. 20gp: Buy a potion to increase your strength")
    print("3. Leave the shop")
    print("> ",) 
    user_input = input()
    if user_input=="1":
        if mhero.heldgold >=20:
            print("You buy and chug a health potion! You feel healthier")
            mhero.health+=15
            mhero.gold-=20
        else:
            print("You don't have enough money!")
    if user_input=="2":
        if mhero.heldgold >=20:
            print("You buy and chug a strength potion! You feel stronger")
            mhero.power+=4
            mhero.gold-=20
        else:
            print("You don't have enough money!")


def fight():
    #Spawns a random enemy
    spawn = randint(1,10) 
    print(spawn)
    if spawn in range(1,5):
        enemy = Goblin()
    elif spawn in range(5,7):
        enemy = Thief()
    elif spawn in range(7,9):
        enemy = Shadow()
    elif spawn == 9:
        enemy = Wizard()
    else:
        enemy = Zombie()
    #Starts a battle
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
            # Hero attacks enemy
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
            # Enemy attacks hero
            enemy.attack(mhero)
            if mhero.alive(enemy) != True:
                print("You are dead.")
                exit()



def main():
    while True:
        mainmenu()



mhero = Hero()
main()
