import random
feld = 1
spieler = True
while feld <= 10:
    if feld == 10:
        einsoderzwei = 1
    else:
        einsoderzwei = random.randint(1,2)
    if spieler == True:
        if einsoderzwei == 1:
            print("X", end="")
            feld += 1
        else:
            print("XX", end="")
            feld += 2
        spieler = False
    else:
        if einsoderzwei == 1:
            print("O", end="")
            feld += 1
        else:
            print("OO", end="")
            feld += 2
        spieler = True
