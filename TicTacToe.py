def initialiseGrille(grille):
    for i in range (0, 9):
        grille[i] = " "

def afficheGrille(grille):
    for i in range (0, 3):
        print(grille[i])
        print("|")
    print("\n-----------------------\n")
    for i in range (0, 3):
        print(grille[i+3])
        print("|")
        print("\n-----------------------\n")
    for i in range (0, 3):
        print(grille[i+6])
        print("|")
        
        
grille = [9]

initialiseGrille(grille)
afficheGrille(grille) 