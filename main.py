import os

#magic numbers
START_HP = 10
START_HP_MAX = 10
START_ATK = 1
START_POT = 0
START_ELX = 0
START_GLD = 5
START_X = 0
START_Y =0
STAT_LEN = 9

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

#map of the corrupted lands 5x5
map = [
    [";", ";", ".", ".", "."],
    [";", ";", ".", ".", "."],
    [".", ".", "A", ".", "."],
    [".", "T", ".", ".", "M"],
    ["T", "T", "T", "M", "M"]]

y_len = len(map) - 1
x_len = len(map[0]) - 1

biome = {
    ",": {
        "t": "PLAINS",
        "e": True},
    ".": {
        "t": "DESERT",
        "e": True},
    ";": {
        "t": "TALL GRASS",
        "e": True},
    "A": {
        "t": "CASTLE",
        "e": False},
    "M": {
        "t": "MOUNTAINS",
        "e": True},
    "T": {
        "t": "FOREST",
        "e": True}
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
        divide()

        dest = input("# ")

        if dest == "0":
            play = False
            menu = True
            save() #auto quit save
        
        if dest == "1":
            if y > 0:
                y -= 1
        elif dest == "2":
            if x < x_len:
                x += 1
        elif dest == "3":
            if y < y_len:
                y += 1
        elif dest == "4":
            if x > 0:
                x -= 1