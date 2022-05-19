from Classes.character.Character import Character
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