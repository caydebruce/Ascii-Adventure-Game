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
STAT_LEN = 9
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
        "e": True
    },
    ".": {
        "t": "DESERT",
        "e": True
    },
    ";": {
        "t": "TALL GRASS",
        "e": True
    },
    "A": {
        "t": "ACADEMY",
        "e": False
    },
    "M": {
        "t": "MOUNTAINS",
        "e": True
    },
    "T": {
        "t": "FOREST",
        "e": True
    },
    "S": {
        "t": "MERCHANT",
        "e": False
    },
    "K": {
        "t": "KING",
        "e": False
    }
}

e_list = ["Skeleton", "Goblin", "Orc"]

mobs = {
    "Skeleton": {
        "hp": random.randint(3,6),
        "dg": 2,
        "gd": random.randint(4,7)
    },
    "Goblin": {
        "hp": 10,
        "dg": 5,
        "gd": 12
    },
    "Orc": {
        "hp": 35,
        "dg": 6,
        "gd": 12,
    },
    "Dark Knight": {
        "hp": 40,
        "dg": 10,
        "gd": 30
    },
    "Evil Wizard": {
        "hp": 60,
        "dg": 15,
        "gd": 100
    }
}

current_tile = map[y][x]
print(current_tile)
name_of_tile = biome[current_tile]["t"]
print(name_of_tile)
enemy_tile = biome[current_tile]["e"]
print(enemy_tile)


def clear():
    os.system('clear')

def divide():
    print('++================================================================++')

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
        str(key)

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
        enemy = random.choice(e_list)
    else:
        enemy = "Evil Wizard"
    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["dg"]
    g = mobs[enemy]["gd"]


    while fight:
        clear()
        divide()
        print("A " + enemy + " wants to fight you!")
        divide()
        print(enemy + "'s HP: " + str(hp) + "/" + str(hpmax))
        print(hero_name + "'s HP: " + str(HP) + "/" + str(HP_MAX))
        print("POTIONS: " + str(POT))
        print("ELIXERS: " + str(ELX))
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
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + hero_name + ".")
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
        print("1, NEW GAME")
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, QUIT")
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
        
        if not standing and biome[map[y][x]]["e"]:
            if random.randint(0, 100) <= 30:
                fight = True
                battle()

        if play:
            divide()
            print("LOCATION: " + biome[map[y][x]]["t"])
            divide()
            print("NAME: " + hero_name)
            print("HP: " + str(HP) + "/" + str(HP_MAX))
            print("ATK: " + str(ATK))
            print("POTIONS: " + str(POT))
            print("ELIXERS: " +str(ELX))
            print("GOLD: " + str(GLD))
            print("COORDS: ", x, y)
            divide()
            if y > 0:
                print("1 - NORTH")
            if x < x_len:
                print("2 - EAST")
            if y < y_len:
                print("3 - SOUTH")
            if x > 0:
                print("4 - WEST")
            print("0 - SAVE AND QUIT")
            if POT > 0:
                print("5 - use POTION")
            if ELX > 0:
                print("6 - use ELIXER")
            if map[y][x] == "S" or map[y][x] == "K" or map[y][x] == "A":
                print("7 - ENTER")
            divide()

            dest = input("# ")

        if dest == "0":
            play = False
            menu = True
            save() #auto quit save
        
        #actions
        if dest == "1":
            if y > 0:
                y -= 1
                standing = False
        elif dest == "2":
            if x < x_len:
                x += 1
                standing = False
        elif dest == "3":
            if y < y_len:
                y += 1
                standing = False
        elif dest == "4":
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