import random

rij0 = [" ", "A", "B", "C"]
rij1 = ["1", "0", "0", "0"]
rij2 = ["2", "0", "0", "0"]
rij3 = ["3", "0", "0", "0"]
veld= [rij0, rij1, rij2, rij3]

def printScreen(invoer): #functie die het veld overzichtelijk print
    for item in invoer:
        for i in item:
            print(i, end="|")
        print("")  # zodat de volgende line niet opzelfde line print

def plaatsSchepen():
    x = random.randint(1, 3)
    y = random.randint(1, 3)
    Yas = veld[y]
    Yas[x] = "x"

def raden():
    gok = str.upper(input("Gok een positie(Typ gok als de vorm A1): "))
    while not(gok[0:1].isalpha() and gok[1:2].isnumeric() and len(gok) == 2): #checkt juiste input format
        print("Foute input!")
        gok = str.upper(input("Gok een positie(Typ gok als de vorm A1): "))
    x = ord(gok[0:1]) - 64
    y = int(gok[1:2])
    Yas = veld[y]
    if Yas[x] == "x":
        print("Raak!")

plaatsSchepen()
printScreen(veld)
raden()