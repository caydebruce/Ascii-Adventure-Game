import os

START_HP = 10
START_ATK = 1
START_GLD = 5

HP = START_HP
ATK = START_ATK
GLD =START_GLD

def clear():
    os.system('clear')

def divide():
    print('++================++')

def save():
    stats = [
        hero_name,
        str(HP),
        str(ATK),
        str(GLD),
    ]

    f = open("load.txt", "w")

    for item in stats:
        f.write(item + "\n")
    f.close()

run = True
menu = True
play = False
rules = False

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
            f = open("load.txt", "r")
            load_list = f.readlines()
            hero_name = load_list[0][:-1]
            HP = load_list[1][:-1]
            ATK = load_list[2][:-1]
            GLD = load_list[3][:-1]
            clear()
            print(hero_name, ": HP =", HP, "ATK =", ATK, "Gold =", GLD)
            print("welcome back, " + hero_name + "!")
            input("> ")
            menu = False
            play = True
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
        print(" 0 - SAVE AND QUIT")
        divide()

        dest = input("# ")

        if dest == "0":
            play = False
            menu = True
            save() #auto quit save