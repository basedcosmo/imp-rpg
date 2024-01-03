#imp uMoria clone rewrite. was going to transfer whole imp game to a system like this, too much effort for now. this is more of a light baseline for anyone.
#classified as a test file, not for use in normal play, more of a test build
import time
import random
looptest = False
consoleloop = True
skills = "Melee: None\nRanged: None\nArcane Magic: None\nHoly Magic: None\nMedical: None\nLockpick: None\nStealth: None\nCharisma: None"
while consoleloop:
    print("\nConsole Input")
    console = ""
    console = input("#")

    if console == "/help":
        print("\nHere is a list of commands: \n/help\n/looptest\n/cgen\n/classes\n/info\n/warrior\n/thief\n/scholar\n/hunter\n/knight\n/skills")
    if console == "/skills":
        print("Skills are on a range from None, Basic, Intermediate, Advanced, Mastery")
        print("Melee, Ranged, Arcane Magic, Holy Magic, Medical, Lockpick, Stealth, Charisma")
    if console == "/looptest":
        looptest = True
    if console == "/cgen":
        cname = input("name: ")
        ccls = input("class: ")
        if ccls == "Warrior":
            skills = "Melee: Intermediate\nRanged: None\nArcane Magic: None\nHoly Magic: None\nMedical: Basic\nLockpick: Basic\nStealth: Basic\nCharisma: Basic"
        if ccls == "Thief":
            skills = "Melee: Basic\nRanged: Basic\nArcane Magic: None\nHoly Magic: None\nMedical: None\nLockpick: Advanced\nStealth: Intermediate\nCharisma: Basic"
        if ccls == "Scholar":
            skills = "Melee: None\nRanged: None\nArcane Magic: Advanced\nHoly Magic: None\nMedical: None\nLockpick: None\nStealth: None\nCharisma: None"
        if ccls == "Priest":
            skills = "Melee: Basic\nRanged: None\nArcane Magic: None\nHoly Magic: Advanced\nMedical: Intermediate\nLockpick: None\nStealth: None\nCharisma: None"
        if ccls == "Hunter":
            skills = "Melee: None\nRanged: Intermediate\nArcane Magic: None\nHoly Magic: None\nMedical: Basic\nLockpick: Basic\nStealth: Basic\nCharisma: Basic"
        cstr = random.randint(3,8)
        cdex = random.randint(3,8)
        cint = random.randint(3,8) 
        cvit = random.randint(3,10)
        print("\nname:", cname, "\nclass:", ccls, "\nstrength:", cstr, "\ndexterity:", cdex, "\nintellect", cint, "\nvitality:", cvit, "\n", skills)
    if console == "/classes":
        print("Warrior, Thief, Scholar, Priest, Hunter")
        print("Try '/Warrior' or other similar commands to check a classes abilities")
    if console == "/warrior":
        print("Warriors are a basic fighting class, that can use any melee weapon and any armor, but have basic skills.")
    if console == "/thief":
        print("Thieves are a roguery centric class, that can use any small weapon, cloth armor, and have advanced roguery skills.")
    if console == "/scholar":
        print("Scholars are a arcane magic centric class, that can use polearms, magic robes, and have advanced arcane skills.")
    if console == "/priest":
        print("Priests are a holy magic centric class, that can use blunt weapons, any armor, and have advanced healing skills.")
    if console == "/hunter":
        print("Hunters are a ranged fighting class, that can use any ranged weapon and any armor, but have basic skills.")
    while looptest:
        print("IMP LOOP TESTING TOOL")
        time.sleep(1)
    