# 2048 - Projet MA20

Reproduction du jeu **2048** en Python avec une interface graphique faite en Tkinter.

Projet realise dans le cadre du module MA20 par **Amin Torrisi**.

---

## Presentation du jeu

Le 2048 est un jeu de puzzle ou le but est de faire glisser des tuiles numerotees sur une grille 4x4.
Quand deux tuiles avec le meme nombre se touchent, elles fusionnent en une seule tuile dont la valeur est doublee.
L'objectif est d'atteindre la tuile **2048**.

### Regles du jeu

- A chaque tour, le joueur deplace toutes les tuiles dans une direction (haut, bas, gauche, droite)
- Les tuiles glissent jusqu'au bord de la grille ou jusqu'a une autre tuile
- Si deux tuiles identiques se rencontrent, elles fusionnent (ex: 2+2 = 4, 4+4 = 8, etc.)
- Apres chaque deplacement, une nouvelle tuile (2 ou 4) apparait sur une case vide
- La partie est **gagnee** quand on atteint la tuile 2048
- La partie est **perdue** quand la grille est pleine et qu'aucune fusion n'est possible

---

## Comment lancer le jeu

### Pre-requis

- Python 3 installe sur l'ordinateur
- Tkinter (normalement inclus avec Python)

### Lancement

```
python game.py
```

Le jeu s'ouvre dans une fenetre. Utilisez les **fleches directionnelles** du clavier pour jouer.

### Menu

- **Fichier > Recommencer** : relance une nouvelle partie
- **Fichier > Quitter** : ferme le jeu

---

## Fonctionnalites

| Fonctionnalite | Description |
|---|---|
| Grille 4x4 | Affichage graphique avec des couleurs differentes pour chaque valeur |
| Deplacements | Les tuiles se deplacent dans les 4 directions avec les fleches du clavier |
| Fusions | Deux tuiles identiques fusionnent automatiquement |
| Score | Le score augmente a chaque fusion (la valeur de la tuile creee est ajoutee) |
| Victoire | Un message "Bravo !" s'affiche quand on atteint 2048 |
| Defaite | Un message "Perdu !" s'affiche quand plus aucun mouvement n'est possible |
| Recommencer | Possibilite de relancer une partie via le menu Fichier |
| Nouvelles tuiles | Une tuile 2 (90%) ou 4 (10%) apparait apres chaque vrai deplacement |

---

## Structure du code

Le jeu est contenu dans un seul fichier : `game.py`

### Variables principales

- `grille` : liste 4x4 qui contient les valeurs des tuiles (0 = case vide)
- `score` : le score actuel du joueur
- `partie_finie` : booleen qui bloque les deplacements quand on a perdu
- `deja_gagne` : booleen pour n'afficher le message de victoire qu'une seule fois

### Fonctions

- `pack4(a, b, c, d)` : prend 4 valeurs d'une ligne ou colonne, les tasse vers la gauche et fusionne les paires egales. Retourne les nouvelles valeurs, le nombre de deplacements et les points gagnes.
- `ajouter_tuile()` : place une tuile 2 ou 4 sur une case vide choisie au hasard.
- `verifier_perdu()` : verifie si la grille est pleine sans aucune fusion possible.
- `verifier_gagne()` : verifie si le joueur vient d'atteindre 2048 pour la premiere fois.
- `display()` : met a jour l'affichage de toutes les tuiles (texte, couleur, taille).
- `deplacement(event)` : gere les touches du clavier et applique le mouvement dans la bonne direction.
- `recommencer()` : remet tout a zero pour une nouvelle partie.

---

## Historique des sprints

| Sprint | Description |
|---|---|
| Sprint 2 | Maquette de la grille + wireframe |
| Sprint 3 | Deplacement des tuiles et fusions fonctionnels |
| Sprint 4 | Score, detection victoire/defaite, menu recommencer |

---

## Technologies utilisees

- **Python 3**
- **Tkinter** (interface graphique)
- **random** (generation aleatoire des tuiles)
