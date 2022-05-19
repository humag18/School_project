class Ranking():
    rank =[]

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

    def new_score(self, winner, pts):
        if not winner in Ranking.rank:
            player = (winner, pts)
            Ranking.rank.append(player)
            print(f"Now {winner} you have {pts} points")
        else:
            for i in Ranking.rank:
                if i[0]==winner:
                    i[1] += pts
                    print(f"Now {i[0]} you have {i[1]} points")

        f = open('ranking.txt', 'w+')

                


    