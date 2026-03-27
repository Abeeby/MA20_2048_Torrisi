# 2048 - Sprint 4
# Amin Torrisi
from tkinter import *
import random

# la grille commence vide, on ajoutera 2 tuiles au hasard au lancement
grille = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

# variable pour savoir si la partie est finie (perdu)
partie_finie = False

# variable pour savoir si on a deja affiche le message de victoire
deja_gagne = False

# le score du joueur
score = 0

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
    4096: "#7c3aed",
    8192: "#6d28d9",
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
win.geometry("430x520")
win.resizable(False, False)
win.title("2048")
win.configure(bg="#1e1b4b")

# titre du jeu
Label(win, text="2048", font=("Helvetica", 36, "bold"),
      fg="#a855f7", bg="#1e1b4b").place(x=160, y=20)

# label pour afficher le score
label_score = Label(win, text="Score : 0", font=("Helvetica", 16, "bold"),
                    fg="white", bg="#1e1b4b")
label_score.place(x=280, y=35)

# label pour afficher un message (gagné ou perdu)
label_message = Label(win, text="", font=("Helvetica", 20, "bold"),
                      fg="white", bg="#1e1b4b")
label_message.place(x=50, y=490)

# on cree les labels vides et on les place dans la fenetre
for line in range(4):
    for col in range(4):
        labels[line][col] = Label(win, text="", width=6, height=3,
                                  font=("Helvetica", 22, "bold"),
                                  bg=couleurs[0])
        labels[line][col].place(x=x0 + largeur * col, y=y0 + hauteur * line)


# fonction pack4 qui tasse 4 valeurs a,b,c,d vers la gauche comme le jeu 2048
# retourne (a, b, c, d, deplacements, points_gagnes)
def pack4(a, b, c, d):
    deplacements = 0
    points_gagnes = 0
    # on met les valeurs non nulles dans une liste
    vals = [x for x in [a, b, c, d] if x != 0]
    # on complete avec des zeros
    while len(vals) < 4:
        vals.append(0)
    # fusionner les paires egales de gauche a droite
    result = []
    i = 0
    while i < 4:
        if i < 3 and vals[i] != 0 and vals[i] == vals[i + 1]:
            nouvelle_tuile = 2 * vals[i]
            result.append(nouvelle_tuile)
            # on ajoute la valeur de la tuile fusionnee au score
            points_gagnes += nouvelle_tuile
            i += 2
        else:
            result.append(vals[i])
            i += 1
    while len(result) < 4:
        result.append(0)
    # compter combien de cases ont change de position
    original = [a, b, c, d]
    for j in range(4):
        if result[j] != original[j]:
            deplacements += 1
    return result[0], result[1], result[2], result[3], deplacements, points_gagnes


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
        # on choisit une case vide au hasard
        line, col = random.choice(cases_vides)
        # 90% de chance d'avoir un 2, 10% d'avoir un 4
        if random.randint(1, 10) == 1:
            grille[line][col] = 4
        else:
            grille[line][col] = 2


# cette fonction verifie si le joueur a perdu
# on a perdu si le tableau est plein ET qu'il n'y a plus 2 cases identiques cote a cote
def verifier_perdu():
    for line in range(4):
        for col in range(4):
            # si une case est vide, on n'a pas perdu
            if grille[line][col] == 0:
                return False
            # si le voisin de droite est identique, on peut encore jouer
            if col < 3 and grille[line][col] == grille[line][col + 1]:
                return False
            # si le voisin du bas est identique, on peut encore jouer
            if line < 3 and grille[line][col] == grille[line + 1][col]:
                return False
    # si on arrive ici, c'est qu'on ne peut plus rien faire
    return True


# cette fonction verifie si le joueur vient de gagner (atteindre 2048)
# on verifie qu'il y a exactement UN 2048 et rien de plus grand
def verifier_gagne():
    nombre_2048_ou_plus = 0
    for line in range(4):
        for col in range(4):
            if grille[line][col] >= 2048:
                nombre_2048_ou_plus += 1
    # on signale "gagne" seulement si on vient de creer le premier 2048
    # (exactement 1 tuile >= 2048 dans la grille)
    if nombre_2048_ou_plus == 1:
        return True
    return False


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
            # couleur : si la valeur depasse 8192, on prend la couleur de 8192
            bg = couleurs.get(val, "#6d28d9")
            # on met a jour le label
            labels[line][col].configure(
                text=txt, bg=bg,
                font=("Helvetica", taille, "bold"),
                width=int(96 / taille), height=int(48 / taille))


# fonction qui gere les touches directionnelles
def deplacement(event):
    global partie_finie, deja_gagne, score

    # si la partie est finie (perdu), on ne fait plus rien
    if partie_finie:
        return

    touche = event.keysym
    total_dep = 0  # compteur total de deplacements pour savoir si c'est un vrai mouvement
    total_points = 0  # points gagnes pendant ce tour

    if touche == "Left":
        for line in range(4):
            a, b, c, d = grille[line][0], grille[line][1], grille[line][2], grille[line][3]
            grille[line][0], grille[line][1], grille[line][2], grille[line][3], dep, pts = pack4(a, b, c, d)
            total_dep += dep
            total_points += pts

    elif touche == "Right":
        for line in range(4):
            a, b, c, d = grille[line][3], grille[line][2], grille[line][1], grille[line][0]
            grille[line][3], grille[line][2], grille[line][1], grille[line][0], dep, pts = pack4(a, b, c, d)
            total_dep += dep
            total_points += pts

    elif touche == "Up":
        for col in range(4):
            a, b, c, d = grille[0][col], grille[1][col], grille[2][col], grille[3][col]
            grille[0][col], grille[1][col], grille[2][col], grille[3][col], dep, pts = pack4(a, b, c, d)
            total_dep += dep
            total_points += pts

    elif touche == "Down":
        for col in range(4):
            a, b, c, d = grille[3][col], grille[2][col], grille[1][col], grille[0][col]
            grille[3][col], grille[2][col], grille[1][col], grille[0][col], dep, pts = pack4(a, b, c, d)
            total_dep += dep
            total_points += pts

    # on ajoute une tuile seulement si quelque chose a bouge
    if total_dep > 0:
        # on ajoute les points gagnes au score et on met a jour l'affichage
        score += total_points
        label_score.configure(text="Score : " + str(score))
        # verifier si on vient de gagner (avant d'ajouter la tuile)
        if not deja_gagne and verifier_gagne():
            deja_gagne = True
            label_message.configure(text="              Bravo !", fg="#a855f7")

        # ajouter une nouvelle tuile
        ajouter_tuile()

        # verifier si on a perdu apres l'ajout de la tuile
        if verifier_perdu():
            partie_finie = True
            label_message.configure(text="              Perdu !", fg="#f87171")

    # on met a jour l'affichage
    display()


# fonction pour recommencer une partie
def recommencer():
    global grille, partie_finie, deja_gagne, score
    # on remet tout a zero
    grille = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    partie_finie = False
    deja_gagne = False
    score = 0
    # on remet le score et le message a zero
    label_score.configure(text="Score : 0")
    label_message.configure(text="")
    # on ajoute 2 tuiles et on affiche
    ajouter_tuile()
    ajouter_tuile()
    display()


# creation du menu Fichier
barre_menu = Menu(win)
menu_fichier = Menu(barre_menu, tearoff=0)
menu_fichier.add_command(label="Recommencer", command=recommencer)
menu_fichier.add_separator()
menu_fichier.add_command(label="Quitter", command=win.destroy)
barre_menu.add_cascade(label="Fichier", menu=menu_fichier)
win.config(menu=barre_menu)

# on ecoute les touches du clavier
win.bind("<Key>", deplacement)

# on ajoute 2 tuiles au hasard pour commencer la partie
ajouter_tuile()
ajouter_tuile()

# on appelle display pour afficher la grille au demarrage
display()

win.mainloop()
