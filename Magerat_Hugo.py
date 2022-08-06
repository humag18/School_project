from random import *
from Classes.Player import Player
from Classes.Game import Game
from Function.Function_menu import *

if __name__ == "__main__":
    setting = menu()
    choice = int(input(">> "))
    life = -1
    if choice == 0:
        setting = game_mode()
        
        while not 0 <= life <= 3:
            try:                    
                life = int(input(">> "))
                # break
            except ValueError:
                print("Oops! That not a valid type try again...")
        name1 = input("Player 1's name >> ")
        if name1 == "bot":
            name1 = "John"
            print(f"Sorry your name is not valid {name1} is your new one")
        name2 = input("Player 2's name >> ")
        if name2 == "bot":
            name2 = "Jack"
            print(f"Sorry your name is not valid {name2} is your new one")
        if life == 0:
            print("The winner will recived 1 points")
            life = 20
            pts = 1
        elif life == 1:
            print("The winner will recived 5 points")
            life = 10
            pts = 5
        elif life == 2:
            print("The winner will recived 10 points")
            life = 5
            pts = 10
        elif life == 3:
            print("The winner will recived 20 points")
            life = 1
            pts = 20
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
            name2 = "bot"
            life = 20
            pts = 1
        elif life == 1:
            print("If you win, you will recived 5 points")
            name2 = "bot"
            life = 10
            pts = 5
        elif life == 2:
            print("If you win, you will recived 10 points")
            name2 = "bot"
            life = 5
            pts = 10
        elif life == 3:
            print("If you win, you will recived 20 points")
            name2 = "bot"
            life = 1
            pts = 20
    elif choice >= 2:
        exit()
    print(pts)
    p1 = Player(name = name1, life = life, monney = 10)
    p2 = Player(name = name2, life = life, monney = 10)
    g = Game(p1, p2, pts = pts)
    g.play()
