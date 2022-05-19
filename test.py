def atac_normal(self):
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

def atac(self):
        if self.position[1] == self.game.nb_columns -2 and self.direction == 1:
            self.enemy.get_hit(self.strength)

        elif self.position[1] == 1 and self.direction == -1:
            self.enemy.get_hit(self.strength)
            
            
        else:
            for character in self.enemy.team:
                if character.position == (self.position[0], self.position[1] + self.direction):
                    self.player.monney += character.get_hit(self.strength)