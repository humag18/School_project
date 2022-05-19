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
    
    def get_hit(self, damages):
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