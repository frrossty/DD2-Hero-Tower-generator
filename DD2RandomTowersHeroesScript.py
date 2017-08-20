#! python3

import random
import pprint

print("Please choose the minimum number of towers you wish to use, 1-4")
minTowers = int(input())
print("Please choose the maximum number of towers you wish to use, 1-4")
maxTowers = int(input())
print()
print("Please choose the minimum number of heroes you wish to use, 1-4")
minHeroes = int(input())
print("Please choose the maximum number of heroes you wish to use, 1-4")
maxHeroes = int(input())


#Libraries for the heroes
def Monk():
    global maxTowers
    global minTowers
    h1 = ["Monk....."]
    t1 = ["Flame Aura", "lightning Aura", "Skyguard Tower", "Boost Aura"]
    tower1 = random.sample(t1, random.randint(minTowers, maxTowers))
    return h1 + tower1 

def Huntress():
    global maxTowers
    global minTowers
    h2 = ["Huntress....."]
    t2 = ["Explosive Trap", "Geyser Trap", "Poison Dart Tower", "Blaze Balloon"]
    tower2 = random.sample(t2, random.randint(minTowers, maxTowers))
    return h2 + tower2

def Apprentice():
    global maxTowers
    global minTowers
    h3 = ["Apprentice....."]
    t3 = ["Flame Tower", "Frostbite Tower", "Arcane Barrier", "Earthshatter Tower"]
    tower3 = random.sample(t3, random.randint(minTowers, maxTowers))
    return h3 + tower3

def Squire():
    global maxTowers
    global minTowers
    h4 = ["Squire....."]
    t4 = ["Spike Blockade", "Cannonball Tower", "Ballista", "Training Dummy"]
    tower4 = random.sample(t4, random.randint(minTowers, maxTowers))
    return h4 + tower4

def AbyssalLord():
    global maxTowers
    global minTowers
    h5 = ["AbyssalLord....."]
    t5 = ["Orc Blockade", "Skeletal Ramster", "Bone Archers", "The colossus"]
    tower5 = random.sample(t5, random.randint(minTowers, maxTowers))
    return h5 + tower5

def Dryad():
    global maxTowers
    global minTowers
    h6 = ["Dryad....."]
    t6 = ["Moss Hornet's Nest", "Harpy's Perch", "Slime Pit", "Angry Nimbus"]
    tower6 = random.sample(t6, random.randint(minTowers, maxTowers))
    return h6 + tower6

def EV2():
    global maxTowers
    global minTowers
    h7 = ["EV2....."]
    t7 = ["Proton Beam", "Reflect Beam", "Buff Beam", "Weapon Manufacturer"]
    tower7 = random.sample(t7, random.randint(minTowers, maxTowers))
    return h7 + tower7

def Mystic():
    global maxTowers
    global minTowers
    h8 = ["Mystic....."]
    t8 = ["Snaking Sands", "Sand Viper", "Viper's Fangs", "Obelisk"]
    tower8 = random.sample(t8, random.randint(minTowers, maxTowers))
    return h8 + tower8

def Lavamancer():
    global maxTowers
    global minTowers
    h9 = ["Lavamancer....."]
    t9 = ["Fissure of Embermount", "Maw of the Earth Drake", "Oil Geyser", "Volcano"]
    tower9 = random.sample(t9, random.randint(minTowers, maxTowers))
    return h9 + tower9


#Loop to produce results
def main():
    global maxTowers
    global minTowers
    global maxHeroes
    global minHeroes
    myList = [Lavamancer(), Mystic(), Monk(), Huntress(), Apprentice(), Squire(), AbyssalLord(), Dryad(), EV2()]
    x = random.sample(myList, random.randint(minHeroes, maxHeroes))
    print()
    pprint.pprint(x)
    restart = input("To re-roll press 'Enter', or press 's' to change the stats")
    if restart == "":
        main()
    elif restart == "s":
        print("Please choose the minimum number of towers you wish to use")
        minTowers = int(input())
        print("Please choose the maximum number of towers you wish to use")
        maxTowers = int(input())
        print()
        print("Please choose the minimum number of heroes you wish to use")
        minHeroes = int(input())
        print("Please choose the maximum number of heroes you wish to use")
        maxHeroes = int(input())
        main()

if __name__ == "__main__":
    main()






