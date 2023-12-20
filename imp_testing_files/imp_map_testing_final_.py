import random
import time 
import os
doom = False
alicar = False

print("Are you wanting to view the Dungeons of Deslicar or Ruins of Alicar (Deslicar, Alicar)")
selection = input("# ")
if selection == "Deslicar":
    doom = True
if selection == "Alicar":
    alicar = True
while doom:
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

    if g == "-1,-2,-1":
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
        print('-1,-1,-2')

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
        print("1,0,-3")

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
        print(" ╔═══════════╗")
        print(" ║··K·····K··║")
        print(" ║···········║")
        print(" ║···K·······║")
        print(" ╚═══════█═══╝")
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
        print(" ╔═█═══════╗")
        print(" ║·········║")
        print(" ╚════════█╝ ")
        print("This room is 5 feet by 45 feet and has one door")
        print("This room also has two knights in it")
        print("1,0,-1")

input("Exiting Program...   ")
