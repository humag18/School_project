class Ranking():
    rank =[]
    def __init__(self, winner):
        self.winner = winner

    def ranking_showing(self):
        try:
            f = open('../ranking.txt', 'r+')
            for i in f:
                a = i.split(' ')
                name = a[0]
                b = a[1]
                c = b.split('\n')
                pts = c[0]
                player = (name, pts)
                Ranking.rank.append(player)

        except FileNotFoundError:
            print("Oops! the file doesn't exist.\nWe are creating a new one...")
            with open('../ranking.txt', 'x') as f:
                print("The file as been created!")

    