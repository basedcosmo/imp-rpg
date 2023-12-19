import time
import random
scholarspells = ["Magic Missile", "Fireball", "Firebolt", "Arcane Light", "Invisibility", "Lightning Bolt", "Chain Lightning", "Locate Object", "Lead to Gold", "Darkvision", "Enchant Weapon", "Haste", "Arcane Shield"]
priestspells = ["Holy Light", "Turn Undead", "Minor Healing", "Major Healing", "Bless", "Protection", "Smite Undead", "Prayer", "Magic Missile"]
naturalistspells = ["Create or Destroy Water", "Purify Food and Drink", "Speak to Animals", "Speak to Spirits or Ghosts", "Comprehend Language", "Animal Messenger", "Speak with Plants", "Animal Form", "Ignite Object"]

print("character generatorizer")
menu = True
racialbonus = "no racial bonus"
racialspecial = "You have no special racial abilities"
classspecial = "You have no special class abilities"
special = "You have no special abilities"
if menu:
    print("1: Begin Generatorizer")
    print("2: Infomation about the Generatorizer")
    print("3: 3d6 Rolling Machine")
    print("4: Spell List")
    print("5: Level Up Bonus Generatorizer")
    choice = input("Input Number Choice")
    if choice == "1":
        menu = False
        print("Warning! If you dont choose a listed class/race name, that voids the benifits of the class/race!")
        strength = random.randint(3,8)
        constitution = random.randint(3,8)
        dexterity = random.randint (3,8)
        intelligence = random.randint (3,8)
        name = input("What is your name?")
        cclass = input("What is your Character Class? (Warrior, Scholar, Priest, Thief, Adventurer, Sorcerer, Viking, Naturalist)")
        if cclass == "Warrior":
            strength + 1
        elif cclass == "Scholar":
            intelligence + 1
            classspecial = "You are a spellcaster."
        elif cclass == "Sorcerer":
            intelligence + 1
            classspecial = "You are a spellcaster"
        elif cclass == "Priest":
            intelligence + 1
            classspecial = "You are a spellcaster."
        elif cclass == "Naturalist":
            intelligence + 1
            classspecial = "You are a spellcaster."
        elif cclass == "Theif":
            dexterity + 1
        elif cclass == "Viking":
            strength + 1
            constitution + 1
            intelligence - 1
            classspecial = "You are unable to used ranged weapons."
        elif cclass == "Adventurer":
            constitution + 1
            classspecial = "You can detect traps from six feet away."
        race = input("What is your race? (Human, Half-Orc, Half-Elf, Elf, Dwarf, Gnome)")
        if race == "Human":
            pass
        elif race == "Half-Orc":
            racialbonus == "orcish strength"
            strength = strength + 2
        elif race == "Half-Elf":
            racialbonus == "half-elf intellect"
            intelligence + 2
        elif race == "Elf":
            racialbonus == "elvish dexterity"
            dexterity + 2
        elif race == "Dwarf":
            racialbonus == "dwarven darkvision"
            racialspecial = "You have Darkvision, 60 feet."
        elif race == "Gnome":
            racialbonus == "Can sense gems"
            racialspecial = "You can sense gems from 60 feet away."
        print("You are", name, "\033 You are a", race, "\033" " You are a", cclass, "\033", racialspecial, "\033", classspecial)
        print("Your full character name is:", name + " the", race, cclass)
        if cclass == "scholar":
            print("Your starting spells are:", random.choice(scholarspells) + ",", random.choice(scholarspells) + ",", random.choice(scholarspells))
        if cclass == "Priest":
            print("Your starting spells are:", random.choice(priestspells) + ",", random.choice(priestspells))
        if cclass == "Sorcerer":
            print("Your starting spells are:", random.choice(scholarspells) + ",", random.choice(scholarspells) + ",", random.choice(scholarspells) + ",", random.choice(scholarspells))
        if cclass == "Naturalist":
            print("Your starting spells are:", random.choice(naturalistspells) + ",",)
        print("strength:", strength)
        print("dexterity:", dexterity)
        print("intelligence:", intelligence)
        print("constitution:", constitution)
        hp = constitution
        ac = dexterity
        print("hp:", hp + 6)
        if ac > 12:
            ac = 11
        if ac < 4:
            ac = 3
        print("ac:", ac + 1)
        print("The system will not automatically restart it's self after this. Please restart it")

if choice == "2":
    menu = False
    print("Hello! The Generatorizer is a basic character generator system for any basic roleplaying game,")
    print("that automatically generates a ST, DX, IQ, and CO value, with an added HP and AC value.")
    print("This is open source, to an extent. You can edit and add various things to the code, but please")
    print("dont remove my hashtag notes. Thank you for using my system! nwphs-1 signing off.")
    menu = True
    
if choice == "3":
    menu = False
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    r3 = random.randint(1, 6)
    rfinal = r1 + r2 + r3
    print("Your roll is:", rfinal)
    menu = True

if choice == "4":
    menu = False
    print("Welcome to the spell codex")
    print("Please choose a spellcasting class")
    print("(priest, scholar, Sorcerer, Naturalist)")
    select = input("# ")
    if select == "Priest":
        print(priestspells)
    elif select == "Scholar":
        print(scholarspells)
    elif select == "Sorcerer":
        print(scholarspells)
    elif select == "Naturalist":
        print(naturalistspells)
levelup = ["+1 strength", "+1 dexterity", "+1 constitution", "+1 intelligence", "+6 mHP", "+1 AC", "+ New Spell (Reroll if you arent a spellcaster)"]
if choice == "5":
    menu = False
    print("I am now automatically generating a level up reward!")
    print("Loading...")
    time.sleep(3)
    print(" ")
    time.sleep(3)
    print("Loading...")
    time.sleep(3)
    print(" ")
    time.sleep(3)
    print("Your level bonus is: ", random.choice(levelup))
    
# severely needs work to make this work good and proper, although, it's currently not the worst system in the world.
if menu:
    print("1: Please restart the program to preform another action. Thank you!")
    
input("\nInput to kill the program.\n")    