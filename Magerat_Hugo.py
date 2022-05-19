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
        classes = (Character, Fighter, Tank, Mage)
        if self.name != "bot" and self.name != "bot_nul":
            print(f"{self.name}: Wich line would you place the new one (0-{self.game.nb_lines-1}) ? (enter if none)")
            line = input(">> ")
            if line != "":
                if 0 <= int(line) <= self.game.nb_lines-1:
                    choices = input(f"wich class would you want to invoke : (0 - {len(classes)-1})"
                                f"(enter to show price and order)\n>> ")
                    if choices == "":
                        choices = input(f"Enter your desired invocation : \n0- Framer : {Character.base_price}$"
                        f"\n1- Fighter : {Fighter.base_price}$ \n2- Tank : {Tank.base_price}$\n3- Magician : {Mage.base_price}$\n>> ")
                    self.n_choice = int(choices)
                    if 0<= self.n_choice <= len(classes) - 1 and self.monney >= classes[int(choices)].base_price:
                        if self.direction == +1:
                            column = 0
                        else:
                            column = self.game.nb_columns-1
                        classes[self.n_choice](self, (int(line), column))
        elif self.name == "bot_nul":
            print("It's the bot's turn...")
            bot_choices = randint(0, len(classes)-1)
            line = randint(0, self.game.nb_lines-1)
            column = self.game.nb_columns-1
            classes[bot_choices](self, (int(line), column))
            
    
    def add_monney(self):
        self.monney+=0.5


class Game:
    def __init__(self, player0, player1, nb_line = 6, nb_column = 15):
        self.players = [player0, player1]
        self.nb_lines = nb_line
        self.nb_columns = nb_column
        self.player_turn = 0
        player0.game = self
        player0.direction = 1
        player1.game = self
        player1.direction = -1

    @property
    def current_player(self):
        return self.players[self.player_turn]

    @property
    def oponent(self):
        if self.player_turn == 0:
            return self.players[self.player_turn + 1]
        else:
            return self.players[self.player_turn - 1]

    @property
    def all_characters(self):
        return self.players[0].team, self.players[1].team

    def get_character(self, position):
        for player in self.all_characters:
            for character in player:
                if position == character.position:
                    return character
        return None

    def place_character(self, character, position):
        board = []
        for line in range(self.nb_lines):
            for column in range(self.nb_columns):
                board.append((line, column))
        if position in board:
            if self.get_character(position) is None:
                character.position = position
                return True
            return False

    def draw(self):
        charac_list = []
        for player in self.all_characters:
            for character in player:
                charac_list.append(character.position)
        print(f"{self.players[0].life:<4}{'  '*self.nb_columns}{self.players[1].life:>4}")
        print("----"+self.nb_columns*"--"+"----")

        for line in range(self.nb_lines):
            print(f"|{line:>2}|", end="")
            for column in range(self.nb_columns):
                if (line, column) in charac_list:
                    for player in self.all_characters:
                        for character in player:
                            if character.position == (line, column):
                                print(f"{character.design}", end="")
                else:
                    print(".", end = " ")
            print(f"|{line:>2}|")

        print("----"+self.nb_columns*"--"+"----")

        print(f"{self.players[0].monney:>3}${'  '*self.nb_columns}${self.players[1].monney:>3}")
    
    def play_turn(self):
        for player in self.all_characters:
            for character in player:
                character.play_turn()
        self.current_player.new_character()
        self.draw()

    def play(self):
        while self.current_player.life > 0:
            self.play_turn()
            self.player_turn += self.current_player.direction
            self.current_player.add_monney()
    
class Character:
    base_price = 1
    base_life = 5
    base_strength = 1

    def __init__(self, player, position):
        self.player = player
        self.position = position
        self.life = self.base_life
        self.strength = self.base_strength
        self.price = self.base_price
        self.turn = 1

        x = self.game.place_character(self, position)
        if x is True:
            self.player.team.append(self)
            self.player.monney -= self.price

    @property
    def direction(self):
        return self.player.direction

    @property
    def game(self):
        return self.player.game

    @property
    def enemy(self):
        if self.player == self.game.current_player:
            return self.game.oponent
        else:
            return self.game.current_player

    @property
    def design(self):
        if self.direction == 1:
            return self.color(">")
        else:
            return self.color("<")

    def move(self):
        new_pos = (self.position[0], self.position[1] + self.direction)
        self.game.place_character(self, new_pos)
        #TODO
    
    def get_hit(self, damages):
        # print("class charcter methode get_hit")
        self.life -= damages
        if self.life <= 0:
            self.player.team.remove(self)
            return self.price/2
        return 0

    def atac(self):
        if self.position[1] == self.game.nb_columns -1 and self.direction == 1:
            self.enemy.get_hit(self.strength)
            self.player.team.remove(self)

        elif self.position[1] == 0 and self.direction == -1:
            self.enemy.get_hit(self.strength)
            self.player.team.remove(self)
            
        else:
            for character in self.enemy.team:
                if character.position == (self.position[0], self.position[1] + self.direction):
                    self.player.monney += character.get_hit(self.strength)

    def play_turn(self):
        self.move()
        self.atac()

    def color(self, txt):
        if self.player.direction == 1:
            return "\033[92m {}\033[00m".format(txt)
        else:
            return "\033[91m {}\033[00m".format(txt)

    def __str__(self):
        return f'Framer({self.price}$) -life : {self.life} -strength : {self.strength}'
        # return self

class Fighter(Character):
    base_price = 2
    base_strength = 2

    @property
    def design(self):
        if self.direction == 1:
            return self.color("F")
        else:
            return self.color("F")

    def __str__(self):
        return f"Fighter ({self.price}$) -life : {self.life} -strength : {self.strength}"

class Tank(Character):
    base_price = 3
    base_life = 10

    @property
    def design(self):
        if self.direction == 1:
            return self.color("T")
        else:
            return self.color("T")

    def __str__(self):
        return f"Tank ({self.price}$) -life : {self.life} -strength : {self.strength}"

    def move(self):
        if self.turn %2 == 0:
            new_pos = (self.position[0], self.position[1] + self.direction)
            self.game.place_character(self, new_pos)
        self.turn += 1

class Mage(Character):
    base_price = 4
    base_life = 4
    base_strength = 4

    @property
    def design(self):
        if self.direction == 1:
            return self.color("M")
        else:
            return self.color("M")

    def atac(self):
        if self.position[1] == self.game.nb_columns -2 and self.direction == 1:
            self.enemy.get_hit(self.strength)
        if self.position[1] == self.game.nb_columns - 1 and self.direction == 1:
            self.enemy.get_hit(self.strength)
            self.player.team.remove(self)
        elif self.position[1] == 1 and self.direction == -1:
            self.enemy.get_hit(self.strength)
        elif self.position[1] == 0 and self.direction == -1:
            self.enemy.get_hit(self.strength)
            self.player.team.remove(self)
            
        else:
            for character in self.enemy.team:
                if character.position == (self.position[0], self.position[1] + self.direction):
                    self.player.monney += character.get_hit(self.strength)


    def __str__(self):
        return f"Mage ({self.position[0]}$) -life : {self.life} -strength : {self.strength}"

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