import os
import random
import ast

#magic numbers
START_HP = 10
START_HP_MAX = 10
START_ATK = 2
START_CRT = 1
START_POT = 2
START_ELX = 3
START_GLD = 0
START_EVA = 0
START_X = 0
START_Y = 0
START_SEEN_TILES = []
STAT_LEN = 14

MAX_POT = 4
MAX_ELX = 4
POT_HEAL = 5
ELX_HEAL = 10
WEP_SMTH = 1
ARM_SMTH = 1

#Hero starting stats
HP = START_HP
HP_MAX = START_HP_MAX
ATK = START_ATK
CRT = START_CRT
EVA = START_EVA
POT = START_POT
ELX = START_ELX
GLD = START_GLD
x = START_X
y = START_Y
SEEN_TILES = START_SEEN_TILES
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
    list(",,,.."),
    list(",,..."),
    list("/,.S."),
    list("//,.."),
    list("~~T.."),
    list("~TT.M"),
    list("TKTMA")]

y_len = len(map) - 1
x_len = len(map[0]) - 1

biome = {
    "~": {
        "d": "\033[2m~\033[0m",
        "t": "RIVER",
        "e": 0,
        "m": ["Error"],
        "w": False
    },
    ",": {
        "d": "\033[2m,\033[0m",
        "t": "PLAINS",
        "e": 33,
        "m": ["Skeleton", "Goblin", "Troll"],
        "w": True
    },
    ".": {
        "d": "\033[2m.\033[0m",
        "t": "DESERT",
        "e": 75,
        "m": ["Skeleton", "Mummy"],
        "w": True
    },
    "/": {
        "d": "\033[2m/\033[0m",
        "t": "TALL GRASS",
        "e": 30,
        "m": ["Skeleton", "Goblin", "Bandit", "Troll"],
        "w": True
    },
    "A": {
        "d": "A",
        "t": "ACADEMY",
        "e": 0,
        "m": ["Error"],
        "w": True
    },
    "M": {
        "d": "\033[2mM\033[0m",
        "t": "MOUNTAINS",
        "e": 100,
        "m": ["Orc"],
        "w": True
    },
    "T": {
        "d": "\033[2mT\033[0m",
        "t": "FOREST",
        "e": 75,
        "m": ["Skeleton", "Goblin", "Orc"],
        "w": True
    },
    "S": {
        "d": "S",
        "t": "MERCHANT",
        "e": 0,
        "m": ["Error"],
        "w": True
    },
    "K": {
        "d": "K",
        "t": "KING",
        "e": 0,
        "m": ["Error"],
        "w": True
    }
}

mobs = {
    "Troll": {
        "hp": [15],
        "dg": [5],
        "ac": [50],
        "gd": [14],
        "rn": [95],
        "ef": ["none"]
    },
    "Error": {
        "hp": [1],
        "dg": [1],
        "ac": [1],
        "gd": [1],
        "rn": [100],
        "ef": ["none"]
    },
    "Bandit": {
        "hp": [12],
        "dg": [1,2,3],
        "ac": [90],
        "gd": [1,2,3,4,5],
        "rn": [10],
        "ef": ["steal"]
    },
    "Skeleton": {
        "hp": [5,5,5,3,6,4],
        "dg": [2],
        "ac": [60],
        "gd": [4,4,4,5,5,6,10],
        "rn": [100],
        "ef": ["none"]
    },
    "Goblin": {
        "hp": [10],
        "dg": [4],
        "ac": [80],
        "gd": [12],
        "rn": [50],
        "ef": ["none"]
    },
    "Orc": {
        "hp": [25,30,35],
        "dg": [6],
        "ac": [90],
        "gd": [12,15,20],
        "rn": [20],
        "ef": ["none"]
    },
    "Mummy": {
        "hp": [40],
        "dg": [10],
        "ac": [100],
        "gd": [30],
        "rn": [95],
        "ef": ["none"]
    },
    "Evil Wizard": {
        "hp": [100],
        "dg": [15],
        "ac": [100],
        "gd": [100],
        "rn": [0],
        "ef": ["none", "fireball"]
    }
}

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
        str(HP_MAX),
        str(ATK),
        str(CRT),
        str(EVA),
        str(POT),
        str(ELX),
        str(GLD),
        str(x),
        str(y),
        str(SEEN_TILES),
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
    print(hero_name + "'s" + " HP has been increased to " + str(HP) + "!")

def mob_effect(effect, enemy):
    global HP, POT, ELX, GLD, HP_MAX

    if effect == "none":
        pass
    elif effect == "steal":
        stolen = random.randint(1,6)
        if stolen <= GLD:
            GLD -= stolen
            print(enemy + " stole " + str(stolen) + " GOLD from you!")
        else:
            GLD = 0
            print(enemy + " stole all of your of your GOLD!")
    elif effect == "fireball":
        print(enemy + " cast a FIREBALL and did 15 extra damage to " + hero_name + "!")
        HP -= 10

def draw_mob_stats(enemy, hp, hpmax, atk):
    print(enemy)
    print("HP: " + str(hp) + "/" + str(hpmax), end=" ")
    for i in range(10):
        if i/10 < hp/hpmax:
            print("\u2588", end="")
        else:
            print("_", end="")
    print()
    print("ATK: " + str(atk))

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
    ac = random.choice(mobs[enemy]["ac"])
    boss = False

    clear()
    print("A " + enemy + " wants to fight you!")
    input("> ")

    while fight:
        clear()
        divide()
        draw_mob_stats(enemy, hp, hpmax, atk)
        divide()  
        draw_stats()
        divide()
        print("1 - ATTACK")
        if POT > 0:
            print("2 - USE POTION (5 HP)")
        if ELX > 0:
            print("3 - USE ELIXER (10 HP)")
        print("4 - RUN!")
        divide()

        choice = input("# ")
        DMG = random.randint(ATK, ATK + CRT)
        if choice == "1":
            hp -= DMG
            print(hero_name + " dealt " + str(DMG) + " damage to the " + enemy + ".")
            if hp > 0:
                if random.randint(0,100) <= ac - EVA:
                    HP -= atk
                    print(enemy + " dealt " + str(atk) + " damage to " + hero_name + ".")
                else:
                    print(enemy + " missed!")
            mob_effect(random.choice(mobs[enemy]["ef"]), enemy)
            input("> ")
        
        elif choice == "2":
            if POT > 0:
                POT -= 1
                heal(POT_HEAL)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + hero_name + ".")
                mob_effect(random.choice(mobs[enemy]["ef"]), enemy)
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
                mob_effect(random.choice(mobs[enemy]["ef"]), enemy)
                input("> ")
            else:
                print("You are out of ELIXERS!")
                input("> ")
        elif choice == "4":
            if random.randint(1, 100) <= random.choice(mobs[enemy]["rn"]):
                print("You ran away from the " + enemy + " successfully!")
                input("> ")
                fight = False
            else:
                HP -= atk
                print("The " + enemy + " stopped you from fleeing!")
                print(enemy + " dealt " + str(atk) + " damage to " + hero_name + ".")
                mob_effect(random.choice(mobs[enemy]["ef"]), enemy)
                input("> ")

        if HP <= 0:
            divide()
            clear()
            print("The " + enemy + " defeated " + hero_name + "...")
            divide()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")
            clear()
        
        if hp <= 0:
            divide()
            clear()
            print(hero_name + " defeated the " + enemy + "!")
            divide()
            fight = False
            GLD += g
            print("You found " + str(g) + " gold!")
            if random.randint(1, 100) <= 30 and POT < MAX_POT:
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
    global buy, GLD, POT, ELX, ATK, CRT, EVA, HP_MAX, MAX_POT, MAX_ELX

    while buy:
        clear()
        divide()
        print("Welcome to my humble shop...")
        divide()
        draw_stats()
        divide()
        print("1 - BUY POTION (" + str(POT_HEAL) + ") - 5 GOLD")
        print("2 - BUY ELIXER (" + str(ELX_HEAL) + ") - 8 GOLD")
        print("3 - UPGRADE WEAPON (+" + str(WEP_SMTH) + " ATK) - 10 GOLD")
        print("4 - SHARPEN WEAPON (+" + str(WEP_SMTH) + " CRT) - 5 GOLD")
        print("5 - UPGRADE ARMOR (+" + str(ARM_SMTH) + " MAX HP) - 10 GOLD")
        print("6 - ENHANCE ARMOR (+" + str(1) + " EVA) - 5 GOLD")
        print("0 - LEAVE")
        divide()

        choice = input("# ")

        if choice == "1":
            if POT == MAX_POT:
                print("You can't carry any more POTIONS!")
            else:
                if GLD >= 5:
                    POT += 1
                    GLD -= 5
                    print("You've bought a POTION!")
                else:
                    print("Not enough gold!")
            input("> ")
        elif choice == "2":
            if ELX == MAX_ELX:
                print("You can't carry any more ELIXERS!")
            else:
                if GLD >= 8:
                    ELX += 1
                    GLD -= 8
                    print("You've bought an ELIXER!")
                else:
                    print("Not enough gold!")
            input("> ")
        elif choice == "3":
            if GLD >= 10:
                ATK += WEP_SMTH
                GLD -= 10
                print("Your sword shines brighter! (" + str(ATK) + "ATK)")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "4":
            if GLD >= 5:
                CRT += WEP_SMTH
                GLD -= 5
                print("Your sword looks sharper! (" + str(CRT) + "CRT)")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "5":
            if GLD >= 10:
                HP_MAX += ARM_SMTH
                GLD -= 10
                print("Your armor shines brighter! (" + str(HP_MAX) + "MAX HP)")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "6":
            if GLD >= 5:
                EVA += ARM_SMTH
                GLD -= 5
                print("Your armor feels lighter! (" + str(EVA) + "EVA)")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "0":
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
        print("1 - LEAVE")
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
        print("The gates require a key. What will you do?")
        divide()
        if key:
            print("1 - USE KEY")
        print("2 - TURN BACK")
        divide()

        choice = input("# ")

        if choice == "1" and key:
            fight = True
            battle()
        elif choice == "2":
            boss = False

def draw_map():
    global SEEN_TILES

    #updates seen tiles in map
    if (x, y) not in SEEN_TILES:
        SEEN_TILES.append((x, y))
    if (x, (y - 1)) not in SEEN_TILES:
        SEEN_TILES.append((x, (y - 1)))
    if (x, (y + 1)) not in SEEN_TILES:
        SEEN_TILES.append((x, (y + 1)))
    if ((x - 1), y) not in SEEN_TILES:
        SEEN_TILES.append(((x - 1), y))
    if ((x + 1), y) not in SEEN_TILES:      
        SEEN_TILES.append(((x + 1), y))

    print("LOCATION: " + biome[map[y][x]]["t"])
    divide()
    print("\u250C", end="")
    for r in range(len(map[0]) + 2):
        print("\u2500", end="")
    print("\u2510")
    for r in range(len(map)):
        print("\u2502 ", end="")
        for c in range(len(map[r])):
            if r == y and c == x:
                print("\033[1m@\033[0m", end = "")
            elif (c, r) in SEEN_TILES:
                print(biome[map[r][c]]["d"], end = "")
            else:
                print(" ", end="")
        print(" \u2502")
    print("\u2514", end="")
    for r in range(len(map[0]) + 2):
        print("\u2500", end="")
    print("\u2518")

def draw_stats():
    print("NAME: " + hero_name)
    print("HP: " + str(HP) + "/" + str(HP_MAX), end=" ")
    for i in range(10):
        if i/10 < HP/HP_MAX:
            print("\u2588", end="")
        else:
            print("_", end="")
    print()
    print("ATK-CRT/EVA: " + str(ATK) + "-" + str(CRT + ATK) + " / " + str(EVA))
    print("POTIONS: ", end="")
    for i in range(4):
        if i < POT:
            print("\033[94m()\033[0m ", end="")
        else:
            print("\033[2m()\033[0m ", end="")
    print()
    print("ELIXERS: ", end="")
    for i in range(4):
        if i < ELX:
            print("\033[34m[]\033[0m ", end="")
        else:
            print("\033[2m[]\033[0m ", end="")
    print()
    print("GOLD: " + str(GLD))  
 
def draw_actions():
    if y > 0:
        print("W - \u25B2 " + biome[map[y - 1][x]]["t"])
    if x > 0:
        print("A - \u25C0 " + biome[map[y][x - 1]]["t"])
    if y < y_len:
        print("S - \u25BC " + biome[map[y + 1][x]]["t"])
    if x < x_len:
        print("D - \u25B6 " + biome[map[y][x + 1]]["t"])
    if POT > 0:
        print("2 - use POTION")
    if ELX > 0:
        print("3 - use ELIXER")
    if map[y][x] == "S" or map[y][x] == "K" or map[y][x] == "A":
        print("E - ENTER")
    print("0 - SAVE AND QUIT")

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
            if len(hero_name) == 0:
                hero_name = "Hero"
            menu = False
            play = True
        elif choice == "2":
            try:
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == STAT_LEN:
                    hero_name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    HP_MAX = int(load_list[2][:-1])
                    ATK = int(load_list[3][:-1])
                    CRT = int(load_list[4][:-1])
                    EVA = int(load_list[5][:-1])
                    POT = int(load_list[6][:-1])
                    ELX = int(load_list[7][:-1])
                    GLD = int(load_list[8][:-1])
                    x = int(load_list[9][:-1])
                    y = int(load_list[10][:-1])
                    temp = ast.literal_eval(load_list[11])
                    print(temp)
                    SEEN_TILES = ast.literal_eval(load_list[11])
                    key = bool(load_list[12][:-1])
                    operating_system = str(load_list[13][:-1])
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
        
        if not standing and random.randint(1, 100) <= biome[map[y][x]]["e"]:
            fight = True
            battle()

        if play:
            clear()
            divide()
            draw_map()
            divide()
            draw_stats()
            divide()
            draw_actions()
            divide()

            # Get input for actions
            dest = input("# ").upper()

        if dest == "0":
            play = False
            menu = True
            save() #auto quit save
        
        #actions
        if dest == "W" and y > 0 and biome[map[y - 1][x]]["w"]:
            y -= 1
            standing = False
        elif dest == "D" and x < x_len and biome[map[y][x + 1]]["w"]:
            x += 1
            standing = False
        elif dest == "S" and y < y_len and biome[map[y + 1][x]]["w"]:
            y += 1
            standing = False
        elif dest == "A" and x > 0 and biome[map[y][x - 1]]["w"]:
            x -= 1
            standing = False
        elif dest == "2":
            if POT > 0:
                if HP == HP_MAX:
                    print("You are already at MAX HP!")
                else:
                    heal(POT_HEAL)
                    POT -= 1
            else:
                print("You are out of POTIONS!")
            input("> ")
            standing = True
        elif dest == "3":
            if ELX > 0:
                if HP == HP_MAX:
                    print("You are already at MAX HP!")
                else:
                    heal(ELX_HEAL)
                    ELX -= 1
            else:
                print("You are out of ELIXERS!")
            input("> ")
            standing = True
        elif dest == "E":
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