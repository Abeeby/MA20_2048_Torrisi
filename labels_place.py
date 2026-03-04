# 2048 - Sprint 2
# Amin Torrisi
# a partir de l'exemple du prof labels_place.py
from tkinter import *

# je met toutes les valeurs dans la grille 
grille = [[2,    2,    8,   16],
          [32,   64,  128,  256],
          [512, 1024, 2048,   0],
          [0,     0,    0,    0]]

# chaque nombre a sa propre couleur
couleurs = {
    0: "#3d4a5c",
    2: "#e8edf2",
    4: "#dbeafe",
    8: "#22d3ee",
    16: "#2dd4bf",
    32: "#34d399",
    64: "#22c55e",
    128: "#fbbf24",
    256: "#fb923c",
    512: "#f87171",
    1024: "#f472b6",
    2048: "#a855f7",
}

# les labels seront stockes la dedans 
labels = [[None, None, None, None],
          [None, None, None, None],
          [None, None, None, None],
          [None, None, None, None]]

# ou commence la grille et l'espacement entre les cases
x0 = 25
y0 = 100
largeur = 95
hauteur = 95

# fenetre
win = Tk()
win.geometry("420x460")
win.title("2048")
win.configure(bg="#1e1b4b")

# titre du jeu
Label(win, text="2048", font=("Helvetica", 36, "bold"),
      fg="#a855f7", bg="#1e1b4b").place(x=160, y=20)

# on cree les labels vides et on les place dans la fenetre
for line in range(4):
    for col in range(4):
        labels[line][col] = Label(win, text="", width=6, height=3,
                                  font=("Helvetica", 22, "bold"),
                                  bg=couleurs[0])
        labels[line][col].place(x=x0 + largeur * col, y=y0 + hauteur * line)
        
#Approche d'une fonction pack4 qui tasse 4 valeurs a,b,c,d vers la gauche comme le jeu 2048
def pack4(a,b,c,d):
    # tasser les zeros vers la droite
    if a == 0:
        a,b,c,d = b,c,d,0
    if b == 0:
        b,c,d = c,d,0
    if c == 0:
        c,d = d,0
    # fusionner les paires egales
    if a == b:
        a,b,c,d = 2*a,c,d,0
    if b == c:
        b,c,d = 2*b,d,0
    if c == d:
        c,d = 2*c,0
    return a,b,c,d

# cette fonction met a jour l'affichage de la grille
def display():
    for line in range(4):
        for col in range(4):
            val = grille[line][col]

            # on affiche rien si la case vaut 0
            if val == 0:
                txt = ""
            else:
                txt = str(val)

            # les grands nombres ont besoin d'une police plus petite
            if val >= 1024:
                taille = 16
            else:
                taille = 24

            # on met a jour le label avec configure
            labels[line][col].configure(text=txt, bg=couleurs[val],
                                        font=("Helvetica", taille, "bold"), width=int(96/taille), height = int(48/taille))

# fonction qui gere les touches directionnelles
def deplacement(event):
    touche = event.keysym

    if touche == "Left":
        # on tasse chaque ligne vers la gauche
        for line in range(4):
            a,b,c,d = grille[line][0], grille[line][1], grille[line][2], grille[line][3]
            grille[line][0], grille[line][1], grille[line][2], grille[line][3] = pack4(a,b,c,d)

    elif touche == "Right":
        # vers la droite = on inverse, on tasse a gauche, on re-inverse
        for line in range(4):
            a,b,c,d = grille[line][3], grille[line][2], grille[line][1], grille[line][0]
            grille[line][3], grille[line][2], grille[line][1], grille[line][0] = pack4(a,b,c,d)

    elif touche == "Up":
        # vers le haut on fait pareil mais avec les colonnes
        for col in range(4):
            a,b,c,d = grille[0][col], grille[1][col], grille[2][col], grille[3][col]
            grille[0][col], grille[1][col], grille[2][col], grille[3][col] = pack4(a,b,c,d)

    elif touche == "Down":
        # vers le bas on inverse les colonnes
        for col in range(4):
            a,b,c,d = grille[3][col], grille[2][col], grille[1][col], grille[0][col]
            grille[3][col], grille[2][col], grille[1][col], grille[0][col] = pack4(a,b,c,d)

    # on met a jour l'affichage apres chaque deplacement
    display()

win.bind("<Key>", deplacement)

print(pack4(4,0,4,8))

# on appelle display pour afficher la grille
display()

win.mainloop()
