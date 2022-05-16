class Player:
    def __init__(self, life):
        self.life = life

    # @prerty
    def is_alive(self):
        return self.life > 0

    def hit(self, dammage):
        print("coco")
        life = Player.is_alive(self)
        print (life,"YO")
        if life == True:
            self.life -= dammage
            print(self.life)
        
        elif life == "False":
            print("end game")

hugo = Player(12)
hugo.hit(1)