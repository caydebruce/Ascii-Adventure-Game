from functools import update_wrapper
import os
import random
import ast

#magic numbers
START_LVL = 1
START_HP = 12
START_HP_MAX = 12
START_MANA = 12
START_MANA_MAX = 12
START_STAM = 12
START_STAM_MAX = 12
START_POT = 4
START_ELX = 4
START_SOULS = 0
START_X = 11
START_Y = 11
START_SEEN_TILES = [(11, 11)]
SPAWN = [(11, 11)]
START_WEAPON = "Fists"
START_RING = "No Ring"
START_SPAWN = (11, 11)
STAT_LEN = 23



MAX_POT = 4
MAX_ELX = 4
STAM_RECOVER = 1
POT_HEAL = 10
ELX_HEAL = 10

#Grave vars
GRAVE = [-100, -100]
GRAVE_SOULS = 0

#Mob Globals
MOB = "Error"
MOB_HP = 0
MOB_HPMAX = 0
MOB_ATK = [-1, -2]
MOB_SOLS = 0
MOB_AC = 0
MOB_SE = []


#Hero starting stats
LVL = START_LVL
HP = START_HP
HP_MAX = START_HP_MAX
MANA = START_MANA
MANA_MAX = START_MANA_MAX
STAM = START_STAM_MAX
STAM_MAX = START_STAM_MAX
POT = START_POT
ELX = START_ELX
SOULS = START_SOULS
x = START_X
y = START_Y
SEEN_TILES = START_SEEN_TILES
operating_system = ""
WEAPON = START_WEAPON
RING = START_RING
WEAPON_STASH = [START_WEAPON]
RING_STASH = [START_RING]
SPAWN = START_SPAWN

#Game starting variables
LVL_COST = 10
run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
speak = False
boss = False
select = False
bridge_1 = False
cast_menu = False
attack_menu = False
hiding = False

#map of the corrupted lands
map = [
    list("```````````````````````"),
    list("`.....................`"),
    list("`.....................`"),
    list("`.....................`"),
    list("`.....................`"),
    list("`.....................`"),
    list("`.....................`"),
    list("`.....................`"),
    list("`.....................`"),
    list("`.....................`"),
    list("`########rrrr.........`"),
    list("`ssssssgr..Hr.........`"),
    list("`ssssssr,r..r.........`"),
    list("`Hsssrr,,,,rr.........`"),
    list("`sssr,,,,r,~..........`"),
    list("`ssr/H,r...~..........`"),
    list("`//////r,..~..........`"),
    list("`r//r//r,..~..........`"),
    list("`TTT////...~..........`"),
    list("`TTTTTTTTTT~..........`"),
    list("`###TTTTTTT~..........`"),
    list("`A_#TTTTTTT~..........`"),
    list("```````````````````````")]

y_len = len(map) - 1
x_len = len(map[0]) - 1

t_norm = "\033[0m"
t_gray = "\033[90m"
t_red = "\033[91m"
t_green = "\033[32m"
t_yellow = "\033[93m"

biome = {
    "s": {
        "d": t_green + "." + t_norm,
        "t": "SWAMP",
        "e": 75,
        "m": ["Swamp Rot Wretch", "Swamp Rot Skeleton"],
        "w": True
    },
    "g": {
        "d": t_red + "&" + t_norm,
        "t": "CHALLENGE THE GREEN HOLY KNIGHT",
        "e": 100,
        "m": ["Green Cursed Knight"],
        "w": True
    },
    "r": {
        "d": t_gray + "#" + t_norm,
        "t": t_gray + "RUINS" + t_norm,
        "e": 0,
        "m": ["Error"],
        "w": False
    },
    "H": {
        "d": "H",
        "t": "HIDEOUT",
        "e": 0,
        "m": ["Error"],
        "w": True
    },
    "`": {
        "d": " ",
        "t": "\033[2mWORLDS EDGE\033[0m",
        "e": 0,
        "m": ["Error"],
        "w": False
    },
    "_": {
        "d": "\033[2m_\033[0m",
        "t": "PATH",
        "e": 3,
        "m": ["Bandit"],
        "w": True
    },
    "#": {
        "d": "\033[2m#\033[0m",
        "t": "\033[2mWALL\033[0m",
        "e": 0,
        "m": ["Error"],
        "w": False
    },
    "~": {
        "d": "\033[2m~\033[0m",
        "t": "\033[2mRIVER\033[0m",
        "e": 0,
        "m": ["Error"],
        "w": False
    },
    ",": {
        "d": "\033[2m,\033[0m",
        "t": "PLAINS",
        "e": 33,
        "m": ["Skeleton", "Scavenger"],
        "w": True
    },
    ".": {
        "d": "\033[2m.\033[0m",
        "t": "DESERT",
        "e": 75,
        "m": ["Skeleton"],
        "w": True
    },
    "/": {
        "d": "\033[2m/\033[0m",
        "t": "TALL GRASS",
        "e": 30,
        "m": ["Skeleton", "Bandit", "Scavenger", "Scavenger"],
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
        "e": 0,
        "m": ["Error"],
        "w": True
    },
    "T": {
        "d": "\033[2mT\033[0m",
        "t": "FOREST",
        "e": 75,
        "m": ["Skeleton", "Forest Sentinel", "Forest Sentinel"],
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

weapons = {
    "No Weapon": {
        "name1": "None",
        "atk1": ["none"],
        "acc1": 100,
        "cost1": 0,
    },
    "Fists": {
        "name1": "PUNCH",
        "atk1": ["basic", 1],
        "acc1": 100,
        "cost1": 0,
    },
    "Bone Club": {
        "name1": "STRIKE",
        "atk1": ["basic", 2],
        "acc1": 90,
        "cost1": 0,
    },
    "Damascus Steel Sword": {
        "name1": "SLASH",
        "atk1": ["basic", 16],
        "acc1": 100,
        "cost1": 0,
        "name2": "HEAVY SLASH",
        "atk2": ["basic", 30],
        "acc2": 100,
        "cost2": 10,
    },
    "Swamp Rot Sword": {
        "name1": "SLASH",
        "atk1": ["basic", 7],
        "acc1": 100,
        "cost1": 1,
        "name2": "HEAVY SLASH",
        "atk2": ["basic", 10],
        "acc2": 100,
        "cost2": 6,
    },
    "Steel Sword": {
        "name1": "SLASH",
        "atk1": ["basic", 8],
        "acc1": 100,
        "cost1": 0,
        "name2": "HEAVY SLASH",
        "atk2": ["basic", 14],
        "acc2": 100,
        "cost2": 6,
    },
     "Iron Sword": {
        "name1": "SLASH",
        "atk1": ["basic", 8],
        "acc1": 100,
        "cost1": 0,
        "name2": "HEAVY SLASH",
        "atk2": ["basic", 10],
        "acc2": 100,
        "cost2": 3,
    },
    "Rusty Sword": {
        "name1": "SLASH",
        "atk1": ["basic", 3],
        "acc1": 90,
        "cost1": 0,
        "name2": "HEAVY SLASH",
        "atk2": ["basic", 5],
        "acc2": 100,
        "cost2": 3,
    },
    "Dual Rapier": {
        "name1": "SLASH",
        "atk1": ["basic", 3],
        "acc1": 75,
        "cost1": 0,
        "name2": "DOUBLE SLASH",
        "atk2": ["double", 3, 100, 2, 75, 1], #[move, dmg, acc, dmg2, acc2, combo dmg]
        "acc2": 100,
        "cost2": 3
    },
    "The Gideon": {
        "name1": "EARTH SHATTER",
        "atk1": ["stager", 12, 5],
        "acc1": 100,
        "cost1": 5,
        "name2": "RECOVER STAM",
        "atk2": ["recover", 0, "s", 5],
        "acc2": 100,
        "cost2": 0
    },
    "Dagger": {
        "name1": "SLASH",
        "atk1": ["basic", 4],
        "acc1": 75,
        "cost1": 0,
        "name2": "STAB",
        "atk2": ["basic", 6],
        "acc2": 90,
        "cost2": 1
    },
    "Cursed Vine Whip": {
        "name1": "WHIP",
        "atk1": ["basic", 5],
        "acc1": 75,
        "cost1": 0,
        "name2": "CONSTRICT",
        "atk2": ["lifesteal", 6, 1], #name dmg heal
        "acc2": 90,
        "cost2": 1
    }
}

rings = {
    "No Ring": {
    },
    "Swamp Rot Ring": {
        "name1": "LESSER HEAL",
        "spell1": ["heal", 8],
        "cost1": 5,
        "name2": "POISON",
        "spell2": ["poison", 3, 10],
        "cost2": 9,
    },
    "Taran's Ring": {
        "name1": "LESSER HEAL",
        "spell1": ["heal", 8],
        "cost1": 5,
        "name2": "FLAME",
        "spell2": ["flame", 5, 10],
        "cost2": 7,
    },
    "Worshipper's Ring": {
        "name1": "HEAL",
        "spell1": ["heal", 10],
        "cost1": 12,
    },
    "Emerald Ring" : {
        "name1": "LESSER HEAL",
        "spell1": ["heal", 5],
        "cost1": 3,
        "name2": "HEAL",
        "spell2": ["heal", 8],
        "cost2": 4,
        "name3": "LIFE STEAL",
        "spell3": ["lifesteal", 12, 6], #name, dmg, heal
        "cost3": 8,
    }
}

mobs = {
    "Error": {
        "hp": [1],
        "dg": [1],
        "ac": [1],
        "sl": [1],
        "rn": [100],
        "ef": ["none"],
        "dp": []
    },
    "Swamp Rot Wretch": {
        "hp": [17,18,20],
        "dg": [7,8,9],
        "ac": [90],
        "sl": [20],
        "rn": [50],
        "ef": ["poison"],
        "dp": [("Swamp Rot Ring", "r", 80)]
    },
    "Swamp Rot Skeleton": {
        "hp": [12],
        "dg": [4,4,5],
        "ac": [75],
        "sl": [12,13,14],
        "rn": [100],
        "ef": ["poison"],
        "dp": [("Swamp Rot Sword", "w", 100)]
    },
    "Green Cursed Knight": {
        "hp": [30],
        "dg": [10],
        "ac": [100],
        "sl": [50],
        "rn": [0],
        "ef": ["lifesteal", 2],
        "dp": [("Cursed Vine Whip", "w", 100), ("Emerald Ring", "r", 100)]
    },
    "Bandit": {
        "hp": [12],
        "dg": [3,4,4],
        "ac": [90],
        "sl": [15],
        "rn": [10],
        "ef": ["steal", 3],
        "dp": [("Dagger", "w", 20)]
    },
    "Skeleton": {
        "hp": [5,5,5,3,6,4],
        "dg": [2, 4],
        "ac": [60],
        "sl": [3,4,5],
        "rn": [100],
        "ef": ["none"],
        "dp": [("Bone Club", "w", 100), ("Worshipper's Ring", "r", 10)]
    },
    "Scavenger": {
        "hp": [7,7,7,8,9],
        "dg": [4, 5],
        "ac": [60],
        "sl": [5,5,6,10],
        "rn": [90],
        "ef": ["none"],
        "dp": [("Rusty Sword", "w", 50), ("Taran's Ring", "r", 10), ("Dual Rapier", "w", 50)]
    },
    "Forest Sentinel": {
        "hp": [20],
        "dg": [8,8,8,14],
        "ac": [70],
        "sl": [20,22,22,24,27],
        "rn": [50],
        "ef": ["lifesteal", 1],
        "dp": [("Iron Sword", "w", 20)]
    },
    "Evil Wizard": {
        "hp": [100],
        "dg": [15],
        "ac": [100],
        "sl": [100],
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

def header():
    print("NAME: " + hero_name + " | LEVEL: " + str(LVL) + " | LOCATION: " + biome[map[y][x]]["t"])

def stam_use():
    global POT, ELX, SOULS, x, y, STAM, HP, MANA, fight, GRAVE, GRAVE_SOULS

    STAM -= 1
    if STAM < 0:
        fight = False
        GRAVE = [x, y]
        GRAVE_SOULS = int(SOULS / 2)
        clear()
        divide()
        print("YOU DIED FROM EXHAUSTION!")
        divide()
        x = SPAWN[0]
        y = SPAWN[1]
        SOULS = 0
        ELX = 0
        POT = 0
        STAM = STAM_MAX
        MANA = MANA_MAX
        HP = HP_MAX
        input("> ")
        clear()

def save():
    stats = [
        hero_name,
        str(LVL),
        str(HP),
        str(HP_MAX),
        str(MANA),
        str(MANA_MAX),
        str(STAM),
        str(STAM_MAX),
        str(POT),
        str(ELX),
        str(SOULS),
        str(x),
        str(y),
        str(SEEN_TILES),
        str(key),
        str(operating_system),
        str(WEAPON),
        str(RING),
        str(WEAPON_STASH),
        str(RING_STASH),
        str(GRAVE),
        str(GRAVE_SOULS),
        str(SPAWN)
    ]

    f = open("load.txt", "w")

    for item in stats:
        f.write(item + "\n")
    f.close()

def heal(amount):
    global HP
    
    temp = amount
    if HP + amount < HP_MAX:
        HP += amount
    else:
        temp = HP_MAX - HP
        HP = HP_MAX
    print(str(temp) + " added to " + hero_name + "'s HP.")
    print(hero_name + "'s" + " HP has been increased to " + str(HP) + "!")

def mana_heal(amount):
    global MANA

    temp = amount
    if MANA + amount < MANA_MAX:
        MANA += amount
    else:
        temp = MANA_MAX - MANA
        MANA = MANA_MAX
    print(str(temp) + " added to " + hero_name + "'s MANA.")
    print(hero_name + "'s" + " MANA has been increased to " + str(MANA) + "!")

def recover(amount):
    global STAM

    if STAM + amount < STAM_MAX:
        STAM += amount
    else:
        STAM = STAM_MAX

def mob_effect(effect):
    global HP, POT, ELX, SOULS, HP_MAX, MOB_HP, MOB_HPMAX

    if effect == "none":
        pass
    elif effect == "steal":
        stolen = mobs[MOB]["ef"][1]
        if stolen <= SOULS:
            SOULS -= stolen
            print(MOB + " stole " + str(stolen) + " SOULS from you!")
        else:
            SOULS = 0
            print(MOB + " stole all of your of your SOULS!")

    elif effect == "fireball":
        print(MOB + " cast a FIREBALL and did 15 extra damage to " + hero_name + "!")
        HP -= 10
    
    elif effect == "lifesteal":
        curse = mobs[MOB]["ef"][1]
        HP -= curse
        if MOB_HP + curse > MOB_HPMAX:
            MOB_HP = MOB_HPMAX
        else:
            MOB_HP += curse
        print(MOB + " drained " + str(curse) + " of your HP and restored their health!")

    elif effect == "poison":
        HP -= 1
        print(hero_name + " has been POISONED!")

def draw_mob_stats():
    global MOB, MOB_HP, MOB_HPMAX, MOB_ATK
    print(MOB)
    for i in range(16):
        if i/16 < MOB_HP/MOB_HPMAX:
            print(t_red + "\u2588" + t_norm, end="")
        else:
            print(t_red + "_" + t_norm, end="")
    print("  HP: " + str(MOB_HP) + "/" + str(MOB_HPMAX))
    print("ATK: " + str(MOB_ATK[0]) + " - " + str(MOB_ATK[-1]))

def death_check():
    global fight, play, run, POT, ELX, SOULS, boss, x, y, MOB_SOLS, MOB, cast_menu, attack_menu, WEAPON_STASH, RING_STASH, HP, STAM, MANA, GRAVE, GRAVE_SOULS

    if HP <= 0:
        GRAVE = [x, y]
        GRAVE_SOULS = int(SOULS / 2)
        clear()
        divide()
        print("The " + MOB + " defeated " + hero_name + "...")
        divide()
        fight = False
        cast_menu = False
        attack_menu = False
        x = SPAWN[0]
        y = SPAWN[1]
        SOULS = 0
        ELX = 0
        POT = 0
        HP = HP_MAX
        MANA = MANA_MAX
        STAM = STAM_MAX
        print("YOU DIED")
        input("> ")
        clear()
        print(str(random.randint(18, 45)) + " years later...")
        input("> ")
        clear()
        
    if MOB_HP <= 0:
        divide()
        clear()
        print(hero_name + " defeated the " + MOB + "!")
        divide()
        fight = False
        cast_menu = False
        attack_menu = False
        SOULS += MOB_SOLS
        print("You aquired " + str(MOB_SOLS) + " SOULS from the " + MOB + "!")
        
        drop_list = mobs[MOB]["dp"]
        for i in drop_list:
            if random.randint(1,100) < i[2]:
                if i[1] == "w" and i[0] not in WEAPON_STASH:
                    WEAPON_STASH.append(i[0])
                    print("You found a " + i[0] + "! - Equip it at any Hideout location.")
                if i[1] == "r" and i[0] not in RING_STASH:
                    RING_STASH.append(i[0])
                    print("You found a " + i[0] + "! - Equip it at any Hideout location.")

        if MOB == "Evil Wizard":
            print("Congratulations! You've defeated the Evil Wizard!")
            print("You have finished the game!")
            boss = False
            play = False
            run = False
        input("> ")
        clear()

def cast(spell):
    global HP, MANA, STAM, WEAPON, RING, MOB_HP, MOB_HPMAX, MOB_ATK, MOB_SOLS, MOB_AC, MOB

    if spell[0] == "heal":
        if HP + spell[1] < HP_MAX:
            HP += spell[1]
        else:
            HP = HP_MAX
        print(hero_name + "'s" + " HP has been increased to " + str(HP) + "!")

    if spell[0] == "flame":
        MOB_HP -= spell[1]
        MOB_AC = MOB_AC * ((100 - spell[2]) / 100)
        print(hero_name + " did " + str(spell[1]) + " damage to " + MOB + " with their spell!")
        print(MOB + "'s accuracy has been decreased by " + str(spell[2]) + "%!")
    
    if spell[0] == "poison":
        MOB_HP -= spell[1]
        for i in MOB_ATK:
            MOB_ATK[i] = int(MOB_ATK[i] * ((100 - spell[2]) /100))
        print(hero_name + " did " + str(spell[1]) + " damage to " + MOB + " with their spell!")
        print(MOB + "'s attacks have been decreased by " + str(spell[2]) + "%!")

def attack(move):
    global HP, MANA, STAM, WEAPON, RING, MOB_HP, MOB_HPMAX, MOB_ATK, MOB_SOLS, MOB_AC, MOB

    if move[0] == "none":
        pass

    if move[0] == "basic":
        MOB_HP -= move[1]
        print(hero_name + " dealt " + str(move[1]) + " damage to the " + MOB + ".")
    
    if move[0] == "double":
        hit1 = random.randint(1,100) < move[2]
        hit2 = random.randint(1,100) < move[4]
        if hit1:
            MOB_HP -= move[1]
            print(hero_name + " dealt " + str(move[1]) + " damage to the " + MOB + " with first strike.")
        else:
            print(hero_name + " missed the first strike!")
        if hit2:
            MOB_HP -= move[3]
            print(hero_name + " dealt " + str(move[3]) + " damage to the " + MOB + " with second strike.")
        else:
            print(hero_name + " missed the second strike!")
        if hit1 and hit2:
            MOB_HP -= move[5]
            print(hero_name + " dealt " + str(move[5]) + " extra COMBO damage to the " + MOB + ".")

    if move[0] == "stager":
        MOB_AC = MOB_AC * ((100 - move[2]) / 100)
        MOB_HP -= move[1]
        print(hero_name + " did " + str(move[1]) + " damage to " + MOB + "!")
        print(MOB + "'s accuracy has been decreased by " + str(move[2]) + "%!")

    if move[0] == "recover":
        if move[2] == "s":
            recover(move[3])
        if move[2] == "m":
            mana_heal(move[2])
    
    if move[0] == "lifesteal":
        MOB_HP -= move[1]
        heal(move[2])
        print(hero_name + " stole " + str(move[1]) + " health from " + MOB + "!")

def battle():
    global fight, boss, HP, POT, ELX, SOULS, MANA, STAM, MOB_HP, MOB_HPMAX, MOB_ATK, MOB_SOLS, MOB_AC, MOB

    if not boss:
        MOB = random.choice(biome[map[y][x]]["m"])
    else:
        MOB = "Evil Wizard"

    MOB_HP = random.choice(mobs[MOB]["hp"])
    MOB_HPMAX = MOB_HP
    MOB_SOLS = random.choice(mobs[MOB]["sl"])
    MOB_AC = random.choice(mobs[MOB]["ac"])
    MOB_ATK = mobs[MOB]["dg"]
    boss = False

    def mob_attack():
        global HP

        mob_dmg = random.choice(mobs[MOB]["dg"])
        if random.randint(0,100) <= MOB_AC:
            HP -= mob_dmg
            print(MOB + " dealt " + str(mob_dmg) + " damage to " + hero_name + ".")
        else:
            print(MOB + " missed!")
        mob_effect(random.choice(mobs[MOB]["ef"]))

    clear()
    print("A " + MOB + " wants to fight you!")
    input("> ")

    if STAM <= 0:
        stam_use()

    while fight:

        clear()
        divide()
        draw_mob_stats()
        divide()  
        header()
        divide()
        draw_stats()
        divide()
        print("1 - ATTACK")
        print("2 - CAST")
        if POT > 0:
            print("3 - USE POTION (" + str(POT_HEAL) + "HP)")
        if ELX > 0:
            print("4 - USE ELIXER (" + str(ELX_HEAL) + "MANA)")
        print("Q - RUN!")
        divide()

        choice = input("# ")

        if choice == "1":

            attack_menu = True
            while attack_menu:
                clear()
                divide()
                draw_mob_stats()
                divide()  
                header()
                divide()
                draw_stats()
                divide()
                print("EQUIPPED WEAPON: " + WEAPON)
                divide()
                for i in range(1, 5):
                    try:
                        print(str(i) + " - " + weapons[WEAPON][("name" + str(i))] + " - (", end="")
                        print(str(weapons[WEAPON][("atk" + str(i))][1]) + " ATK) - (", end="")
                        print(str(weapons[WEAPON][("cost" + str(i))]) + " STAM)")
                    except:
                        pass
                print("Q - BACK")

                choice = input("# ")

                try:
                    if int(choice) in range(1,5):
                        if STAM >= weapons[WEAPON]["cost" + choice]:
                            STAM -= weapons[WEAPON]["cost" + choice]
                            if random.randint(1,100) < weapons[WEAPON]["acc" + choice]:
                                attack(weapons[WEAPON]["atk" + choice])
                            else:
                                print(hero_name + " missed!")
                            if MOB_HP > 0:
                                mob_attack()
                            attack_menu = False
                        else:
                            print("Not enough STAMINA!")
                        input("> ")
                except:
                    pass

                if choice.upper() == "Q":
                    attack_menu = False

        elif choice == "2":
            
            cast_menu = True
            while cast_menu:
                clear()
                divide()
                draw_mob_stats()
                divide()  
                header()
                divide()
                draw_stats()
                divide()
                print("EQUIPPED RING: " + RING)
                divide()
                for i in range(1,5):
                    try:
                        print(str(i) + " - " + rings[RING][("name" + str(i))] + " - (", end="")
                        print(str(rings[RING][("cost" + str(i))]) + " MANA)")
                    except:
                        pass
                print("Q - BACK")

                choice = input("# ")

                try:
                    if int(choice) in range(1,5):
                        if MANA >= rings[RING]["cost" + choice]:
                            MANA -= rings[RING]["cost" + choice]
                            cast(rings[RING]["spell" + choice])
                            if MOB_HP > 0:
                                mob_attack()
                            cast_menu = False
                        else:
                            print("Not enough MANA!")
                        input("> ")
                except:
                    pass

                if choice.upper() == "Q":
                    cast_menu = False
         
        elif choice == "3":
            if POT > 0:
                POT -= 1
                heal(POT_HEAL)
                if MOB_HP > 0:
                    mob_attack()
                input("> ")
            else:
                print("You are out of POTIONS!")
                input("> ")

        elif choice == "4":
            if ELX > 0:
                ELX -= 1
                mana_heal(ELX_HEAL)
                if MOB_HP > 0:
                    mob_attack()
                input("> ")
            else:
                print("You are out of ELIXERS!")
                input("> ")

        elif choice.upper() == "Q":
            if random.randint(1, 100) <= random.choice(mobs[MOB]["rn"]):
                print("You ran away from the " + MOB + " successfully!")
                input("> ")
                fight = False
            else:
                mob_attack()
                print("The " + MOB + " stopped you from fleeing!")
                input("> ")

        death_check()
 
def hideout():
    global hiding, WEAPON, RING, HP, MANA, STAM, SOULS, POT, ELX, LVL, MANA_MAX, HP_MAX, STAM_MAX

    while hiding:
        HP = HP_MAX
        MANA = MANA_MAX
        STAM = STAM_MAX
        clear()
        divide()
        header()
        divide()
        print("Welcome back to the hideout master " + hero_name)
        divide()
        draw_stats()
        divide()
        print("1 - WEAPON STASH - (" + str(len(WEAPON_STASH)) + " ITEMS)")
        print("2 - RING STASH   - (" + str(len(RING_STASH)) +  " ITEMS)")
        print("3 - CRAFT POTION - (10 SOULS)")
        print("4 - CRAFT ELIXER - (10 SOULS)")
        LVL_COST = (int(pow(float(LVL), 1.2)) + 10)
        print("5 - LEVEL UP HP   - (%d SOULS)" % LVL_COST)
        print("6 - LEVEL UP MANA - (%d SOULS)" % LVL_COST)
        print("7 - LEVEL UP STAM - (%d SOULS)" % LVL_COST)
        print("Q - EXIT HIDEOUT")

        choice = input("# ")

        if choice == "1":
            wep_stash_menu = True

            while wep_stash_menu:
                clear()
                divide()
                print("WEAPON STASH")
                divide()
                print("Which weapon would you like to equip?")
                divide()
                for wep in range(len(WEAPON_STASH)):
                    print(str(wep + 1) + " - " + WEAPON_STASH[wep] + " - (" + str(weapons[WEAPON_STASH[wep]]["atk1"][1])  + " ATK)")
                print("Q - BACK")
                
                wep_choice = input("# ").upper()

                if wep_choice == "Q":
                    wep_stash_menu = False

                if wep_choice.isnumeric():
                    if 0 < int(wep_choice) <= int(len(WEAPON_STASH)):
                        WEAPON = WEAPON_STASH[int(wep_choice) - 1]
                        print("You've equipped " + WEAPON)
                        input("> ")

        if choice == "2":
            rng_stash_menu = True

            while rng_stash_menu:
                clear()
                divide()
                print("RING STASH")
                divide()
                print("Which ring would you like to equip?")
                divide()
                for r in range(len(RING_STASH)):
                    print(str(r + 1) + " - " + RING_STASH[r])
                print("Q - BACK")

                r_choice = input("# ").upper()

                if r_choice == "Q":
                    rng_stash_menu = False
                
                if r_choice.isnumeric():
                    if 0 < int(r_choice) <= int(len(RING_STASH)):
                        RING = RING_STASH[int(r_choice) - 1]
                        print("You've equipped " + RING)
                        input("> ")
        
        if choice == "3":
            if POT == MAX_POT:
                print("You can't carry any more POTIONS!")
            else:
                if SOULS >= 10:
                    POT += 1
                    SOULS -= 10
                    print("You've bought a POTION!")
                else:
                    print("Not enough SOULS!")
            input("> ")
        
        if choice == "4":
            if ELX == MAX_ELX:
                print("You can't carry any more ELIXERS!")
            else:
                if SOULS >= 10:
                    ELX += 1
                    SOULS -= 10
                    print("You've bought an ELIXER!")
                else:
                    print("Not enough SOULS!")
            input("> ")
        
        if choice == "5" or choice == "6" or choice == "7":
            if SOULS >= LVL_COST:
                SOULS -= LVL_COST
                LVL += 1
                if choice == "5":
                    HP_MAX += 1
                    HP += 1
                    print("HP INCREASED TO %d" % HP)
                elif choice == "6":
                    MANA_MAX += 1
                    MANA += 1
                    print("MANA INCREASED TO %d" % MANA)
                elif choice == "7":
                    STAM_MAX +=1
                    STAM += 1
                    print("STAM INCREASED TO %d" % STAM)
                input("> ")
            else:
                print("Not enough SOULS!")
                input("> ")

        if choice.upper() == "Q":
            hiding = False
            print("Leaving the hideout...")
            input("> ")

def king():
    global speak, key

    while speak:
        clear()
        divide()
        print("Hello there, " + hero_name + "!")
        if weapons[WEAPON]["atk1"] < 10:
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
    if ((x + 1), (y + 1)) not in SEEN_TILES:      
        SEEN_TILES.append(((x + 1), (y + 1)))
    if ((x + 1), (y - 1)) not in SEEN_TILES:      
        SEEN_TILES.append(((x + 1), (y - 1)))
    if ((x - 1), (y + 1)) not in SEEN_TILES:      
        SEEN_TILES.append(((x - 1), (y + 1)))
    if ((x - 1), (y - 1)) not in SEEN_TILES:      
        SEEN_TILES.append(((x - 1), (y - 1)))
    if ((x + 2), y) not in SEEN_TILES:      
        SEEN_TILES.append(((x + 2), y))
    if ((x - 2), y) not in SEEN_TILES:      
        SEEN_TILES.append(((x - 2), y))
    if (x, (y + 2)) not in SEEN_TILES:      
        SEEN_TILES.append((x, (y + 2)))
    if (x, (y - 2)) not in SEEN_TILES:      
        SEEN_TILES.append((x, (y - 2)))

    header()
    divide()
    print("\u250C", end="")
    for i in range(14):
        print("\u2500", end="")
    print("\u2510")
    for r in range(y - 3,y + 4):
        print("\u2502", end="")
        for c in range(x - 3,x + 4):
            if r == y and c == x:
                print("@", end = " ")
            elif GRAVE[0] == c and GRAVE[1] == r:
                print("+", end=" ")
            elif 0 <= c <= x_len and 0 <= r <= y_len and (c, r) in SEEN_TILES:
                print(biome[map[r][c]]["d"], end = " ")
            else:
                print("  ", end="")
        print("\u2502")
    print("\u2514", end="")
    for i in range(14):
        print("\u2500", end="")
    print("\u2518")

def draw_stats():
    for i in range(16):
        if i/16 < HP/HP_MAX:
            print(t_red + "\u2588" + t_norm, end="")
        else:
            print(t_red + "_" + t_norm, end="")
    print("  HP:   " + str(HP) + "/" + str(HP_MAX))

    for i in range (16):
        if i/16 < MANA/MANA_MAX:
            print("\033[34m\u2588\033[0m", end="")
        else:
            print("\033[34m_\033[0m", end="")
    print("  MANA: " + str(MANA) + "/" + str(MANA_MAX))

    for i in range(16):
        if i/16 < STAM/STAM_MAX:
            print("\033[92m\u2588\033[0m", end="")
        else:
            print("\033[92m_\033[0m", end="")
    print("  STAM: " + str(STAM) + "/" + str(STAM_MAX))

    print("POTIONS: ", end="")
    for i in range(4):
        if i < POT:
            print(t_red + "() " + t_norm, end="")
        else:
            print(t_gray + "() " + t_norm, end="")
    print()
    print("ELIXERS: ", end="")
    for i in range(4):
        if i < ELX:
            print("\033[34m[]\033[0m ", end="")
        else:
            print(t_gray + "[]\033[0m ", end="")
    print()
    print("SOULS: " + str(SOULS))  
 
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
        print("3 - use POTION")
    if ELX > 0:
        print("4 - use ELIXER")
    if map[y][x] == "$" or map[y][x] == "K" or map[y][x] == "A" or map[y][x] == "H":
        print("E - ENTER")
    print("0 - SAVE AND QUIT")

while run:
    while menu:
        clear()
        divide()
        print("1 - NEW GAME")
        print("2 - LOAD GAME")
        print("3 - RULES")
        print("0 - QUIT")
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
            LVL = START_LVL
            HP = START_HP
            HP_MAX = START_HP_MAX
            MANA = START_MANA
            MANA_MAX = START_MANA_MAX
            STAM = START_STAM
            STAM_MAX = START_STAM_MAX
            POT = START_POT
            ELX = START_ELX
            SOULS = START_SOULS
            x = START_X
            y = START_Y
            SEEN_TILES = [START_SEEN_TILES]
            WEAPON = START_WEAPON
            RING = START_RING
            WEAPON_STASH = [START_WEAPON]
            RING_STASH = [START_RING]
            SPAWN = START_SPAWN

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
            print("Awake again... Do you remember you name?")
            hero_name = input("input name# ")
            if len(hero_name) == 0:
                hero_name = "Hero"
            print("Hmm... What a shame. I thought we finally made progress last time...")
            input("> ")
            menu = False
            play = True
        elif choice == "2":
            try:
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == STAT_LEN:
                    hero_name = load_list[0][:-1]
                    LVL = int(load_list[1][:-1])
                    HP = int(load_list[2][:-1])
                    HP_MAX = int(load_list[3][:-1])
                    MANA = int(load_list[4][:-1])
                    MANA_MAX = int(load_list[5][:-1])
                    STAM = int(load_list[6][:-1])
                    STAM_MAX = int(load_list[7][:-1])
                    POT = int(load_list[8][:-1])
                    ELX = int(load_list[9][:-1])
                    SOULS = int(load_list[10][:-1])
                    x = int(load_list[11][:-1])
                    y = int(load_list[12][:-1])
                    SEEN_TILES = ast.literal_eval(load_list[13])
                    key = bool(load_list[14][:-1])
                    operating_system = str(load_list[15][:-1])
                    WEAPON = str(load_list[16][:-1])
                    RING = str(load_list[17][:-1])
                    WEAPON_STASH = ast.literal_eval(load_list[18])
                    RING_STASH = ast.literal_eval(load_list[19])
                    GRAVE = ast.literal_eval(load_list[20])
                    GRAVE_SOULS = int(load_list[21][:-1])
                    SPAWN = ast.literal_eval(load_list[22])
                    clear()

                    print(hero_name, ": HP =", HP, "MANA = ", MANA, "STAM = ", STAM, "SOULS =", SOULS)
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
        elif choice == "0":
            clear()
            print("Game Quit Successfully")
            quit()

    while play:
        save() #autosave
        clear()

        #Grave Machanic
        if [x, y] == GRAVE:
            SOULS += GRAVE_SOULS
            clear()
            divide()
            print("You retrived %d SOULS!" % GRAVE_SOULS)
            divide()
            GRAVE = [-100,-100]
            GRAVE_SOULS = 0
            input("> ")

        
        #Hideout regen
        if map[y][x] == "H":
            HP = HP_MAX
            MANA = MANA_MAX
            STAM = STAM_MAX
            SPAWN = [x ,y]
        
        #Mob spawn mechanic
        if not standing and random.randint(1, 100) <= biome[map[y][x]]["e"]:
            fight = True
            battle()

        #Draw screen
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

        #actions
        if dest == "0":
            play = False
            menu = True
            save() #auto quit save
        
        if dest == "W" and y > 0 and biome[map[y - 1][x]]["w"]:
            y -= 1
            stam_use()
            standing = False
        elif dest == "D" and x < x_len and biome[map[y][x + 1]]["w"]:
            x += 1
            stam_use()
            standing = False
        elif dest == "S" and y < y_len and biome[map[y + 1][x]]["w"]:
            y += 1
            stam_use()
            standing = False
        elif dest == "A" and x > 0 and biome[map[y][x - 1]]["w"]:
            x -= 1
            stam_use()
            standing = False

        elif dest == "3":
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

        elif dest == "4":
            if ELX > 0:
                if MANA == MANA_MAX:
                    print("You are already at MAX MANA!")
                else:
                    mana_heal(ELX_HEAL)
                    ELX -= 1
            else:
                print("You are out of ELIXERS!")
            input("> ")
            standing = True

        elif dest == "E":
            if map[y][x] == "K":
                speak = True
                king()
            if map[y][x] == "A":
                boss = True
                academy()
            if map[y][x] == "H":
                hiding = True
                hideout()
        else:
            standing = True