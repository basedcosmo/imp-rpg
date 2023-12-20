import time
import random
import os
#You can take the code, and share it as long as you ask before you do and dont promote it as your own code, and dont say you created it either. Contact me at basedcosmo on discord.
wizardspells = ["Magic Missile", "Fireball", "Firebolt", "Arcane Light", "Invisibility", "Lightning Bolt", "Chain Lightning", "Locate Object", "Lead to Gold", "Darkvision", "Enchant Weapon", "Haste", "Arcane Shield", "Identify", "Dispell Curse"]
sorcererspells =  ["Magic Missile", "Fireball", "Firebolt", "Arcane Light", "Invisibility", "Lightning Bolt", "Chain Lightning", "Locate Object", "Darkvision", "Enchant Weapon", "Haste", "Arcane Shield", "Ignite Weapon", "Cure Drunkard"]
clericspells = ["Holy Light", "Turn Undead", "Minor Healing", "Major Healing", "Prayer of Mass Healing", "Cure Wounds", "Cure Sickness", "Bless Person", "Protection", "Prayer", "Magic Missile"]
paladinspells = ["Holy Light", "Turn Undead", "Minor Healing", "Major Healing", "Bless Person", "Protection", "Thunderous Smite", "Holy Smite", "Searing Smite", "Insightful Question", "Dispell Curse"]
spellscrolls = ["Magic Missile", "Fireball", "Firebolt", "Arcane Light", "Invisibility", "Lightning Bolt", "Chain Lightning", "Locate Object", "Lead to Gold", "Darkvision", "Enchant Weapon", "Haste", "Arcane Shield", "Holy Light", "Turn Undead", "Minor Healing", "Major Healing", "Bless Person", "Protection", "Smite Undead", "Prayer", "Magic Missile", "Identify", "Dispell Curse", "Speak to Animals"]
weapon = ["Shortsword", "Longsword", "Greatsword", "Club", "Mace", "Maul", "Druidic Staff", "Spellbook", "Shortbow", "Longbow", "Crossbow", "Dagger", "Rapier", "Lute", "Drum and Drumsticks", "Gauntlets", "Crystal Ball", "Hatchet", "Waraxe", "Danish Axe"]
items = "Nothing"
item = ["Torch", "Glasses", "Mirror", "Holy Water", "Holy Symbol", "Beartrap", "Thief's Tools", "Map", "Compass", "Lead Fishing Weight", "Pint of Ale", "Glass of Wine", "Horn of Mead", "Lead Boots", "Raincoat", "Light Cloak", "Fake Amulet of Yendor"]
armor = ["Clothing", "Gambeson", "Leather Armor", "Plate Armor", "Magical Robes", "Dark Wraps", "Chainmail", "Wooden Shield", "Copper Shield", "Iron Shield"]
blesscurse = ["-3 Cursed", "-2 Cursed", "-1 Cursed", "Uncursed", "Uncursed", "Uncursed", "Uncursed", "Uncursed", "+1 Blessed", "+2 Blessed", "+3 Blessed", "+4 Blessed"]
ttype = ["Golden", "Silver", "Bronze", "Iron", "Copper"]
treasure = ["Chalice", "Mug", "Necklace", "Monacle", "Bowl", "Urn", "Bar", "Medallion"]
jewels = ["Necklace", "Ring", "Cape", "Helmet", "Gloves", "Toering", "Belt"]
jtype = ["Intellect", "Vigor", "Vitality", "Speed", "Darkvision", "Binding", "Blinding", "Slowness", "Light", "Springing", "Reading", "Purification", "Chastity", "Disintegration"]
enemy = ["Orcs", "Goblins", "Skeletons", "Zombies", "Mummies", "Slimes", "Giant Bats", "Wolves", "Greedy Gnomes", "Cultists", "Demons", "Kobolds", "Bears", "Trogbears", "Centaurs", "Ogres", "Knights", "Minotaurs", "Ettins", "Incubi", "Succubi", "Trolls", "Golems", "Vampires", "Grey Dragons", "Blue Dragons", "Silver Dragons"]
Wtype = ["Sword", "Axe", "Maul", "Bow", "Staff"]
Weffect = ["Mjolnir, Hammer of Lighting", "Sumarbrander, Sword of Summer", "Gungnir, Spear of The All-Father", "Hrunting, the Blood Tempered Blade", "Sharur, the Smasher of Thousands", "Dyrnwyn, Blade of Fire", "Excalibur, the Holy Blade", "Gram, Blade of the Dragon Slayer", "Sting, the Orc Slayer", "Skofnung, King's Blade", "Cinder, the Scalding Halberd", "Throthnur, the Elven Bow of Truth", "Fulgor, Lightning of the North", "Aegis, the Speaking Shield", "Nipalan, the Pushing Arrow", "Mustaine, Mettalic Aerodynamic shirt", "Billiam, Stanley's Bottomless Bucket"]
print("character generatorizer")
name = "None"
race = "None"
cclass = "None"
strength = 0
dexterity = 0
intelligence = 0
constitution = 0
hp = 0
mana = 0
ac = 0

fart = [
    name,
    race,
    cclass,
    strength,
    dexterity,
    intelligence,
    constitution,
    hp,
    mana,
    ac
]
menu = True
doom = False
alicar = False
deslicar = False
racialbonus = "no racial bonus"
racialspecial = "You have no special racial abilities"
classspecial = "You have no special class abilities"
special = "You have no special abilities"
cursegen1 = random.randint(1, 3)
cursegen2 = random.randint(1, 3)
cursegen3 = random.randint(1, 3)
randloot = random.randint(1, 3)
if menu:
    print("System made by Cosmo and amarvin")
    print(" ")
    print("1: Begin Generatorizer")
    print("2: Infomation about the Generatorizer")
    print("3: Random Unique Item Generator")
    print("4: Spell List")
    print("5: Level Up Bonus Generatorizer")
    print("6: Random Loot Generator")
    print("7: Room Generator")
    print("8: Enemy Codex")
    print("9: Shop Generator")
    print("10: Dungeon Navagator")
    choice = input("Input Number Choice: ")
    if choice == "1":
        menu = False
        print("Warning! If you dont choose a listed class/race name, that voids the benifits of the class/race!  ")
        strength = random.randint(3, 8)
        constitution = random.randint(3, 10)
        dexterity = random.randint (3, 8)
        intelligence = random.randint (3, 8)
        name = input("What is your name?")
        cclass = input("What is your Character Class? (Fighter, Wizard, Cleric, Thief, Adventurer, Sorcerer, Hunter, Paladin)  ")
        if cclass == "Fighter":
            strength + 2
        elif cclass == "Wizard":
            intelligence + 2
            classspecial = "You are a spellcaster."
        elif cclass == "Sorcerer":
            intelligence + 1
            classspecial = "You are a spellcaster"
        elif cclass == "Cleric":
            intelligence + 1
            classspecial = "You are a spellcaster."
        elif cclass == "Thief":
            dexterity + 2
        elif cclass == "Adventurer":
            constitution + 1
            classspecial = "You start with random items, and loot."
            items = (random.choice(weapon), random.choice(armor), "Scroll of " + random.choice(spellscrolls))
        elif cclass == "Paladin":
            strength + 1
            constitution + 1
            classspecial = "You are a spellcaster."
        elif cclass == "Hunter":
            dexterity + 1
            constitution + 1
        if cclass == "Thief":
            race = input("What is your race? (Human, Half-Orc, Half-Elf, Elf, Dwarf, Gnome, Hobbit)  ")
        if cclass == "Adventurer":
            race = input("What is your race? (Human, Half-Orc, Half-Elf, Elf, Dwarf, Gnome, Hobbit)  ")
        if cclass == "Fighter":
            race = input("What is your race? (Human, Half-Orc, Half-Elf, Elf, Dwarf, Gnome)  ")
        if cclass == "Wizard":
            race = input("What is your race? (Human, Half-Orc, Half-Elf, Elf, Dwarf, Gnome)  ")
        if cclass == "Cleric":
            race = input("What is your race? (Human, Half-Orc, Half-Elf, Elf, Dwarf, Gnome)  ")
        if cclass == "Sorcerer":
            race = input("What is your race? (Human, Half-Orc, Half-Elf, Elf, Dwarf, Gnome)  ")
        if cclass == "Hunter":
            race = input("What is your race? (Half-Orc, Half-Elf, Elf)  ")
        if cclass == "Paladin":
            race = input("What is your race? (Human, Dwarf)  ")
        if race == "Human":
            racialbonus = "no racial bonus"
        elif race == "Half-Orc":
            racialbonus == "orcish strength"
            strength = strength + 2
        elif race == "Elf":
            racialbonus == "elvish dexterity"
            dexterity = dexterity + 1
        elif race == "Half-Elf":
            racialbonus == "druidic instincts"
            racialspecial == "gain the spell 'Speak to Animals'"

        elif race == "Dwarf":
            racialbonus == "dwarven darkvision"
            racialspecial = "You have Darkvision, 60 feet."
        elif race == "Gnome":
            racialbonus == "can sense gems"
            racialspecial = "You can sense gems from 60 feet away."
        elif race == "Hobbit":
            dexterity + 2
            racialbonus = "hobbit dexterity"
            racialspecial = "Hobbits are locked to Thieves and Adventurers, if you arent a thief or adventurer, you must make a new character."

        os.system('cls')
        print("You are", name, "× You are a", race, "×" " You are a", cclass, "×", racialspecial, "×", classspecial)
        print("Your full character name is:", name + " the", race, cclass)
        if cclass == "Wizard":
            print("Your starting spells are:", random.choice(wizardspells) + ",", random.choice(wizardspells) + ",", random.choice(wizardspells))
        if cclass == "Cleric":
            print("Your starting spells are:", random.choice(clericspells) + ",", random.choice(clericspells))
        if cclass == "Sorcerer":
            print("Your starting spells are:", random.choice(wizardspells) + ",", random.choice(wizardspells) + ",", random.choice(wizardspells) + ",", random.choice(wizardspells))
        if cclass == "Paladin":
            print("Your starting spells are:", random.choice(paladinspells) + ",", random.choice(paladinspells) + ",", random.choice(paladinspells))
        if race == "Half-Elf":
            print("You have an additional race inherant spell: Speak to Animals")
        if cclass == "Fighter":
            print("Your starting items are: Blessed +1 Longsword, Uncursed Wooden Shield, Uncursed Warrior's Tunic, Uncursed Potion of Healing")
        if cclass == "Wizard":
            print("Your starting items are: Uncursed Staff, Uncursed Spellbook, Uncursed Magic Robes, Uncursed Potion of Mana Rejuvination, Blessed +1 Ring of Magic Resistance")
        if cclass == "Cleric":
            print("Your starting items are: Uncursed Mace, Uncursed Spellbook, Uncursed Magic Robes, Blessed +2 Holy Symbol")
        if cclass == "Thief":
            print("Your starting items are: Uncursed Dagger, Uncursed Thieves Guild Attire, Uncursed Thief's Tools")
        if cclass == "Sorcerer":
            print("Your starting items are: Uncursed Shortsword, Uncursed Crystal Ball, Uncursed Magic Robes")
        if cclass == "Adventurer":
            print("Your starting items are: Uncursed Potion of Healing,", "Blessed +1 " + random.choice(weapon) + ",", "Blessed +1 " + random.choice(armor))
        if cclass == "Hunter":
            print("Your starting items are: Uncursed Crossbow, 20 Uncursed Bolts, Uncursed Beartrap, Uncursed Potion of Haste")
        if cclass == "Paladin":
            print("Your starting items are: Blessed +1 Longsword, Uncursed Plate Armor, Uncursed Spellbook")
        print("strength:", strength)
        print("dexterity:", dexterity)
        print("intelligence:", intelligence)
        print("constitution:", constitution)
        hp = constitution
        mana = intelligence
        ac = dexterity
        print("hp:", hp + 6, "/", hp + 6)
        if mana >= 9:
            mana = 8
        print("mana:", mana, "/", mana)
        if ac > 16:
            ac = 15
        if ac <= 4:
            ac = 4
        print("ac:", ac + 1)

if choice == "2":
    menu = False
    print("Hello! The Generatorizer is a basic character generator system for any basic roleplaying game,")
    print("that automatically generates a ST, DX, IQ, and CO value, with an added HP and AC value.")
    print("This is open source, to an extent. You can edit and add various things to the code, but please")
    print("dont remove my hashtag notes. Thank you for using my system! nwphs-1 signing off.")
    menu = True
    
if choice == "3":
    print("Below, is a Unique, Mythical Weapon.")
    print(random.choice(Weffect))

if choice == "4":
    menu = False
    print("Welcome to the spell codex")
    print("Please choose a spellcasting class")
    print("(Cleric, Paladin, Wizard, Sorcerer, Half-Elf, All)")
    select = input("# ")
    if select == "Cleric":
        print(clericspells)
    if select == "Paladin":
        print(paladinspells)
    elif select == "Wizard":
        print(wizardspells)
    elif select == "Sorcerer":
        print(sorcererspells)
    elif select == "Half-Elf":
        print("['Speak to Animals']")
    elif select == "All":
        print(spellscrolls)

    menu = True

levelup = ["+1 strength", "+1 dexterity", "+1 constitution", "+1 intelligence", "+6 mHP", "Learn a random spell"]
if choice == "5":
    menu = False
    print("I am now automatically generating a level up reward!")
    print("Drum roll please...")
    time.sleep(2)
    print("Your level bonus is: ", random.choice(levelup))

if choice == "6":
    print("Please choose a item type to generate (Jewel, Item, Weapon, Armor, Treasure, Scroll, Wand, All)")
    fart = input("Input: ")
    if fart == "Jewel":
        print(random.choice(blesscurse), random.choice(jewels), "of", random.choice(jtype))
        print(random.choice(blesscurse), random.choice(jewels), "of", random.choice(jtype))
        print(random.choice(blesscurse), random.choice(jewels), "of", random.choice(jtype))
    if fart == "Item":
        print(random.choice(blesscurse), random.choice(item))
        print(random.choice(blesscurse), random.choice(item))
        print(random.choice(blesscurse), random.choice(item))
    if fart == "Weapon":
        print(random.choice(blesscurse), random.choice(weapon))
        print(random.choice(blesscurse), random.choice(weapon))
        print(random.choice(blesscurse), random.choice(weapon))
    if fart == "Armor":
        print(random.choice(blesscurse), random.choice(armor))
        print(random.choice(blesscurse), random.choice(armor))
        print(random.choice(blesscurse), random.choice(armor))
    if fart == "Treasure":
        print(random.choice(blesscurse), random.choice(ttype), random.choice(treasure), "worth", random.randint(1,700), "¤")
        print(random.choice(blesscurse), random.choice(ttype), random.choice(treasure), "worth", random.randint(1,700), "¤")
        print(random.choice(blesscurse), random.choice(ttype), random.choice(treasure), "worth", random.randint(1,700), "¤")
    if fart == "Scroll":
        print(random.choice(blesscurse), "Scroll of", random.choice(spellscrolls))
        print(random.choice(blesscurse), "Scroll of", random.choice(spellscrolls))
        print(random.choice(blesscurse), "Scroll of", random.choice(spellscrolls))
    if fart == "Wand":
        print(random.choice(blesscurse), "Wand of", random.choice(spellscrolls))
        print(random.choice(blesscurse), "Wand of", random.choice(spellscrolls))
        print(random.choice(blesscurse), "Wand of", random.choice(spellscrolls))
    if fart == "All":
        print(random.choice(blesscurse), random.choice(jewels), "of", random.choice(jtype))
        print(random.choice(blesscurse), random.choice(item))
        print(random.choice(blesscurse), random.choice(weapon))
        print(random.choice(blesscurse), random.choice(armor))
        print(random.choice(blesscurse), random.choice(ttype), random.choice(treasure), "worth", random.randint(1,300), "¤")
        print(random.choice(blesscurse), "Scroll of", random.choice(spellscrolls))
        print(random.choice(blesscurse), "Wand of", random.choice(spellscrolls))

shopyn = ["Is", "Isn't", "Isn't", "Isn't", "Isn't", "Isn't"]
traps = ["a Pitfall Trap", "a Spike Trap", "a Mimic", "a Fake Door", "an Exploding Chest", "a Firebreathing Chest", "a Boulder Trap at the Door", "a Boulder Trap above a Chest", "no Traps", "no Traps", "no Traps", "no Traps"]
if choice == "7":
    print("\nWarning this section of code is outdated\n")
    floor = input("What floor are you on?  ")
    print("Now generating a room...")
    door = random.randint(1,3)
    print("\n \n \nYou are on floor", floor)
    print(random.randint(2,8), "units by", random.randint(2,8), "units")
    print("There are", random.randint(2,4), random.choice(enemy), "in the room.")
    print("With", door, "door(s) in the room.")
    print("This room, loot wise, has", random.randint(2,6), "items in it. (Roll on all table, said times, and roll 1d6 to pick a loot)")
    print("This room has", random.choice(traps))
    print("If floor is greater than 3")
    print("     There", random.choice(shopyn), "a shop in this room.")
    print("     There is also are two", random.choice(enemy), "in this room")
# severely needs work to make this work good and proper, although, it's currently not the worst system in the world.
shit = False    
if choice == "8":
    shit = True
while shit:
    os.system('cls')
    print("Please choose a monster from this list:")
    print(enemy)
    print(' ')
    EIM = input("Please input your choice here (Cap. Sensitive):   ")
    if EIM == "Orcs":
        print("Name: Orc")
        print("Items: Longsword, Gambeson,", random.randint(1,40), "¤")
        print("str: 8")
        print("dex: 5")
        print("int: 4")
        print("con: 9")
        print("hp: 15/15")
        print("mana: 4/4")
        print("ac: 6")
        print("dmg: 1d6")
        print("notes: orcs will petrify in natural or holy light.")
    if EIM == "Goblins":
        print("Name: Goblin")
        print("Items: Shortsword, Dark Wraps,", random.randint(1,40), "¤")
        print("str: 5")
        print("dex: 8")
        print("int: 4")
        print("con: 5")
        print("hp: 11/11")
        print("mana: 4/4")
        print("ac: 9")
        print("dmg: 1d6")
        print("notes: goblins can be payed to leave players alone by means of gold coins (¤) or treasure, which is based off of this equasion ((int - 12) x 10)")
    if EIM == "Skeletons":
        print("Name: Skeleton")
        print("Items: Shortsword, Tattered Leather,", random.randint(1,40), "¤")
        print("str: 4")
        print("dex: 4")
        print("int: 4")
        print("con: 3")
        print("hp: 9/9")
        print("mana: 4/4")
        print("ac: 5")
        print("dmg: 1d6")
        print("notes: skeletons take 2x blunt damage. skeletons are immune to fire damage.")
    if EIM == "Zombies":
        print("Name: Zombie")
        print("Items:", random.choice(blesscurse), random.choice(item), random.randint(1,40), "¤")
        print("str: 6")
        print("dex: 3")
        print("int: 1")
        print("con: 5")
        print("hp: 11/11")
        print("mana: 1/1")
        print("ac: 3")
        print("dmg: 1d6")
        print("notes: players must make a con save or be zombified in 1d6 hours.")
    if EIM == "Mummies":
        print("Name: Mummy")
        print("Items: Golden Dagger, Mummy Wraps,")
        print("str: 7")
        print("dex: 2")
        print("int: 1")
        print("con: 6")
        print("hp: 12/12")
        print("mana: 2/2")
        print("ac: 3")
        print("dmg: 1d6")
        print("notes: mummies take x2 fire damage")
    if EIM == "Greedy Gnomes":
        print("Name: Greedy Gnome (Dungeon Gnome)")
        print("Items: Maul, Gambeson,", random.randint(1,40), "¤")
        print("str: 6")
        print("dex: 6")
        print("int: 7")
        print("con: 8")
        print("hp: 14/14")
        print("mana: 8/8")
        print("ac: 7")
        print("dmg: 1d6")
        print("notes: gnomes in the dungeon turn into greedy gnomes when they see gold. they will attempt to mug you.")
    if EIM == "Slimes":
        print("Name: Dungeon Slime")
        print("Items: None")
        print("str: 4")
        print("dex: 4")
        print("int: 4")
        print("con: 10")
        print("hp: 16/16")
        print("mana: 0/0")
        print("ac: 5")
        print("dmg: 1d6")
        print("notes: the slime is instantly killed when in contact with fire. if fire wasnt used to kill them, the party can obtain their flamable slime")
    if EIM == "Giant Bats":
        print("Name: Giant Bat")
        print("Items: None")
        print("str: 4")
        print("dex: 4")
        print("int: 4")
        print("con: 4")
        print("hp: 10/10")
        print("mana: 0/0")
        print("ac: 5")
        print("dmg: 1d6")
        print("notes: giant bats have a +2 ac when evading ranged attacks, due to their nimble flying techniques")
    if EIM == "Wolves":
        print("Name: Wolf")
        print("Items: None")
        print("str: 9")
        print("dex: 7")
        print("int: 3")
        print("con: 9")
        print("hp: 15/15")
        print("mana: 3/3")
        print("ac: 8")
        print("dmg: 1d6")
        print("notes: wolves have a crushing bite, players must make a con check to not have a bone broken when they attack.")
    if EIM == "Cultists":
        print("Name: Demon Cultist")
        print("Items: Dagger, Magic Robes,", random.randint(1,40), "¤")
        print("Spells: Invisibility, Curse Object")
        print("str: 4")
        print("dex: 6")
        print("int: 8")
        print("con: 5")
        print("hp: 11/11")
        print("mana: 8/8")
        print("ac: 7")
        print("dmg: 1d6")
        print("notes: cultists are weak to any attacks by a holy entity.")
    if EIM == "Demons":
        print("Name: Demon")
        print("Items: Demonic Whip, Uncursed", random.choice(treasure))
        print("str: 8")
        print("dex: 6")
        print("int: 6")
        print("con: 9")
        print("hp: 15/15")
        print("mana: 6/6")
        print("ac: 7")
        print("dmg: 2d6")
        print("notes: demons are weak to any attacks by a holy entity.")
    if EIM == "Kobolds":
        print("Name: Kobold")
        print("Items: Shortsword, Chainmail, Wooden Shield", random.randint(10,15), "¤")
        print("str: 5")
        print("dex: 5")
        print("int: 5")
        print("con: 5")
        print("hp: 11/11")
        print("mana: 5/5")
        print("ac: 6")
        print("dmg: 1d6")
        print("notes: kobolds have a chance (1d6, when 6), to be friendly in a room, willing to trade with the party.")
    if EIM == "Bear":
        print("Name: Cave Bear")
        print("Items: None")
        print("str: 10")
        print("dex: 6")
        print("int: 3")
        print("con: 11")
        print("hp: 17/17")
        print("mana: 0/0")
        print("ac: 6")
        print("dmg: 2d6")
        print("notes: bears have a crushing bite, players must make a con-2 check to not have a bone broken when they attack.")
    if EIM == "Trogbears":
        print("Name: Trogbear")
        print("Items: Large Maul, Large Dark Wraps,", random.randint(30,100), "¤")
        print("str: 10")
        print("dex: 8")
        print("int: 2")
        print("con: 9")
        print("hp: 23/23")
        print("mana: 0/0")
        print("dmg: 3d6")
        print("ac: 9")
        print("notes: trogbears are resistant to blade damage.")
    if EIM == "Ogre":
        print("Name: Ogre")
        print("Items: Large Club, Large Loincloth,", random.randint(8,83), "¤")
        print("str: 11")
        print("dex: 3")
        print("int: 1")
        print("con: 10")
        print("hp: 41/41")
        print("mana: 0/0")
        print("ac: 4")
        print("dmg: 3d6")
        print("notes: ogres deal 1d6 less damage to small creatures (goblins, hobbits, dwarves, gnomes, etc).")
    if EIM == "Knights":
        print("Name: Knights")
        print("Items: Longsword, Regal Plate Armor,", random.randint(100,500), "¤")
        print("str: 8")
        print("dex: 6")
        print("int: 6")
        print("con: 6")
        print("hp: 28/28")
        print("mana: 6/6")
        print("ac: 7")
        print("dmg: 2d6")
        print("notes: knights will only attack evil creatures on sight (half-orcs, orcs, goblins, demons, etc).")
    if EIM == "Centuar":
        print("Name: Centuar")
        print("Items: Large Greatsword")
        print("str: 7")
        print("dex: 9")
        print("int: 6")
        print("con: 6")
        print("hp: 13/13")
        print("mana: 0/0")
        print("ac: 9")
        print("dmg: 2d6")
        print("notes: centuars have a dex+2 on all dex saving throws.")
    if EIM == "Ettins":
        print("Name: Ettins")
        print("Items: Large Club, Tattered Clothing")
        print("str: 11")
        print("dex: 4")
        print("int: 4")
        print("con: 11")
        print("hp: 15/15")
        print("mana: 0/0")
        print("ac: 5")
        print("dmg: 3d6")
        print("notes: ettins make every int check twice, taking the higher roll.")
    if EIM == "Incubi":
        print("Name: Incubus")
        print("Items: Shortsword")
        print("Spells: Firebolt, Lure")
        print("str: 7")
        print("dex: 7")
        print("int: 11")
        print("con: 7")
        print("hp: 13/13")
        print("mana: 12/12")
        print("ac: 6")
        print("dmg: 1d6")
        print("notes: incubi will lure female characters towards them (int save). non-binary characters and male characters are immune to this")
    if EIM == "Succubi":
        print("Name: Succubus")
        print("Items: Shortsword")
        print("Spells: Firebolt, Lure")
        print("str: 7")
        print("dex: 7")
        print("int: 11")
        print("con: 7")
        print("hp: 13/13")
        print("mana: 12/12")
        print("ac: 6")
        print("dmg: 1d6")
        print("notes: succubi will lure male characters towards them (int save). non-binary characters and female characters are immune to this")
    if EIM == "Trolls":
        print("Name: Troll")
        print("Items: Large Club, Large Tattered Clothes")
        print("str: 11")
        print("dex: 3")
        print("int: 3")
        print("con: 11")
        print("hp: 36/36")
        print("mana: 4/4")
        print("ac: 6")
        print("dmg: 3d6")
        print("notes: trolls will petrify in natural or holy light.")
    if EIM == "Golems":
        print("Name: Golem")
        print("Items: Ruby Eye Sensor (2)")
        print("str: 11")
        print("dex: 3")
        print("int: 3")
        print("con: 11")
        print("hp: 36/36")
        print("mana: 0/0")
        print("ac: 6")
        print("dmg: 3d6")
        print("notes: golems only take damage from bludgeoning attacks.")
    if EIM == "Vampires":
        print("Name: Vampire")
        print("Items: Shortsword, Regal Gambeson,", random.randint(100,500), "¤")
        print("str: 8")
        print("dex: 6")
        print("int: 6")
        print("con: 9")
        print("hp: 34/34")
        print("mana: 8/8")
        print("ac: 7")
        print("dmg: 3d6")
        print("notes: vampires will heal the same amount of all damage they deal.")
    if EIM == "Silver Dragons":
        print("Name: Silver Dragon")
        print("Items: None")
        print("str: 11")
        print("dex: 9")
        print("int: 11")
        print("con: 11")
        print("hp: 75/75")
        print("mana: 4/4")
        print("ac: 9")
        print("dmg: 4d6")
        print("notes: silver dragons are blind, but can sense the presence of gold. they also breathe fire, and deal an extra 1d6 fire damage")
    if EIM == "Blue Dragons":
        print("Name: Blue Dragon")
        print("Items: None")
        print("str: 11")
        print("dex: 9")
        print("int: 11")
        print("con: 11")
        print("hp: 55/55")
        print("mana: 4/4")
        print("ac: 9")
        print("dmg: 3d6")
        print("notes: blue dragons are smaller, but are impervious to frost damage. they also breathe freezing air, and deal an extra 1d6 frost damage")
    if EIM == "Grey Dragons":
        print("Name: Grey Dragon")
        print("Items: None")
        print("str: 11")
        print("dex: 9")
        print("int: 11")
        print("con: 11")
        print("hp: 121/121")
        print("mana: 4/4")
        print("ac: 9")
        print("dmg: 5d6")
        print("notes: grey dragons are very large and very dangerous. they breathe a petrification liquid, that petrifies living things. grey dragons are very weak to fire damage, and take an extra x3 fire damage.")
    shitfart = input("Input exit to quit, anything else to restart the codex")
    if shitfart == "exit":
        quit()
    if shitfart == "Exit":
        quit()

if choice == "10":
    print("Are you wanting to view the Dungeons of Deslicar, Dungeons of Doom, Ruins of Alicar (Deslicar, Alicar, Doom)")
    selection = input("# ")
    if selection == "Deslicar":
        deslicar = True
    if selection == "Alicar":
        alicar = True
    if selection == "Doom":
        doom = True

while deslicar:
    print("please input coordinates of the map in the dungeon (format is x,y,z, e.g. first room is 0,0,-1)")

    g = input("coords:  ")
    os.system('cls')

    if g == "-1,0,-1":
        print(" ╔══════╗")
        print(" ║·O····║")
        print(" ║······█")
        print(" ║······║")
        print(" ║······║")
        print(" ╚═█════╝")
        print("This room is 20 feet by 30 feet and has one door")
        print("This room also has an Orc inside of it")
        print('-1,0,-1')

    if g == "-1,-1,-1":
        print(" ╔══█═════╗")
        print(" ║······■·║")
        print(" ║········║")
        print(" ║········║")
        print(" ║········║")
        print(" ╚══════█═╝")
        print("This room is 20 feet by 40 feet and has two doors")
        print("This room also has a chest in it")
        print('-1,-1,-1')

    if g == "-1,-2,-1":
        print(" ╔════█╗")
        print(" ║·g···║")
        print(" █····g║")
        print(" ║···g■║")
        print(" ╚═════╝")
        print("This room is 15 feet by 25 feet and has two doors")
        print("This room also has three goblins and a chest in it")
        print('-1,-2,-1')

    if g == "-2,-2,-1":
        print(" ╔═══════╗")
        print(" ║·······║")
        print(" ║·»·····█")
        print(" ║·······║")
        print(" ╚═══════╝")
        print("This room is 15 feet by 35 feet and has one door")
        print("This room also has a downwards staircase in it")
        print('-2,-2,-1')

    if g == "0,0,-1":
        print(" ╔═════╗")
        print(" ║·g···║")
        print(" █····g║")
        print(" ║··«··║")
        print(" ╚═════╝")
        print("This room is 15 feet by 25 feet and has one door")
        print("This room also has two goblins and an upwards staircase in it")
        print('0,0,-1')

    if g == "0,0,-2":
        print(" ╔══════╗")
        print(" ║······║")
        print(" █······║")
        print(" ║··«···║")
        print(" ╚══════╝")
        print("This room is 15 feet by 30 feet and has one door")
        print("This room also has an upwards staircase in it")
        print('0,0,-2')

    if g == "-1,0,-2":
        print(" ╔═══█══╗")
        print(" ║······║")
        print(" ║·z····█")
        print(" ║····z·║")
        print(" ╚══════╝")
        print("This room is 15 feet by 30 feet and has one door")
        print("This room also has two zombies in it")
        print('-1,0,-2')
    
    if g == "-1,-1,-2":
        print(" ╔═══█══╗")
        print(" ║······║")
        print(" ║s·····║")
        print(" ║·····p║")
        print(" ╚═█════╝")
        print("This room is 15 feet by 30 feet and has one door")
        print("This room also has a skeleton and a pile of gold in it")
        print('-1,-1,-2')
    
    if g == "-1,-2,-2":
        print(" ╔══════╗")
        print(" ║··k··»║")
        print(" ║······║")
        print(" ║k···k·║")
        print(" ╚═█════╝")
        print("This room is 15 feet by 30 feet and has one door")
        print("This room also has three kobolds and a downwards staircase in it")
        print('-1,-2,-2')

    if g == "0,0,-3":
        print(" ╔════█═╗")
        print(" ║··k··«█")
        print(" ║······║")
        print(" ║k···k·║")
        print(" ╚══════╝")
        print("This room is 15 feet by 30 feet and has one door")
        print("This room also has three kobolds and a downwards staircase in it")
        print('0,0,-3')
        
    if g == "0,1,-3":
        print(" ╔══█═════╗")
        print(" ║······■·║")
        print(" ║········║")
        print(" ║········║")
        print(" ║········║")
        print(" ╚══════█═╝")
        print("This room is 20 feet by 40 feet and has two doors")
        print("This room also has a (trapped) chest in it")
        print('0,1,-3')
    
    if g == "1,0,-3":
        print(" ╔═══════╗")
        print(" ║·······║")
        print(" █···c···║")
        print(" ║·······║")
        print(" ╚═══════╝")
        print("This room is 15 feet by 35 feet and has one door")
        print("This room also has a campfire in it")
        print("1,0,-3")
    if g == "0,2,-3":
        print(" ╔═══════╗")
        print(" ║·p·····║")
        print(" ║~~~~~~~║")
        print(" ║·······║")
        print(" ╚════█══╝")
        print("This room is 15 feet by 35 feet and has one door")
        print("This room also has a stream of flowing water and a pedestal holding an amulet on it in it")
        print("0,2,-3")

while alicar:
    print("please input coordinates of the map in the ruins (format is x,y,z, e.g. starting room is 0,0,0)")

    g = input("coords:  ")
    os.system('cls')

    if g == "0,0,0":
        print(" ╔══════════════════╗")
        print(" ║·········A········║")
        print(" ║··················█")
        print(" ║···»··············║")
        print(" ║·················╔╝")
        print(" ╚═════════════════╝")
        print("This room is 20 feet by 90 feet and has one door, which acts as the entrace to the dungeon")
        print("This room also has an Ancient Guardian and a downwards staircase in it")
        print('0,0,0')
    
    if g == "0,0,-1":
        print(" ╔════════════════╗")
        print(" ║···········«····║")
        print(" ║····K···········█")
        print(" ║················║")
        print(" ╚═══════█════════╝")
        print("This room is 15 feet by 80 feet and has two doors")
        print("This room also has a knight and an upwards staircase in it")
        print('0,0,-1')

    if g == "0,-1,-1":
        print(" ╔═█══════════╗")
        print(" ║········K···║")
        print(" ║············║")
        print(" ║···K········║")
        print(" ╚═══════█════╝")
        print("This room is 15 feet by 60 feet and has two doors")
        print("This room also has two knights in it")
        print("0,-1,-1")
    if g == "0,-2,-1":
        print(" ╔═══════█═══╗")
        print(" ║··K·····K··║")
        print(" ║···········║")
        print(" ║···K·······║")
        print(" ╚═══════════╝")
        print("This room is 15 feet by 60 feet and has two doors")
        print("This room also has three knights in it")
        print("0,-2,-1")

    if g == "1,0,-1":
        print(" ╔═══█═════╗")
        print(" █·········║")
        print(" ║·K····K··║")
        print(" ╚═════════╝ ")
        print("This room is 10 feet by 45 feet and has one door")
        print("This room also has two knights in it")
        print("1,0,-1")
    if g == "1,1,-1":
        print(" ╔══════█══╗")
        print(" ║·········║")
        print(" ╚█════════╝ ")
        print("This room is 5 feet by 45 feet and has one door")
        print("This room also has nothing in it")
        print("1,1,-1")
    if g == "1,2,-1":
        print(" ╔══█═════╗")
        print(" ║······■·║")
        print(" ║········║")
        print(" ║···K····║")
        print(" ║···KK···║")
        print(" ╚══════█═╝")
        print("This room is 20 feet by 40 feet and has two doors")
        print("This room also has three knights and a chest in it")
        print('1,2,-1')
    if g == "1,3,-1":
        print(" ╔═══════╗")
        print(" ║·····K·║")
        print(" ║·»·····║")
        print(" ║·······║")
        print(" ╚═══█═══╝")
        print("This room is 15 feet by 35 feet and has one door")
        print("This room also has a knight and a downwards staircase in it")
        print('1,3,-1')
    if g == "0,0,-2":
        print(" ╔═════════╗")
        print(" ║········«║")
        print(" ╚█════════╝ ")
        print("This room is 5 feet by 45 feet and has one door")
        print("This room also has an upwards staircase in it")
        print("0,0,-2")
    if g == "0,-1,-2":
        print(" ╔══█═════╗")
        print(" ║······■·║")
        print(" ║········║")
        print(" ║·K······║")
        print(" ║·······K║")
        print(" ╚══════█═╝")
        print("This room is 20 feet by 40 feet and has two doors")
        print("This room also has two knights and a chest in it")
        print("0,-1,-2")
    if g == "0,-2,-2":
        print(" ╔═█══════╗")
        print(" ║······KK║")
        print(" ║········║")
        print(" ║KK····»·║")
        print(" ╚════════╝")
        print("This room is 20 feet by 40 feet and has two doors")
        print("This room also has four knights and a chest in it")
        print("0,-2,-2")
    if g == "0,0,-3":
        print(" ╔════════╗")
        print(" ║·····«··║")
        print(" ║p·······║")
        print(" ║········║")
        print(" ╚════════╝")
        print("This room is 20 feet by 40 feet and has two doors")
        print("This room also has a pedestal with Gungnir, Spear of the All-Father on it in it")
        print("0,0,-3")

while doom:
    print("please input coordinates of the map in the dungeon (format is x,y,z, e.g. first room is 0,0,-1)")
    g = input("coords:  ")
    os.system('cls')
    
    if g == "0,0,-1":
        print(" ╔══════╗")
        print(" ║«·····║")
        print(" ║······█")
        print(" ║······║")
        print(" ║······║")
        print(" ╚═█════╝")
        print("This room is 20 feet by 30 feet and has one door")
        print("This room also has an upwards staircase inside of it")
        print('0,0,-1')
    
    if g == "0,-1,-1":
        print(" ╔══█═══╗")
        print(" ║····o·║")
        print(" ║······║")
        print(" ║·····o║")
        print(" ║···o··║")
        print(" ╚═█════╝")
        print("This room is 20 feet by 30 feet and has one door")
        print("This room also has three orcs in it")
        print('0,-1,-1')
    
    if g == "0,-2,-1":
        print(" ╔════█═╗")
        print(" ║·····o║")
        print(" ║o·····║")
        print(" ║······║")
        print(" ║···o··║")
        print(" ╚█═════╝")
        print("This room is 20 feet by 30 feet and has one door")
        print("This room also has three orcs in it")
        print('0,-2,-1')
    
    if g == "0,-3,-1":
        print(" ╔═════█╗")
        print(" ║gg····║")
        print(" ║·g····║")
        print(" ║······║")
        print(" ║···g·g║")
        print(" ╚══════╝")
        print("This room is 20 feet by 30 feet and has one door")
        print("This room also has five goblins in it")
        print('0,-3,-1')          
    
    if g == "1,0,-1":
        print(" ╔═══════╗")
        print(" ║·p·····█")
        print(" █·······║")
        print(" ║·······║")
        print(" ╚═══════╝")
        print("This room is 15 feet by 35 feet and has one door")
        print("This room also has a pedestal with a fake amulet of yendor on it in it")
        print('1,0,-1')

    if g == "2,0,-1":
        print(" ╔══█════╗")
        print(" ║s··ss··║")
        print(" ║s·····s║")
        print(" █·····ss║")
        print(" ╚═══════╝")
        print("This room is 15 feet by 35 feet and has one door")
        print("This room also has seven slimes in it")
        print('2,0,-1')
   
    if g == "2,1,-1":
        print(" ╔═══════╗")
        print(" ║d······█")
        print(" ║·······║")        
        print(" ║·······║")
        print(" ║·······║")
        print(" ║·······║")
        print(" ╚═══█═══╝")
        print("This room is 25 feet by 35 feet and has one door")
        print("This room also has a Silver Dragon in it")
        print('2,1,-1')
    
    if g == "3,1,-1":
        print(" ╔═══════╗")
        print(" ║·······║")
        print(" ║·······║")        
        print(" █·······║")
        print(" ║·······║")
        print(" ║·······║")
        print(" ╚═══█═══╝")
        print("This room is 25 feet by 35 feet and has one door")
        print("This room also has nothing in it")
        print('3,1,-1')

    if g == "3,0,-1":
        print(" ╔═══█═══╗")
        print(" ║·······║")
        print(" ║■······║")        
        print(" ║·······║")
        print(" ║·······║")
        print(" ║····»··║")
        print(" ╚═══════╝")
        print("This room is 25 feet by 35 feet and has one door")
        print("This room also has a chest and a downwards staircase in it")
        print('3,0,-1')
    
    if g == "3,0,-1":
        print(" ╔═══════╗")
        print(" ║■······║")
        print(" ║·······█")        
        print(" ║····«··║")
        print(" ╚═══════╝")
        print("This room is 25 feet by 35 feet and has one door")
        print("This room also has a chest and an upwards staircase in it")
        print('0,0,-2')

if choice == "9":
    print("The shop is selling:", "\n", random.choice(blesscurse), random.choice(item), "for", random.randint(50,500), "¤", "\n", random.choice(blesscurse), random.choice(item), "for", random.randint(50,500), "¤", "\n", random.choice(blesscurse), random.choice(weapon), "for", random.randint(50,500), "¤", "\n", random.choice(blesscurse), random.choice(armor), "for", random.randint(50,500), "¤", "\n", random.choice(blesscurse), "Scroll of", random.choice(spellscrolls), "for", random.randint(50,500), "¤", "\n", random.choice(blesscurse), "Scroll of", random.choice(spellscrolls), "for", random.randint(50,500), "¤",)

if menu:
    input("Input anything to close the program   ")
    
    
