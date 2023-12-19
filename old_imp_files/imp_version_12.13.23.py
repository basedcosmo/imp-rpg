import random
print("character generatorizer")
menu = True
racialbonus = "no racial bonus"
racialspecial = "You have no special abilities"
classspecial = "You have no special abilities"
special = "You have no special abilities"
if menu:
    print("1: Begin Generatorizer")
    print("2: Infomation about the Generatorizer")
    print("3: 3d6 Rolling Machine")
    choice = input("Input Number Choice")
    
    if choice == "1":
        menu = False
        strength = random.randint(3,16)
        constitution = random.randint(3,16)
        dexterity = random.randint (3,16)
        intelligence = random.randint (3,16)
        name = input("What is your name?")
        cclass = input("What is your Character Class? (Fighter, Wizard, Cleric, Thief)")
        if cclass == "Fighter":
            strength + 1
        elif cclass == "Wizard":
            intelligence + 1
            classspecial = "You are a spellcaster."
        elif cclass == "Cleric":
            constitution + 1
            classspecial = "You are a spellcaster."
        elif cclass == "Theif":
            dexterity + 1
        race = input("What is your race? (Human, Half-Orc, Elf, Dwarf)")
        if race == "Human":
            racialbonus = "no racial bonuses"
        elif race == "Half-Orc":
            racialbonus == "orcish strength"
            strength = strength + 2
        elif race == "Elf":
            racialbonus == "elvish dexterity"
            dexterity = dexterity + 2
        elif race == "Dwarf":
            racialbonus == "dwarven darkvision"
            racialspecial = "You have Darkvision, 60 feet."
        print("You are", name, "- You are a", race, "-" " You are a", cclass, "-", racialspecial, "-", classspecial)
        print("strength:", strength)
        print("dexterity:", dexterity)
        print("intelligence:", intelligence)
        print("constitution:", constitution)
        hp = constitution
        ac = dexterity
        print("hp:", hp + 6)
        if ac > 16:
            ac = 15
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

# severely needs work to make this work good and proper, although, it's currently not the worst system in the world.
if menu:
    print("1: Please restart the program to preform another action. Thank you!")
    
    
