import os
import random

#magic numbers
START_HP = 30
START_HP_MAX = 500
START_ATK = 5
START_POT = 5
START_ELX = 5
START_GLD = 50
START_X = 0
START_Y = 0
STAT_LEN = 10
POT_HEAL = 5
ELX_HEAL = 10
SMTHNG = 3

#Hero starting stats
HP = START_HP
HP_MAX = START_HP_MAX
ATK = START_ATK
POT = START_POT
ELX = START_ELX
GLD = START_GLD
x = START_X
y = START_Y
operating_system = ""

#Game starting variables
run = True
menu = True
play = False
rules = False
key = False
fight = True
standing = True
buy = False
speak = False
boss = False
select = False

#map of the corrupted lands 5x5
map = [
    [";", ",", ".", "S", "."],
    [";", ";", ",", ".", "."],
    [",", ",", "T", ".", "."],
    [",", "T", "T", ".", "M"],
    ["T", "K", "T", "M", "A"]]

y_len = len(map) - 1
x_len = len(map[0]) - 1

biome = {
    ",": {
        "t": "PLAINS",
        "e": 33,
        "m": ["Skeleton", "Goblin", "Orc"]

    },
    ".": {
        "t": "DESERT",
        "e": 25,
        "m": ["Skeleton", "Mummy"]
    },
    ";": {
        "t": "TALL GRASS",
        "e": 30,
        "m": ["Skeleton", "Goblin", "Orc"]
    },
    "A": {
        "t": "ACADEMY",
        "e": 0,
        "m": []
    },
    "M": {
        "t": "MOUNTAINS",
        "e": 100,
        "m": ["Orc"]
    },
    "T": {
        "t": "FOREST",
        "e": 75,
        "m": ["Skeleton", "Goblin", "Orc"]
    },
    "S": {
        "t": "MERCHANT",
        "e": 0,
        "m": []
    },
    "K": {
        "t": "KING",
        "e": 0,
        "m": 0
    }
}

mobs = {
    "Skeleton": {
        "hp": [5,5,5,5,6,4],
        "dg": [2],
        "ac": 60,
        "gd": [4,4,4,5,5,6,10]
    },
    "Goblin": {
        "hp": [10],
        "dg": [5],
        "ac": 80,
        "gd": [12]
    },
    "Orc": {
        "hp": [15,20,35],
        "dg": [6],
        "ac": 90,
        "gd": [12,15,20]
    },
    "Mummy": {
        "hp": [40],
        "dg": [10],
        "ac": 100,
        "gd": [30]
    },
    "Evil Wizard": {
        "hp": [60],
        "dg": [15],
        "ac": 100,
        "gd": [100]
    }
}

current_tile = map[y][x]
name_of_tile = biome[current_tile]["t"]

def clear():

    if operating_system == "MAC":
        os.system('clear')
    elif operating_system == "WIN":
        os.system('cls')

def divide():
    print('================================================================')

def save():
    stats = [
        hero_name,
        str(HP),
        str(ATK),
        str(POT),
        str(ELX),
        str(GLD),
        str(x),
        str(y),
        str(key),
        str(operating_system)
    ]

    f = open("load.txt", "w")

    for item in stats:
        f.write(item + "\n")
    f.close()

def heal(amount):
    global HP
    if HP + amount < HP_MAX:
        HP += amount
    else:
        HP = HP_MAX
    print("You feel stronger!")
    print(hero_name + "'s" + " HP has been increased to " + str(HP) + "!")

def battle():
    global fight, play, run, HP, POT, ELX, GLD, boss

    if not boss:
        enemy = random.choice(biome[map[y][x]]["m"])
    else:
        enemy = "Evil Wizard"
    hp = random.choice(mobs[enemy]["hp"])
    hpmax = hp
    atk = random.choice(mobs[enemy]["dg"])
    g = random.choice(mobs[enemy]["gd"])

    while fight:
        clear()
        divide()
        print("A " + enemy + " wants to fight you!")
        divide()
        print(enemy + "'s HP: " + str(hp) + "/" + str(hpmax))
        print(hero_name + "'s HP: " + str(HP) + "/" + str(HP_MAX))
        print("POTIONS: ", end="")
        for i in range(POT):
            print("() ", end="")
        print()
        print("ELIXERS: ", end="")
        for i in range(ELX):
            print("[] ", end="")
        print()
        divide()
        print("1 - ATTACK")
        if POT > 0:
            print("2 - USE POTION (5 HP)")
        if ELX > 0:
            print("3 - USE ELIXER (10 HP)")
        divide()

        choice = input("# ")

        if choice == "1":
            hp -= ATK
            print(hero_name + " dealt " + str(ATK) + " damage to the " + enemy + ".")
            if hp > 0:
                if random.randint(0,100) <= mobs[enemy]["ac"]:
                    HP -= atk
                    print(enemy + " dealt " + str(atk) + " damage to " + hero_name + ".")
                else:
                    print(enemy + " missed!")
            input("> ")
        
        elif choice == "2":
            if POT > 0:
                POT -= 1
                heal(POT_HEAL)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + hero_name + ".")
                input("> ")
            else:
                print("You are out of POTIONS!")
                input("> ")

        elif choice == "3":
            if ELX > 0:
                ELX -= 1
                heal(ELX_HEAL)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + hero_name + ".")
                input("> ")
            else:
                print("You are out of ELIXERS!")
                input("> ")

        if HP <= 0:
            print("The " + enemy + " defeated " + hero_name + "...")
            divide()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")
            clear()
        
        if hp <= 0:
            print(hero_name + " defeated the " + enemy + "!")
            divide()
            fight = False
            GLD += g
            print("You found " + str(g) + " gold!")
            if random.randint(0, 100) <= 30:
                POT += 1
                print("You've found a POTION!")
            if enemy == "Evil Wizard":
                print("Congratulations! You've defeated the Evil Wizard!")
                print("You have finished the game!")
                boss = False
                play = False
                run = False
            input("> ")
            clear()
 
def shop():
    global buy, GLD, POT, ELX, ATK

    while buy:
        clear()
        divide()
        print("Welcome to my humble shop...")
        divide()
        print("GOLD: " + str(GLD))
        print("POTIONS: " + str(POT))
        print("ELIXERS: " + str(ELX))
        print("ATK: " + str(ATK))
        divide()
        print("1 - BUY POTION (" + str(POT_HEAL) + ") - 5 GOLD")
        print("2 - BUY ELIXER (" + str(ELX_HEAL) + ") - 8 GOLD")
        print("3 - UPGRADE WEAPON (" + str(SMTHNG) + "ATK) - 10 GOLD")
        print("4 - LEAVE")
        divide()

        choice = input("# ")

        if choice == "1":
            if GLD >= 5:
                POT += 1
                GLD -= 5
                print("You've bought a POTION!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "2":
            if GLD >= 8:
                ELX += 1
                GLD -= 8
                print("You've bought an ELIXER!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "3":
            if GLD >= 10:
                ATK += SMTHNG
                GLD -= 10
                print("Your sword shines brighter! (" + str(ATK) + "ATK)")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "4":
            buy = False

def king():
    global speak, key

    while speak:
        clear()
        divide()
        print("Hello there, " + hero_name + "!")
        if ATK < 10:
            print("You're not strong enough! The Evil Wizard will burn you alive!")
            print("Keep sharpening your skills!")
            key = False
        else:
            print("This will let you into the Academy! Slay the Wizard!")
            print("Received: KEY")
            key = True
        
        divide()
        print("1 -LEAVE")
        divide()
        choice = input("# ")
        if choice == "1":
            speak = False

def academy():
    global boss, key, fight

    while boss:
        clear()
        divide()
        print("You approach the gates of the Academy")
        print("What will you do?")
        divide()
        if key:
            print("1 - USE KEY")
        print("2 - TURN BACK")
        divide()

        choice = input("# ")

        if choice == "1":
            fight = True
            battle()
        elif choice == "2":
            boss = False


while run:
    while menu:
        clear()
        divide()
        print("1 - NEW GAME")
        print("2 - LOAD GAME")
        print("3 - RULES")
        print("4 - QUIT")
        divide()

        if rules:
            clear()
            divide()
            print("These are the rules.")
            divide()
            rules = False
            choice = ""
            input("> ")
        else:
            choice = input("# ")

        if choice == "1":
            clear()

            select = True
            while select:
                clear()
                print("What system are you playing on?")
                print("1 - MAC")
                print("2 - WIN")
                divide()
                choice = input("# ")
                if choice == "1":
                    operating_system = "MAC"
                    clear()
                    print("You chose MAC as your system!")
                    select = False
                if choice == "2":
                    operating_system = "WIN"
                    clear()
                    print("You chose WIN as your system!")
                    select = False
                input("> ")
            clear()
            print("What is your name Hero?")
            hero_name = input("# ")
            menu = False
            play = True
        elif choice == "2":
            try:
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == STAT_LEN:
                    hero_name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    POT = int(load_list[3][:-1])
                    ELX = int(load_list[4][:-1])
                    GLD = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    operating_system = str(load_list[9][:-1])
                    clear()
                    print(hero_name, ": HP =", HP, "ATK =", ATK, "Gold =", GLD)
                    print("welcome back, " + hero_name + "!")
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("Save file corrupt, please create new character!")
                    input("> ")
            except OSError:
                print("No saved file! Please select #1 NEW GAME")
                input("> ")
        elif choice == "3":
            clear()
            rules = True
        elif choice == "4":
            clear()
            print("Game Quit Successfully")
            quit()

    while play:
        save() #autosave
        clear()
        
        if not standing and random.randint(0, 100) <= biome[map[y][x]]["e"]:
                fight = True
                battle()

        if play:

            #Draws map
            clear()
            divide()
            print("LOCATION: " + biome[map[y][x]]["t"])
            divide()
            for r in range(len(map)):
                print("| ", end="")
                for c in range(len(map[r])):
                    if r == y and c == x:
                        print("@", end = " ")
                    else:
                        print(map[r][c], end = " ")
                print("|")
            divide()

            #Draws relevant stats
            print("NAME: " + hero_name)
            print("HP: " + str(HP) + "/" + str(HP_MAX))
            print("ATK: " + str(ATK))
            print("POTIONS: ", end="")
            for i in range(POT):
                print("() ", end="")
            print()
            print("ELIXERS: ", end="")
            for i in range(ELX):
                print("[] ", end="")
            print()
            print("GOLD: " + str(GLD))
            divide()

            #Draws play options
            if y > 0:
                print("W - \u25B2 " + biome[map[y - 1][x]]["t"])
            if x > 0:
                print("A - \u25C0 " + biome[map[y][x - 1]]["t"])
            if y < y_len:
                print("S - \u25BC " + biome[map[y + 1][x]]["t"])
            if x < x_len:
                print("D - \u25B6 " + biome[map[y][x + 1]]["t"])
            if POT > 0:
                print("5 - use POTION")
            if ELX > 0:
                print("6 - use ELIXER")
            if map[y][x] == "S" or map[y][x] == "K" or map[y][x] == "A":
                print("7 - ENTER")
            print("0 - SAVE AND QUIT")
            divide()

            dest = input("# ").upper()

        if dest == "0":
            play = False
            menu = True
            save() #auto quit save
        
        #actions
        if dest == "W":
            if y > 0:
                y -= 1
                standing = False
        elif dest == "D":
            if x < x_len:
                x += 1
                standing = False
        elif dest == "S":
            if y < y_len:
                y += 1
                standing = False
        elif dest == "A":
            if x > 0:
                x -= 1
                standing = False
        elif dest == "5":
            if POT > 0:
                heal(POT_HEAL)
                POT -= 1
            else:
                print("You are out of POTIONS!")
            input("> ")
            standing = True
        elif dest == "6":
            if ELX > 0:
                heal(ELX_HEAL)
                ELX -= 1
            else:
                print("You are out of ELIXERS!")
            input("> ")
            standing = True
        elif dest == "7":
            if map[y][x] == "S":
                buy = True
                shop()
            if map[y][x] == "K":
                speak = True
                king()
            if map[y][x] == "A":
                boss = True
                academy()
        else:
            standing = True