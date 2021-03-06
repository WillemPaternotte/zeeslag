import random
import math
import os
import time 

if not os.path.exists("save.txt"):
    bestand = open("save.txt", "w+")#maakt een save file bij het open van het spel als deze nog niet bestaat
    bestand.close()

def printScreen(invoer): #functie die het veld overzichtelijk print
    for item in invoer:
        for i in item:
            print(i, end=" ")
        print("")  # zodat de volgende line niet opzelfde line print

def maakBord(lengte): #maakt een overzichtelijk bord met cijfers en letters langs de zijkanten
    bord = []
    lijnAlfabet(bord, lengte, 0)
    for i in range(1, lengte+1):
        bord.append([])
        nummersBord(bord, i)
        for i2 in range(lengte):
            bord[i].append("-")
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

def bordsize(): #vraagt hoegroot het bord moet zijn
    lengte = input("Hoeveel bij hoeveel moet het bord groot zijn?: ")
    while not lengte.isnumeric(): #controlleert input 
        print("Kies een nummer")
        lengte = input("Hoeveel bij hoeveel moet het bord groot zijn?: ")
    lengte = int(lengte)
    while not(2 < lengte <= 24): #Maximale groot 24x24 want 24 letters in het alfabet kleiner dan 3x3 niet leuk
        print("De maximale grootte is 24x24 en de minimale grootte is 3")
        lengte = int(input("Hoeveel bij hoeveel moet het bord groot zijn?: "))
    return lengte

def plaatsSchepen(gamemode, aantal, bord1, bord2, bordgrootte): #plaatst Schepen
    schepen = 0
    plaatsZelfSchepen(aantal, bord1, bordgrootte)
    if gamemode != "Y": #laat pc plaatsen als je singleplayer doer
        while schepen < aantal:
            x = random.randint(1, bordgrootte)
            y = random.randint(1, bordgrootte)
            while checkScheep(x, y, bord2) == True:
                x = random.randint(1, bordgrootte)
                y = random.randint(1, bordgrootte)
            bord2[y][x] = "x"
            schepen += 1
    else:
        plaatsZelfSchepen(aantal, bord2, bordgrootte)

def plaatsZelfSchepen(aantal, bord, bordgrootte): #functie die player schepen laat plaatsen
    schepen = 0
    print("Voor we kunnen spelen, moet je je schepen plaatsen!")
    while schepen < aantal: 
        printScreen(bord)
        pos = checkGokVorm(bordgrootte, bord, "Kies een positie(Typ keuze als de vorm A1): ")
        x = ord(pos[0]) - 64
        y = int(pos[1])
        while checkScheep(x, y, bord) == True: #check of schepen niet tegen elkaar staan
            print("Schepen mogen elkaar niet raken")
            pos = checkGokVorm(bordgrootte, bord, "Kies een positie(Typ keuze als de vorm A1): ")
            x = ord(pos[0]) - 64
            y = int(pos[1])
        bord[y][x] = "x"
        schepen +=1
        os.system("cls" if os.name == "nt" else "clear")   

def checkScheep(x, y, bord): #cehcked over er schepen in een 3x3 rond de gekoze positie zijn
    check = False
    y -= 1
    for i in range(3):
        Xas = x-1
        while Xas - x < 2:
            if bord[y][Xas] == "x":
                check = True
            Xas += 1
        y+= 1
    return check

def checkGokVorm(bordgrootte, bord, tekst): #zorgt voor juiste input
    invoer = str.upper(input(tekst))
    while not(len(invoer) == 2 and invoer[0].isalpha() and invoer[1].isnumeric() and ord(invoer[0]) - 64 <= bordgrootte and int(invoer[1]) <= bordgrootte) or bord[int(invoer[1])][ord(invoer[0]) - 64] == "~" or bord[int(invoer[1])][ord(invoer[0]) - 64] == "x": #checkt juiste input format en of de pos bestaat
        if  not(len(invoer) == 2 and invoer[0].isalpha() and invoer[1].isnumeric() and ord(invoer[0]) - 64 <= bordgrootte and int(invoer[1]) <= bordgrootte):
            print("foute input!")
        else:
            print("deze positie heb je al gekozen!")
        invoer = str.upper(input(tekst))
    return invoer

def raden(bordA, bordB, score, bordgrootte): #gok functie
    gok = checkGokVorm(bordgrootte, bordB, "Gok een positie(Typ gok als de vorm A1): ")
    x = ord(gok[0]) - 64
    y = int(gok[1])
    if bordA[y][x] == "x":
        bordB[y][x] = "x"
        print("Raak!")
        score +=1
    else:
        bordB[y][x] = "~"
        print("mis!")
    return score

def PCraden(bordA, bordB, score, bordgrootte): #gok functie voor de Computer
    x = random.randint(1, bordgrootte)
    y = random.randint(1, bordgrootte)
    while checkScheep(x, y, bordB) == True:
        x = random.randint(1, bordgrootte)
        y = random.randint(1, bordgrootte)
    if bordA[y][x] == "x":
        bordB[y][x] = "x"
        print("Raak!")
        score +=1
    else:
        bordB[y][x] = "~"
        print("mis!")
    return score

def save(data, bordAschepen, bordBspelen, bordBschepen, bordAspelen): # algemene save functie slaat alles op
    bestand = open("save.txt", "w")
    for item in data:
        bestand.write(str(item))
        bestand.write(",")
    bestand.write("\n")
    saveBord(bordAschepen, bestand)
    saveBord(bordBspelen, bestand)
    saveBord(bordBschepen, bestand)
    saveBord(bordAspelen, bestand)
    bestand.close()

def saveBord(bord, bestand): #write 1 bord op 1 line in een bestand
    for rij in bord:
        for item in rij:
            bestand.write(item)
            bestand.write(".")
        bestand.write(",")
    bestand.write("\n")

def Data(State,Size,ScoreA, ScoreB, Schepen, Gamemode): #verzameld alle data en zet het inn een lijstje
    data = []
    data.append(State)
    data.append(Size)
    data.append(ScoreA)
    data.append(ScoreB)
    data.append(Schepen)
    data.append(Gamemode)
    return data

def getVar(welke): #krijgt 1 variable uit de data
    bestand = open("save.txt", "r")
    dataTekst = bestand.readline()
    data = dataTekst.split(",")
    var = data[welke]
    bestand.close()
    return var

def getBord(welke, size): #krijgt 1 bord uit de save file
    print(size)
    bestand = open("save.txt", "r")
    loop = 0
    bordtekst = bestand.readline()
    while loop < welke:
        bordtekst = bestand.readline()
        loop +=1
    lijst = bordtekst.split(',')
    Bord = []
    for x in range(size+2):
        Bord.append([])
        Bord[x] = lijst[x].split(".")
    bestand.close()
    return Bord

def gameMode(): #vraagt game mode
    print("Wil je local mulitplayer spelen? Druk Y: \nStandaard gamemode is tegen de Computer.")
    mode = str.upper(input())
    return mode
    
def welkom():
    bestand = open("art.txt").read()
    print(bestand)
    time.sleep(5)
    os.system("cls" if os.name == "nt" else "clear")
    print("""Welkom bij zeeslag,
ik zal eerst even kort het spel uitleggen.
Geef als eerst op hoe groot je het bord zou willen hebben.
Daarna zal de computer een aantal schepen plaatsen afhankelijk van de bordgrootte. 
Het is aan jou de taak om alle schepen te raken met zo min mogelijk beurten. 
Om een schip te raken typ je de coördinaten van de locatie waarvan je denkt dat een schip zit. 
Succes! """)

def beurt(player,schepen, score, bordSpelen, bordSchepen, bordgrootte): #1 beurt
    overgeblevenSchepen = schepen - score
    os.system("cls" if os.name == "nt" else "clear") # ;)
    if player == "Y":
        print("Er zijn nog", overgeblevenSchepen, "schepen over.")
        printScreen(bordSpelen)
        score = raden(bordSchepen, bordSpelen, score, bordgrootte)
    else: 
        score = PCraden(bordSchepen, bordSpelen, score, bordgrootte)
    time.sleep(.75) #mag dit? kleine delay zorgt voor soepelere erveraring

    return score

def main(): #hoofdprogramma, verklaart eerst variabelen, daarna while loop met programma
    while True: #algemene loop, voor meerde potjes
        if getVar(0) == "Game" and str.upper(input("Er is een save gevonden, om op deze save verder te spelen Druk: Y")) == "Y":
            bordgrootte = int(getVar(1))
            bordAschepen = getBord(1, bordgrootte)
            bordBspelen =  getBord(2, bordgrootte)
            bordBschepen = getBord(3, bordgrootte)
            bordAspelen = getBord(4, bordgrootte)
            scoreA = int(getVar(2))
            scoreB = int(getVar(3))
            schepen = int(getVar(4)) 
            gamemode = "pc" #we gaan ervan uit dat na laden je tegen pc speelt, anders kan je valsspelen 
        else:# vraagt alle variabellen en maakt borden
            welkom()
            bordgrootte = bordsize()
            bordAschepen = maakBord(bordgrootte)
            bordBspelen = maakBord(bordgrootte)
            bordBschepen = maakBord(bordgrootte)
            bordAspelen = maakBord(bordgrootte)
            schepen = math.floor(bordgrootte * (math.sqrt(bordgrootte)/2) -1)#geweldige formule die meestal werkt behalve bij 8
            scoreA = 0
            scoreB = 0
            gamemode = gameMode()
            plaatsSchepen(gamemode, schepen, bordBschepen, bordAschepen, bordgrootte)
        while not(scoreB == schepen or scoreA == schepen):#gameloop
            print("Speler 1 is aan de Beurt")
            printScreen(bordAspelen)
            print("Je tegenstander heeft al ", scoreB, "Schepen geraakt")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
            scoreB = beurt("Y", schepen, scoreB, bordBspelen, bordAschepen, bordgrootte)
            data = Data("Game", bordgrootte, scoreA, scoreB, schepen, gamemode)
            save(data, bordAschepen, bordBspelen, bordBschepen, bordAspelen)
            if not(scoreB == schepen or scoreA == schepen):#tussen beurten checken of er is gewonnen
                if gamemode == "Y":
                    print("Speler 2 is aan de Beurt")
                    printScreen(bordBspelen)
                    print("Je tegenstander heeft al ", scoreA, "Schepen geraakt")
                time.sleep(3)
                os.system("cls" if os.name == "nt" else "clear")
                scoreA = beurt(gameMode, schepen, scoreA, bordAspelen, bordBschepen, bordgrootte)
                data = Data("Game", bordgrootte, scoreA, scoreB, schepen, gamemode)
                save(data, bordAschepen, bordBspelen, bordBschepen, bordAspelen)
        data = Data("Clear", bordgrootte, scoreA, scoreB, schepen, gamemode)
        save(data, bordAschepen, bordBspelen, bordBschepen, bordAspelen)  
        if scoreB == schepen:#kijkt wie wint en laat juiste tekst zien
            print("speler1 heeft gewonnen!")
            printScreen(bordBspelen)
        else:
            print("speler2 heeft gewonnen!")
            printScreen(bordAspelen)
        input("druk enter om nog een keer te spelen!")

main()


