class Player :

    def __init__(self, name, life, money):
        """
        PARAM : - name : str
                - life : float
                - money : float
        initialisate team to empty list, game and direction to None
        """
        # TODO

    @property
    def is_alive(self):
        # TODO
        return 0


    def get_hit(self, damages):
        """
        Take the damage to life
        PARAM : - damages : float
        """
        # TODO


    def new_character(self):
        """
        Ask to player where add a new Character,
        check if enough monney
        and create the new one
        """
        line = input(f"{self.name}: Wich line would you place the new one (0-{self.game.nb_lines-1}) ? (enter if none) ")
        if line != "":
            line = int(line)
            if 0<=line<=self.game.nb_lines-1 :
                if self.money >= Character.base_price :
                    column = 0 if self.direction == +1 else self.game.nb_columns-1
                    Character(self,(line,column))


class Game :

    def __init__(self,player0, player1, nb_lines=6,nb_columns=15):
        """
        PARAM : - player0 : Player
                - player1 : Player
                - nb_lines : float
                - nb_columns : float
        - update players' direction and game
        - initialisate player_turn to 0
        """
        # TODO


    @property
    def current_player(self):
        # TODO
        return 0

    @property
    def oponent(self):
        # TODO
        return 0

    @property
    def all_characters(self):
        # TODO
        return 0


    def get_character_at(self, position):
        """
        PARAM : - position : tuple
        RETURN : character at the position, None if there is nobody
        """
        # TODO


    def place_character(self, character, position):
        """
        place character to position if possible
        PARAM : - character : Character
                - position : tuple
        RETURN : bool to say if placing is done or not
        """
        # TODO



    def draw(self):
        """
        print the board
        """
        print(f"{self.players[0].life:<4}{'  '*self.nb_columns}{self.players[1].life:>4}")

        print("----"+self.nb_columns*"--"+"----")

        for line in range(self.nb_lines):
            print(f"|{line:>2}|", end="")
            for col in range(self.nb_columns):
                # TODO
                print(".", end=" ")
            print(f"|{line:<2}|")

        print("----"+self.nb_columns*"--"+"----")

        print(f"{self.players[0].money:<3}${'  '*self.nb_columns}${self.players[1].money:>3}")


    def play_turn(self):
        """
        play one turn :
            - current player can add a new character
            - current player's character play turn
            - oponent player's character play turn
            - draw the board
        """
        # TODO



    def play(self):
        """
        play an entire game : while current player is alive, play a turn and change player turn
        """
        # TODO






### PERSONNAGES ###
class Character :

    base_price = 1
    base_life = 5
    base_strength = 1 

    def __init__(self, player, position):
        """
        PARAM : - player : Player
                - position : tuple
        Set player to player in param.
        Set life, strength and price to base_life, base_strength and base_price.
        Place th character at the position
        If OK : add the current character to the player's team and take the price
        """

        self.player = player
        self.life = self.base_life
        self.strength = self.base_strength
        self.price = self.base_price

        ok = self.game.place_character(self, position)
        if ok :
            self.player.team.append(self)
            self.player.money -= self.price


    @property
    def direction(self):
        # TODO
        return 0

    @property
    def game(self):
        # TODO
        return 0

    @property
    def enemy(self):
        # TODO
        return 0

    @property
    def design(self):
        # TODO
        return 0


    def move(self):
        """
        the character move one step front
        """
        # TODO


    def get_hit(self, damages):
        """
        Take the damage to life. If dead, the character is removed from his team and return reward
        PARAM : damages : float
        RETURN : the reward due to hit (half of price if the character is killed, 0 if not)
        """
        # TODO


    def attack(self):
        """
        Make an attack :
            - if in front of ennemy's base : hit the base
            - if in front of character : hit him (and get reward)
        """
        # TODO


    def play_turn(self):
        """
        play one turn : move and attack
        """
        # TODO


    def __str__(self):
        """
        return a string represent the current object
        """
        # TODO





if __name__ == "__main__":
    print("Let's Play !!! ")
    # TODO
   
