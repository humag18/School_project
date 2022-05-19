from random import *
from Player import Player
from Game import Game
def menu():
    print("#--------------------------------------------#")
    print("#             Welcome to the game            #")
    print("#--------------------------------------------#")
    print("#          Chose your gaming setting         #")
    print("#                [0] 1 VS 1                  #")
    print("#                [1] 1 VS bot                #")
    print("#                [2] Show rank               #")
    print("#                [2] quit                    #")
    print("#                                            #")
    print("#--------------------------------------------#")

def game_mode():
    print("#--------------------------------------------#")
    print("#                                            #")
    print("#        Chose your game mode :              #")
    print("#            [0] Easy (PV : 20)              #")
    print("#            [1] Normal (PV : 10)            #")
    print("#            [2] Hardcore (PV : 5)           #")
    print("#            [3] Ultra Hardcore (PV : 1)     #")
    print("#                                            #")
    print("#--------------------------------------------#")

if __name__ == "__main__":
    setting = menu()
    choice = int(input(">> "))
    life = -1
    if choice == 0:
        setting = game_mode()
        
        while life < 0 or life > 4:
            try:                    
                life = int(input(">> "))
                # break
            except ValueError:
                print("Oops! That not a valid type try again...")
        name1 = input("Player 1's name >> ")
        name2 = input("Player 2's name >> ")
        if life == 0:
            print("The winner will recived 1 points")
            life = 20
        elif life == 1:
            print("The winner will recived 5 points")
            life = 10
        elif life == 2:
            print("The winner will recived 10 points")
            life = 5
        elif life == 3:
            print("The winner will recived 20 points")
            life = 1
    elif choice == 1:
        setting2 = game_mode()
        while True:
            try:                    
                life = int(input(">> "))
                break
            except ValueError:
                print("Oops! That not a valid type try again...")
        name1 = input("Player's name >> ")
        name2 = "bot"
        
        if life == 0:
            print("If you win, you will recived 1 points")
            name2 = "bot_nul"
            life = 20
        elif life == 1:
            print("If you win, you will recived 5 points")
            name2 = "bot_nul"
            life = 10
        elif life == 2:
            print("If you win, you will recived 10 points")
            name2 = "bot"
            life = 5
        elif life == 3:
            print("If you win, you will recived 20 points")
            name2 = "bot"
            life = 1
    elif choice >= 2:
        exit()
    p1 = Player(name = name1, life = life, monney = 10)
    p2 = Player(name = name2, life = life, monney = 10)
    g = Game(p1, p2)
    g.play()