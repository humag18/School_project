from Function.Ranking import *
class Game:
    def __init__(self, player0, player1, pts, nb_line = 6, nb_column = 15):
        self.players = [player0, player1]
        self.nb_lines = nb_line
        self.nb_columns = nb_column
        self.player_turn = 0
        player0.game = self
        player0.direction = 1
        player1.game = self
        player1.direction = -1
        self.pts = pts

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
        print(f"{self.oponent.name} is the winner!!")
        winner = new_score(self.oponent.name, self.pts)
        show = show_rank(winner)
 