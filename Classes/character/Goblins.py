from Classes.character.Character import Character
class Goblins(Character):
    base_strength = 3
    base_life = 3
    base_price = 3

    @property
    def design(self):
        return self.color("G")

    def atac(self):
        if self.position[1] == self.game.nb_columns -1 and self.direction == 1:
            self.enemy.get_hit(self.strength)
            self.player.team.remove(self)
            self.player.monney += 1

        elif self.position[1] == 0 and self.direction == -1:
            self.enemy.get_hit(self.strength)
            self.player.team.remove(self)
            self.player.monney += 1

        else:
            for character in self.enemy.team:
                if character.position == (self.position[0], self.position[1] + self.direction):
                    self.player.monney += character.get_hit(self.strength)*2