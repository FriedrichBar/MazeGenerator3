# l'objectif est la cellule de la carte contenant 0

def distancePasse(depuis, carte, objectif, chemin):
    # si on passe par l'objectif dans le chemin, on considère que la distance est nulle
    if objectif in chemin:
        return 0
    else:
        return carte[depuis[0]][depuis[1]]

def penalites(chemin):
    """
    Calcule la pénalité du programme

    IN: chemin, carte

    OUT: float(pénalité)
    """
    # Si le programme visite une cellule déjà visitée, on ajoute une grosse pénalité
    return abs(len(chemin) - len(set(chemin)))

def progToChemin(programme, debut, carte):
    """
    Convertis un programme en chemin

    IN: programme(tableau d'entier), debut(cellule de départ), carte(labyrinthe)

    OUT: chemin(tableau de cellule)
    """
    chemin = [debut]
    # Pour chaque choix du programme, on ajoute à notre chemin la cellule correspondante si ce n'est pas un mur
    for choix in programme:
        # On utilise un try except pour éviter d'avoir 2 ifs imbriqués pour chaque choix
        # Il faudrait vérifier si l'on est pas en Out Of Range
        # Et ensuite vérifier qu'on reste dans le labyrinthe après une tentative du programme
        try:
            # 0 et pas un mur
            if choix == 0 and carte[debut[0]][debut [1]+1] != -100 and debut[1]+1 < len(carte):
                chemin.append((debut[0],debut[1]+1))
            # 1 et pas un mur
            if choix == 1 and carte[debut[0]-1][debut[1]+1] != -100 and debut[0]-1 >= 0 and debut[1]+1 < len(carte):
                chemin.append((debut[0]-1,debut[1]+1))
            # 2 et pas un mur
            if choix == 2 and carte[debut[0]-1][debut[1]] != -100 and debut[0]-1 >= 0:
                chemin.append((debut[0]-1,debut[1]))
            # 3 et pas un mur
            if choix == 3 and carte[debut[0]-1][debut[1]-1] != -100 and debut[0]-1 >= 0 and debut[1]-1 >= 0:
                chemin.append((debut[0]-1,debut[1]-1))
            # 4 et pas un mur
            if choix == 4 and carte[debut[0]][debut[1]-1] != -100 and debut[1]-1 >= 0:
                chemin.append((debut[0],debut[1]-1))
            # 5 et pas un mur
            if choix == 5 and carte[debut[0]+1][debut[1]-1] != -100 and debut[0]+1 < len(carte) and debut[1]-1 >= 0:
                chemin.append((debut[0]+1,debut[1]-1))
            # 6 et pas un mur
            if choix == 6 and carte[debut[0]+1][debut[1]] != -100 and debut[0]+1 < len(carte):
                chemin.append((debut[0]+1,debut[1]))
            # 7 et pas un mur
            if choix == 7 and carte[debut[0]+1][debut[1]+1] != -100 and debut[0]+1 < len(carte) and debut[1]+1 < len(carte):
                chemin.append((debut[0]+1,debut[1]+1))
            debut = chemin[-1]
        except:
            pass
    return chemin

# le plus petit est le mieux
def Fitness(programme, carte, debut, objectif):
    chemin = progToChemin(programme, debut, carte)
    dist = distancePasse(debut, carte, objectif, chemin)
    pena = penalites(chemin)
    if objectif in chemin:
        return -1000
    return 2 * dist + 5 * pena
