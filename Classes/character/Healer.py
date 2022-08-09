from Classes.character.Character import Character
class Healer(Character):
    base_strength = 0
    base_life = 6
    base_price = 7

    @property
    def design(self):
        return self.color("H")

    def move(self):
        new_pos = (self.position[0], self.position[1] + self.direction)
        self.game.place_character(self, new_pos)
        if self.turn%2 == 0:
            self.player.life += 0.5
        self.turn+=1
