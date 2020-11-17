import random

def printScreen(invoer): #functie die het veld overzichtelijk print
    for item in invoer:
        for i in item:
            print(i, end="|")
        print("")  # zodat de volgende line niet opzelfde line print

def maakBord(lengte):
    bord = []
    bord.append([])
    bord[0].append(" ")
    for i in range(0, lengte):
        bord[0].append( chr(65 + i) )
    bord[0].append(" ")
    for i in range(1, lengte+1):
        bord.append([])
        bord[i].append(i)
        for i2 in range(lengte):
            bord[i].append(0)
        bord[i].append(i)
    bord.append([])
    bord[lengte +1].append(" ")
    for i in range(0, lengte):
        bord[lengte +1].append( chr(65 + i) )
    bord[lengte +1].append(" ")
    return bord

def plaatsSchepen(aantal, bord, bordgrootte):
    schepen = 0
    while schepen < aantal:
        x = random.randint(1, bordgrootte)
        y = random.randint(1, bordgrootte)
        Yas = bord[y]
        while checkScheep(x, y, bord) == True:
            x = random.randint(1, bordgrootte)
            y = random.randint(1, bordgrootte)
            Yas = bord[y]
        Yas[x] = "x"
        schepen += 1

def checkScheep(x, y, bord):
    check = False
    y -= 1
    for i in range(3):
        Xas = x-1
        Yas = bord[y]
        while Xas - x < 2:
            if Yas[Xas] == "x":
                check = True
            Xas += 1
        y+=1
    return check

def raden(bord1):
    gok = str.upper(input("Gok een positie(Typ gok als de vorm A1): "))
    while not(gok[0].isalpha() and gok[1].isnumeric() and len(gok) == 2): #checkt juiste input format
        print("Foute input!")
        gok = str.upper(input("Gok een positie(Typ gok als de vorm A1): "))
    x = ord(gok[0]) - 64
    y = int(gok[1])
    Yas = bord1[y]
    if Yas[x] == "x":
        print("Raak!")


bordgrootte = int(input("bord groote"))
bord = maakBord(bordgrootte)
plaatsSchepen(5, bord, bordgrootte)
printScreen(bord)
raden(bord)
