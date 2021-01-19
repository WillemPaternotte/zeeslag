import random
import math
import os
import time 

def printScreen(invoer): #functie die het veld overzichtelijk print
    for item in invoer:
        for i in item:
            print(i, end=" ")
        print("")  # zodat de volgende line niet opzelfde line print

def maakBord(lengte):
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

def bordsize(): 
    lengte = input("Hoeveel bij hoeveel moet het bord groot zijn?: ")
    while not lengte.isnumeric():
        print("Kies een nummer")
        lengte = input("Hoeveel bij hoeveel moet het bord groot zijn?: ")
    lengte = int(lengte)
    while not(2 < lengte <= 24): #Maximale groot 24x24 want 24 letters in het alfabet kleiner dan 3x3 niet leuk
        print("De maximale grootte is 24x24")
        lengte = int(input("Hoeveel bij hoeveel moet het bord groot zijn?: "))
    return lengte

def plaatsSchepen(aantal, bord, bordgrootte):
    schepen = 0
    while schepen < aantal:
        x = random.randint(1, bordgrootte)
        y = random.randint(1, bordgrootte)
        while checkScheep(x, y, bord) == True:
            x = random.randint(1, bordgrootte)
            y = random.randint(1, bordgrootte)
        bord[y][x] = "x"
        schepen += 1

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

def checkGokVorm(bordgrootte, bord):
    invoer = str.upper(input("Gok een positie(Typ gok als de vorm A1): "))
    while not(len(invoer) == 2 and invoer[0].isalpha() and invoer[1].isnumeric() and ord(invoer[0]) - 64 <= bordgrootte and int(invoer[1]) <= bordgrootte) or bord[int(invoer[1])][ord(invoer[0]) - 64] == "~" or bord[int(invoer[1])][ord(invoer[0]) - 64] == "x": #checkt juiste input format en of de pos bestaat
        if  not(len(invoer) == 2 and invoer[0].isalpha() and invoer[1].isnumeric() and ord(invoer[0]) - 64 <= bordgrootte and int(invoer[1]) <= bordgrootte):
            print("foute input!")
        else:
            print("deze positie heb je al gegokt!")
        invoer = str.upper(input("Gok een positie(Typ gok als de vorm A1): "))
    return invoer

def raden(bordA, bordB, score, bordgrootte):
    gok = checkGokVorm(bordgrootte, bordB)
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

def save(data, bordA, bordB): # algemene save functie slaat alles op
    bestand = open("save.txt", "w")
    for item in data:
        bestand.write(str(item))
        bestand.write(",")
    bestand.write("\n")
    saveBord(bordA, bestand)
    saveBord(bordB, bestand)
    bestand.close()

def saveBord(bord, bestand): #write 1 bord op 1 line in een bestand
    for rij in bord:
        for item in rij:
            bestand.write(item)
            bestand.write(".")
        bestand.write(",")
    bestand.write("\n")

def Data(State,Size,Score, Schepen, Beurten): #verzameld alle data en zet het inn een lijstje
    data = []
    data.append(State)
    data.append(Size)
    data.append(Score)
    data.append(Schepen)
    data.append(Beurten)
    return data

def getVar(welke):
    bestand = open("save.txt", "r")
    dataTekst = bestand.readline()
    data = dataTekst.split(",")
    var = data[welke]
    bestand.close()
    return var

def getBord(welke, size):
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

def main(): #hoofdprogramma, verklaart eerst variabelen, daarna while loop met programma
    while True:
        if getVar(0) == "Game" and str.upper(input("Er is een save gevonden, om op deze save verder te spelen Druk: Y")) == "Y":
            bordgrootte = int(getVar(1))
            bordAschepen = getBord(1, bordgrootte)
            bordBspelen =  getBord(2, bordgrootte)
            score = int(getVar(2))
            schepen = int(getVar(3)) 
            beurten = int(getVar(4))
        else:
            bordgrootte = bordsize()
            bordAschepen = maakBord(bordgrootte)
            bordBspelen = maakBord(bordgrootte)
            schepen = math.floor(bordgrootte * (math.sqrt(bordgrootte)/2) -1)#geweldige formule die meestal werkt behalve bij 8
            score = 0
            beurten = 0
            plaatsSchepen(schepen, bordAschepen, bordgrootte)
        while not(score == schepen):
            overgeblevenSchepen = schepen - score
            os.system("cls" if os.name == "win32" else "clear") # ;)
            print("Er zijn nog", overgeblevenSchepen, "schepen over.")
            printScreen(bordBspelen)
            score = raden(bordAschepen, bordBspelen, score, bordgrootte)
            beurten +=1
            time.sleep(.75) #mag dit? kleine delay zorgt voor soepelere erveraring
            data = Data( "Game", bordgrootte, score, schepen, beurten)
            save(data, bordAschepen, bordBspelen)# saved spel aan het einde van beurt
        data = Data("Clear", bordgrootte, score, schepen, beurten)
        save(data, bordAschepen, bordBspelen)
        printScreen(bordBspelen)  
        print("gewonnen")
        input("druk enter om nog een keer te spelen!")

main()


