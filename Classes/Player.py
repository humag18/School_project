from Classes.character.Character import Character
from Classes.character.Fighter import Fighter
from Classes.character.Tank import Tank
from Classes.character.Archer import Archer
from Classes.character.Goblins import Goblins
from Classes.character.Healer import Healer
from random import *
class Player: 

    def __init__(self, name, life, monney, direction = None, game = None, team = None):
        self.name = name
        self.life = life
        self.monney = monney
        self.direction = direction
        self.team = team or []
        self.game = game
        self.n_choice = 0
        self.line = 0

    @property
    def is_alive(self):
        return self.life > 0

    def get_hit(self, dammage):
        self.life -= dammage

    def new_character(self):
        classes = (Character, Fighter, Tank, Archer, Goblins, Healer)
        if self.name != "bot":
            print(f"{self.name}: Wich line would you place the new one (0-{self.game.nb_lines-1}) ? (enter if none)")
            line = input(">> ")
            if line != "":
                if 0 <= int(line) <= self.game.nb_lines-1:
                    choices = input(f"wich class would you want to invoke : (0 - {len(classes)-1})"
                                f"(enter to show price and order)\n>> ")
                    if choices == "":
                        choices = input(f"Enter your desired invocation : \n0- Framer : {Character.base_price}$"
                        f"\n1- Fighter : {Fighter.base_price}$ \n2- Tank : {Tank.base_price}$\n3- Archer : {Archer.base_price}$\n4- Goblins : {Goblins.base_price} \n5- Healer : {Healer.base_price}$\n>> ")
                    self.n_choice = int(choices)
                    if 0<= self.n_choice <= len(classes) - 1 and self.monney >= classes[int(choices)].base_price:
                        if self.direction == +1:
                            column = 0
                        else:
                            column = self.game.nb_columns-1
                        classes[self.n_choice](self, (int(line), column))
        elif self.name == "bot":
            print("It's the bot's turn...")
            bot_choices = randint(0, len(classes)-1)
            if self.monney >= classes[int(bot_choices)].base_price:
                line = randint(0, self.game.nb_lines-1)
                column = self.game.nb_columns-1
                classes[bot_choices](self, (int(line), column))
            
    
    def add_monney(self):
        self.monney+=0.5