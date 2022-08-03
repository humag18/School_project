from json import *
def new_score(player, pts):
    with open ('data.json', 'r', encoding = 'utf-8') as data_file:
        data = load(data_file)
    new = {'playername' : player, 'pts' : pts}
    for i in data:
        if i['playername'] == player:            
            data.remove(i)
            point = i['pts'] + new['pts']
            i['pts'] = point
            data.append(i)
            with open('data.json', 'w', encoding = 'utf-8') as data_file:
                dump(data, data_file)
            exit()
    data.append(new)
    with open('data.json', 'w', encoding = 'utf-8') as data_File:
        dump(data, data_file)
    
    print("Updating data... Done")

def show_rank(rank):
    n = 1
    rank.sort(key = lambda x: x[1], reverse = True)
    for i in rank:
        print(f"{i[0]} as {i[1]} points!")
        n+=1