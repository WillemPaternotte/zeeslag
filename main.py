import random

def printScreen(invoer): #functie die het veld overzichtelijk print
    for item in invoer:
        for i in item:
            print(i, end="|")
        print("")  # zodat de volgende line niet opzelfde line print

def maakBord(lengte):
    bord = []
    lijnAlfabet(bord, lengte, 0)
    for i in range(1, lengte+1):
        bord.append([])
        nummersBord(bord, i)
        for i2 in range(lengte):
            bord[i].append(0)
        nummersBord(bord, i)
    lijnAlfabet(bord, lengte, lengte+1)
    return bord

def lijnAlfabet(bord, lengte, Pos): #maakt de rij aplhabet bij bord
    bord.append([])
    bord[Pos].append("  ") # zodat het alles op 1 kolom recht staat
    for i in range(0, lengte):
        bord[Pos].append( chr(65 + i) )
    bord[Pos].append("  ") # zodat het alles op 1 kolom recht staat

def nummersBord(bord, i): #Zodat de cijfers aan de rand van het bord mooi printen, anders staan lijnen na 10 breder door extra teken
    if i < 10:
        value = " " + str(i)
        bord[i].append(value)
    else:
        bord[i].append(i) 

def bordgrootte(): 
    lengte = int(input("Hoeveel bij hoeveel moet het bord groot zijn?: "))
    while not(lengte <= 24): #Maximale groot 24x24 want 24 letters in het alfabet 
        print("De maximale grootte is 24x24")
        lengte = int(input("Hoeveel bij hoeveel moet het bord groot zijn?: "))
    return lengte

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

def checkScheep(x, y, bord): #cehcked over er schepen in een 3x3 rond de gekoze positie zijn
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


bordgrootte = bordgrootte()
bordje = maakBord(bordgrootte)
plaatsSchepen(5, bordje, bordgrootte)
printScreen(bordje)
# raden(bord)
