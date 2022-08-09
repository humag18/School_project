from Classes.character.Character import Character
class Archer(Character):
    base_price = 4
    base_life = 2
    base_strength = 4

    @property
    def design(self):
            return self.color("A")

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
