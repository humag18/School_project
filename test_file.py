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
n = 1

for i in rank:
    # for j in i:
    print(f"#{n} {i[0]}, with {i[1]}, pts")
    n+=1

new = "Jade"
pts2 = 30
tuples = (new, pts2)
rank.append(tuples)
rank.sort(key=lambda x: x[1], reverse=True)
print(rank)
f = open('ranking.txt', 'w+')
for i in rank:
    f.write(f"{i[0]} {i[1]}\n")

f.close()