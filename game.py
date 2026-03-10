# 2048 - Sprint 3
# Amin Torrisi
from tkinter import *
import random
import math


# la grille commence vide, on ajoutera 2 tuiles au hasard au lancement
grille = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

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
# retourne (a, b, c, d, deplacements, fusions)
def pack4(a,b,c,d):
    deplacements = 0
    fusions = 0
    # on met les valeurs non nulles dans une liste, puis on complete avec des zeros
    vals = [x for x in [a,b,c,d] if x != 0]
    # compter les deplacements (cases qui ont change de position)
    while len(vals) < 4:
        vals.append(0)
    # fusionner les paires egales de gauche a droite
    result = []
    i = 0
    while i < 4:
        if i < 3 and vals[i] != 0 and vals[i] == vals[i+1]:
            result.append(2 * vals[i])
            fusions += 1
            i += 2
        else:
            result.append(vals[i])
            i += 1
    while len(result) < 4:
        result.append(0)
    # compter les deplacements
    original = [a,b,c,d]
    for j in range(4):
        if result[j] != original[j]:
            deplacements += 1
    return result[0], result[1], result[2], result[3], deplacements, fusions

# cette fonction ajoute une tuile (2 ou 4) sur une case vide au hasard
def ajouter_tuile():
    # on cherche toutes les cases vides dans la grille
    cases_vides = []
    for line in range(4):
        for col in range(4):
            if grille[line][col] == 0:
                cases_vides.append((line, col))

    # si il reste au moins une case vide
    if len(cases_vides) > 0:
        # on choisit une case vide au hasard avec random.choice
        line, col = random.choice(cases_vides)

        # 90% de chance d'avoir un 2, 10% d'avoir un 4
        if random.randint(1, 10) == 1:
            grille[line][col] = 4
        else:
            grille[line][col] = 2

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
            grille[line][0], grille[line][1], grille[line][2], grille[line][3], dep, fus = pack4(a,b,c,d)

    elif touche == "Right":
        # vers la droite = on inverse, on tasse a gauche, on re-inverse
        for line in range(4):
            a,b,c,d = grille[line][3], grille[line][2], grille[line][1], grille[line][0]
            grille[line][3], grille[line][2], grille[line][1], grille[line][0], dep, fus = pack4(a,b,c,d)

    elif touche == "Up":
        # vers le haut on fait pareil mais avec les colonnes
        for col in range(4):
            a,b,c,d = grille[0][col], grille[1][col], grille[2][col], grille[3][col]
            grille[0][col], grille[1][col], grille[2][col], grille[3][col], dep, fus = pack4(a,b,c,d)

    elif touche == "Down":
        # vers le bas on inverse les colonnes
        for col in range(4):
            a,b,c,d = grille[3][col], grille[2][col], grille[1][col], grille[0][col]
            grille[3][col], grille[2][col], grille[1][col], grille[0][col], dep, fus = pack4(a,b,c,d)

    # on ajoute une nouvelle tuile apres chaque deplacement
    ajouter_tuile()

    # on met a jour l'affichage apres chaque deplacement
    display()

win.bind("<Key>", deplacement)

print(pack4(4,0,4,8))    # attendu: (8, 8, 0, 0,)
print(pack4(0,0,0,8))    # attendu: (8, 0, 0, 0,)

# on ajoute 2 tuiles au hasard pour commencer la partie
ajouter_tuile()
ajouter_tuile()

# on appelle display pour afficher la grille
display()

win.mainloop()
