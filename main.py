import requests
import sys
from mojang import API
import os
import json
from pprint import pprint
import time

def getInfo(call):
        r = requests.get(call)
        return r.json()


os.system('cls')
print("=================")
print(">>>>STARTMENU<<<<")
print("1: Log In 2: Exit")
print("=================")

firstoption = int(input("Enter your option: "))

if firstoption == 1:
    os.system('cls')
    IGN = input("Enter your username: ")
    uuid = API().get_uuid(IGN)
    print(uuid)
    print(IGN)
    url = f"https://api.hypixel.net/player?key=23d2538e-cd2b-4ff0-91e0-634d64d65281&uuid={uuid}"
    print(url)

    data = getInfo(url)

    DuelCoins = data["player"]
    DuelCoins1 = DuelCoins["stats"]
    DuelCoins2 = DuelCoins1["Duels"]
    DuelCoins3 = DuelCoins2["coins"]

    while True:
        os.system('cls')
        def menu():
                    print("==============================")
                    print(">>>>>>>>>> GAME MENU <<<<<<<<<")
                    print("1: Bedwars 2: Skywars 3: Duels")
                    print("==============================")

        menu()

        option = int(input("Enter your option: "))

        if option == 1:
                print("comming soon")

        elif option == 2:
                print("comming soon")

        elif option == 3:
            print(DuelCoins3)


        else :
                    print("Please type a valid number !")
            
        os.system("pause")
elif firstoption == 2:
        print("GOODBYE")
        time.sleep(1)
        exit()

else :
        print("Please type a valid number !")




url = f"https://api.hypixel.net/player?key=23d2538e-cd2b-4ff0-91e0-634d64d65281&uuid={uuid}"

data = getInfo(url)

DuelCoins = data["player"]
DuelCoins1 = DuelCoins["stats"]
DuelCoins2 = DuelCoins1["Duels"]
DuelCoins3 = DuelCoins2["coins"]

while True:
    os.system('cls')
    def menu():
            print("==============================")
            print(">>>>>>>>>> GAME MENU <<<<<<<<<")
            print("1: Bedwars 2: Skywars 3: Duels")
            print("==============================")

    menu()

    option = int(input("Enter your option: "))

    if option == 1:
            print("comming soon")

    elif option == 2:
            print("comming soon")

    elif option == 3:
            print(DuelCoins3)


    else :
            print("Please type a valid number !")
      
    os.system("pause")