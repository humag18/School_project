rank = []
a = 0
try:
    f = open('ranking.txt', 'r+')
    for x in f:
        # for i in x:
        a = x.split(" ")
        name = a[0]
        b = a[1]
        c = b.split("\n")
        pts = int(c[0])
        player = (name, pts)
        rank.append(player)
    f.truncate(0)
    f.close()
except FileNotFoundError:
    print("Oops! The file doesn't exist we are creating a new one")
    with open('ranking.txt', 'x') as f:
        print("The file as been created!")
