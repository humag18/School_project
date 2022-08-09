from json import *
def new_score(player, pts):
    path = "./data.json"
    with open (path, "r", encoding = "utf-8") as data_file:
        data = load(data_file)
    data_file.close()
    new = {'playername' : player.capitalize(), 'pts' : pts}
    for i in data:
        if i['playername'] == player.capitalize():            
            data.remove(i)
            point = i['pts'] + new['pts']
            i['pts'] = point
            data.append(i)
            with open(path, "w", encoding = 'utf-8') as data_file1:
                dump(data, data_file1)
            data_file.close()
            exit()
    data.append(new)
    with open(path, 'w', encoding = 'utf-8') as data_file2:
        dump(data, data_file2)
    data_file.close()
    
    print("Updating data... Done")

def show_rank():
    path = "./data.json"
    with open (path, "r", encoding = "utf-8") as data_file:
        data = load(data_file)
    data_file.close()
    rank = sorted(data, key = lambda k: k['pts'], reverse = True)
    n = 0
    for i in rank:
        n+=1
        print(n, "#", i['playername'], "with", i["pts"], "points")