import random

monkey_list = ["dart_monkey", "boomerang_monkey", "bomb_shooter", "tack_shooter", "ice_monkey", "glue_gunner", "sniper_monkey", "monkey_sub", "monkey_buccaneer", "monkey_ace", "heli_pilot", "mortar_monkey", "dartling_gunner", "wizard_monkey", "super_monkey", "ninja_monkey" "alchemist", "druid", "banana_farm", "spike_factory", "monkey_village", "engineer"]
hero_list = ["quincy", "gwendolynn", "striker jones", "obynn_greenfoot", "geraldo", "pat_fusty", "ezili", "benjamin", "captain_churchill", "adora", "admiral_brickell", "ETN", "sauda", "psi"]

primary_gamemode = ["dart_monkey", "boomerang_monkey", "bomb_shooter", "tack_shooter", "ice_monkey", "glue_gunner"]
military_gamemode = ["sniper_monkey", "monkey_sub", "monkey_buccaneer", "monkey_ace", "heli_pilot", "mortar_monkey", "dartling_gunner"]
magic_gamemode = ["wizard_monkey", "super_monkey","ninja_monkey", "alchemist", "druid"]


def mainMenu():
    print("*** MENU ***")
    print("")
    print("e1- Primary gamemode randomizer")
    print("e2- Military gamemode randomizer")
    print("e3- Magic gamemode randomizer")
    print("e4- Normal randomizer")
    print("e5- Exit")
    print("")

    while True:

        selection = input("Enter a choice: ")

        if(selection == "e1"):
            primary_mode()
            break
        elif(selection == "e2"):
            military_mode()
            break
        elif(selection == "e3"):
            magic_mode()
            break
        elif(selection == "e4"):
            monkeys_3()
            break
        elif(selection == "e5"):
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 'e1'-'e5'")
            print("")

    
def primary_mode():
    randomized_prim_mode = random.choices(primary_gamemode, k=3)
    primary_mode_hero = random.choice(hero_list)
    print()
    print(randomized_prim_mode)
    print(primary_mode_hero)
    print()
    prim_reroll = input("Would you like to reroll your primary 'monkey' or 'hero': ").lower()
    if prim_reroll == "monkey":
        primary_mode2()
    elif prim_reroll == "hero":
        reroll_hero()
    else:
        print("Try again, you typed something wrong!")
    


def military_mode():
    randomized_military_mode = random.choices(military_gamemode, k=3)
    military_mode_hero = random.choice(hero_list)
    print()
    print(randomized_military_mode)
    print(military_mode_hero)
    print()
    military_reroll = input("Would you like to reroll your primary 'monkey' or 'hero': ").lower()
    if military_reroll == "monkey":
        military_mode2()
    elif military_reroll == "hero":
        reroll_hero()
    else:
        print("Try again, you typed something wrong!")

def magic_mode():
    randomized_magic_mode = random.choices(magic_gamemode, k=3)
    magic_mode_hero = random.choice(hero_list)
    print()
    print(randomized_magic_mode)
    print(magic_mode_hero)
    print()
    magic_reroll = input("Would you like to reroll your primary 'monkey' or 'hero': ").lower()
    if magic_reroll == "monkey":
        magic_mode2()
    elif magic_reroll == "hero":
        reroll_hero()
    else:
        print("Try again, you typed something wrong!")



def primary_mode2():
    randomized_prim_mode2 = random.choices(primary_gamemode, k=3)
    primary_mode_hero2 = random.choice(hero_list)
    print(randomized_prim_mode2)
    print(primary_mode_hero2)

def military_mode2():
    randomized_military_mode2 = random.choices(military_gamemode, k=3)
    military_mode_hero2 = random.choice(hero_list)
    print(randomized_military_mode2)
    print(military_mode_hero2)

def magic_mode2():
    randomized_magic_mode2 = random.choices(magic_gamemode, k=3)
    magic_mode_hero2 = random.choice(hero_list)
    print(randomized_magic_mode2)
    print(magic_mode_hero2)


def reroll_3monkeys():
    rerolled_3monkeys = random.choices(monkey_list, k=3)
    print(rerolled_3monkeys)

def reroll_hero():
    rerolled_hero = random.choice(hero_list)
    print(rerolled_hero)

def monkeys_3():
    randomized_3monkeys = random.choices(monkey_list, k=3)
    randomized_hero = random.choice(hero_list)
    print(f"here are your 3 random monkeys you have to use: {randomized_3monkeys}")
    print(f"Here is your randomized hero: {randomized_hero}\n")
    reroll = input("Do you want to re-roll your 'monkey' or 'hero'?: ").lower()
    while True:
        if reroll == "monkey":
            reroll_3monkeys()
            break
        elif reroll == "hero":
            reroll_hero()
            break
        else:
            print("You typed something wrong, try again!")

mainMenu()