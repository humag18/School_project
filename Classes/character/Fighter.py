from Classes.character.Character import Character
class Fighter(Character):
    base_price = 2
    base_strength = 2

    @property
    def design(self):
        return self.color("F")

    def __str__(self):
        return f"Fighter ({self.price}$) -life : {self.life} -strength : {self.strength}"