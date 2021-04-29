

from IPython.display import clear_output


def spielfeld_anzeigen(spielfeld):
    clear_output()

    #spielfeld = ["X"] *10
    print(" "+spielfeld[1]+" | "+spielfeld[2]+" | "+spielfeld[3])
    print("-----------")
    print(" "+spielfeld[4]+" | "+spielfeld[5]+" | "+spielfeld[6])
    print("-----------")
    print(" "+spielfeld[7]+" | "+spielfeld[8]+" | "+spielfeld[9])

    
    
#spielfeld_anzeigen([])

#def spieler_eingabe():
   # markierung = ""
   # while not markierung == "X" or markierung == "O":
   #     input("Bitte wähle ein Feled zwischen 1-9: ").upper()
#checken
   # if markierung == "X":
    #    return "X"
    #else:
   #     return "O"

#spieler_eingabe()

def markierung_setzen(spielfeld, markierung, postion):
    spielfeld[position] = markierung


#checken ob jemand Gewonnen hat:

def sieg_check(spielfeld, markierung):
    sieg = ((spielfeld[1] and spielfeld[2] and spielfeld[3] == markierung) or
    (spielfeld[4] and spielfeld[5] and spielfeld[6] == markierung) or
    (spielfeld[7] and spielfeld[8] and spielfeld[9] == markierung) or
    (spielfeld[1] and spielfeld[4] and spielfeld[7] == markierung) or
    (spielfeld[2] and spielfeld[5] and spielfeld[8] == markierung) or
    (spielfeld[3] and spielfeld[6] and spielfeld[9] == markierung) or
    (spielfeld[1] and spielfeld[5] and spielfeld[9] == markierung)or
    (spielfeld[3] and spielfeld[5] and spielfeld[7] == markierung))
    return sieg


def beginner():
    return "Spieler 1"

#checken ob das Feld frei ist

def platz_frei(spielfeld, markierung):
    if spielfeld[position] == "":
        return

#checken ob das Spielfeld voll ist und ein unentschieden herrscht

def alle_felder_voll(spielfeld):
    for i in spielfeld:
        if platz_frei(spielfeld, markierung):
            return False
    return


def spielfeld_auswaelen(spielfeld):
    while postion not in [1,2,3,4,5,6,7,8,9].split() or not platz_frei(spielfeld, position):
        input("Spieler 1: Wähle ein Feld zwischen 1-9: ")
        return int(position)

def nochmal_spielen():
    return input("Möchtest du nochmal Spielen? Ja oder Nein: ").lower().startswith("j")

print("Willkommen in meinem Tic Tac Toe! ")



while True:
    feld = [""]*10
    zug = "Spieler 1"
    print(zug+" darf beginnen!")
    spiel_lauft = True
    
    if sieg_check(feld, spieler1)
