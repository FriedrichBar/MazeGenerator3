import numpy as np
import random

def initialisationLabyrinthe(L,l):
    """
    Initalise le labyrinthe

    IN: L(Longueur), l(largeur)

    OUT: Labyrinthe(matrice Lxl)
    """
    return np.zeros((L,l))

def verificationVoisins(Labyrinthe, celluleX, celluleY):
    """
    Vérifie si une cellule ne possède uniquement qu'un voisin déjà visité

    IN: Labyrinthe(matrice), cellule

    OUT: booléen
    """
    # Récupération de la somme des voisins de cellule
    lignes, colonnes = Labyrinthe.shape
    l0, l1 = max(0, celluleX-1), min(lignes-1, celluleX+1)
    c0, c1 = max(0, celluleY-1), min(colonnes-1, celluleY+1)
    ls = list({l0, celluleX, l1})
    cs = [[c] for c in list({c0, celluleY, c1})]
    # Si la somme des voisins est égale à 1
    if Labyrinthe[ls, cs].sum() - Labyrinthe[celluleX, celluleY] == 1:
        return True
    # Sinon
    return False

def voisinsCellule(Labyrinthe, celluleX, celluleY):
    """
    Obtiens les voisins de cellule

    IN: Labyrinthe(matrice), cellule

    OUT: Liste de cellules
    """
    # Initialisation de la matrice des voisins de cellule
    listeCellules = [[celluleX-1, celluleY-1], [celluleX-1, celluleY], [celluleX-1, celluleY+1],
                     [celluleX,   celluleY-1],                         [celluleX,   celluleY+1],
                     [celluleX+1, celluleY-1], [celluleX+1, celluleY], [celluleX+1, celluleY+1]]
    # Initialisation d'une matrice de "suppression" afin d'éviter tout OutOfRange
    suppressionCellule = []
    # Si celluleX est en haut du labyrinthe
    if celluleX == 0:
        suppressionCellule.append((celluleX-1, celluleY-1))
        suppressionCellule.append((celluleX-1, celluleY))
        suppressionCellule.append((celluleX-1, celluleY+1))
    # Si celluleX est en bas du labyrinthe
    if celluleX == len(Labyrinthe) - 1:
        suppressionCellule.append((celluleX+1, celluleY-1))
        suppressionCellule.append((celluleX+1, celluleY))
        suppressionCellule.append((celluleX+1, celluleY+1))
    # Si celluleY est à gauche du labyrinthe
    if celluleY == 0:
        suppressionCellule.append((celluleX-1, celluleY-1))
        suppressionCellule.append((celluleX, celluleY-1))
        suppressionCellule.append((celluleX+1, celluleY-1))
    # Si celluleY est à droite du labyrinthe
    if celluleY == len(Labyrinthe[0]) - 1:
        suppressionCellule.append((celluleX-1, celluleY+1))
        suppressionCellule.append((celluleX, celluleY+1))
        suppressionCellule.append((celluleX+1, celluleY+1))
    # Suppression d'éventuels doublons
    suppressionCellule = list(dict.fromkeys(suppressionCellule))
    # Suppression dans la liste des cellules
    for suppression in suppressionCellule:
        listeCellules.pop(listeCellules.index([suppression[0], suppression[1]]))
    return listeCellules

def voisinsValidesCellule(Labyrinthe, celluleX, celluleY):
    """
    Obtiens les voisins valides de cellule

    IN: Labyrinthe(matrice), cellule

    OUT: Liste de cellules
    """
    # Récupération des voisins de cellule
    listeCellules = voisinsCellule(Labyrinthe, celluleX, celluleY)
    # Initialisation de la liste des voisins de cellule valides
    listeCellulesValides = []
    # Pour chaque voisins de cellule
    for voisin in listeCellules:
        # Si la somme des cellules voisines est égale à 1
        if verificationVoisins(Labyrinthe, voisin[0], voisin[1]) and Labyrinthe[voisin[0]][voisin[1]] == 0:
            # On ajoute la cellule aux cellules valides
            listeCellulesValides.append(voisin)
    return listeCellulesValides

def DFS(L, l):
    """
    Effectue le Depth-First Search (implémentation itérative) afin de générer le labyrinthe

    IN: L(Longueur), l(largeur)
    
    OUT: Labyrinthe(matrice), celluleDepart
    """
    # Initialisation du labyrinthe
    Labyrinthe = initialisationLabyrinthe(L, l)
    # On choisit par hasard la cellule de départ
    celluleDepart = [random.randrange(L), random.randrange(l)]
    # On initialise le stack
    stack = []
    # Ajout de la cellule de départ
    stack.append([celluleDepart[0], celluleDepart[1]])
    Labyrinthe[celluleDepart[0]][celluleDepart[1]] = 1
    # Tant que le stack n'est pas vide
    while len(stack) != 0:
        # On prend la dernière cellule du stack
        celluleActuelle = stack[-1]
        # On récupère les voisins valides de la cellule actuelle
        listeCellulesSuivantes = voisinsValidesCellule(Labyrinthe, celluleActuelle[0], celluleActuelle[1])
        # S'il y a des voisins
        if len(listeCellulesSuivantes) > 0:
            celluleSuivante = random.choice(listeCellulesSuivantes)
            Labyrinthe[celluleSuivante[0]][celluleSuivante[1]] = 1
            stack.append(celluleSuivante)
        # Sinon il faut "backtrack"
        else:
            stack.pop()
            # On évite un IndexOutOfRange
            if len(stack) != 0:
                celluleActuelle = stack[-1]
    return Labyrinthe, celluleDepart