def new_score(player, pts):
    rank = []

    f = open('ranking.txt', 'r+')
    for i in f:
        a = i.split(' ')
        name = a[0]
        b = a[1]
        c = b.split("\n")
        point = c[0]
        players = (name, point)
        rank.append(players)
    f.close()
    lap = 0
    for i in rank:
        if i[0] == player:
            a = int(i[1])
            rank.remove(i)
            point = a+pts
            winner = (player, str(point))
            rank.append(winner)
        else:
            lap+=1

    if lap == len(rank):
         winner = (player, pts)
         rank.append(winner)
    # rank.sort(key = lambda x: x[1], reverse = True)


    f = open('ranking.txt', 'w+')
    f.truncate(0)
    for j in rank:
        name = j[0]
        pt = j[1]
        f.write(name + " " + str(pt) + "\n")
    return rank

def show_rank(rank):
    n = 1
    rank.sort(key = lambda x: x[1], reverse = True)
    for i in rank:
        print(f"{i[0]} as {i[1]} points!")
        n+=1