def menu():
    nb_columns = 43
    print("#"+nb_columns*"-"+"#")
    txt = "Welcome to the game"
    space = int((44-len(txt))/2)
    print("#"+space*" "+txt+space*" "+"#")
    print("#"+nb_columns*"-"+"#")
    txt = "Chose your settings"
    space = int((44-len(txt))/2)
    print("#"+space*" "+txt+space*" "+"#")
    txt = "[0] 1 VS 1"
    space = int(44-16-len(txt))
    print("#"+15*" "+txt+space*" "+"#")
    txt = "[1] 1 VS bot"
    space = int(44-16-len(txt))
    print("#"+15*" "+txt+space*" "+"#")
    txt = "[2] Show rank"
    space = int(44-16-len(txt))
    print("#"+15*" "+txt+space*" "+"#")
    txt = "[3] quit "
    space = int(44-16-len(txt))
    print("#"+15*" "+txt+space*" "+"#")
    print("#"+nb_columns*"-"+"#")


def game_mode():
    nb_columns = 43
    print("#"+nb_columns*"-"+"#")
    txt = "Chose your game mode"
    space = int((44-len(txt))/2)
    space1 = space-1
    print("#"+space*" "+txt+space1*" "+"#")
    print("#"+nb_columns*"-"+"#")
    txt = "[0] Easy (PV : 20)"
    space = int(44-11-len(txt))
    print("#"+10*" "+txt+space*" "+"#")
    txt = "[1] Normal (PV : 10)"
    space = int(44-11-len(txt))
    print("#"+10*" "+txt+space*" "+"#")
    txt = "[2] Hardcore (PV : 5)"
    space = int(44-11-len(txt))
    print("#"+10*" "+txt+space*" "+"#")
    txt = "[3] Ultra Hardcore (PV : 1)"
    space = int(44-11-len(txt))
    print("#"+10*" "+txt+space*" "+"#")
    print("#"+nb_columns*"-"+"#")