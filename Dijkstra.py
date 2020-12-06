from Labyrinthe import *

def initialisationDijkstra(Labyrinthe):
    """
    Initialise la carte pour Dijkstra

    IN: Labyrinthe(matrice)

    OUT: carteLabyrinthe(matrice)
    """
    # Récupération de la taille du Labyrinthe
    carteLabyrinthe = np.zeros((len(Labyrinthe), len(Labyrinthe[0])))
    # Initialisation de mapLabyrinthe
    for i in range(len(carteLabyrinthe)):
        for j in range(len(carteLabyrinthe[0])):
            carteLabyrinthe[i][j] = -100 # -100 au lieu de None à cause de NumPy
            # Si la cellule est un mur
            if Labyrinthe[i][j] == 0:
                carteLabyrinthe[i][j] = -1
    return carteLabyrinthe

def recuperationNone(carteLabyrinthe):
    """
    Récupère le nombre de cellules ayant comme valeur -100

    IN: carteLabyrinthe(matrice)

    OUT: nombreNone(int)
    """
    nombreNone = 0
    for x in range(len(carteLabyrinthe)):
        for y in range(len(carteLabyrinthe[0])):
            if carteLabyrinthe[x][y] == -100:
                nombreNone += 1
    return nombreNone

def verificationCelluleAdjacente(cellule1X, cellule1Y, cellule2X, cellule2Y):
    """
    Vérifie si deux cellules sont adjacentes

    IN: cellule1X, cellule1Y, cellule2X, cellule2Y

    OUT: booléen
    """
    celluleX = abs(cellule1X - cellule2X)
    celluleY = abs(cellule1Y - cellule2Y)
    if celluleX <= 1 and celluleY <= 1 and celluleX + celluleY >= 1 and celluleX + celluleY <= 2:
        return True
    return False

def positionCelluleVoisine(celluleActuelleX, celluleActuelleY, celluleAdjacenteX, celluleAdjacenteY):
    """
    Récupère la position de la cellule voisine par rapport à notre cellule actuelle

    IN: celluleActuelle, celluleAdjacente

    OUT: entier(position)
    """
    # La cellule adjacente est en 0
    if celluleAdjacenteX == celluleActuelleX and celluleAdjacenteY - 1 == celluleActuelleY:
        return 0
    # La cellule adjacente est en 1
    if celluleAdjacenteX + 1 == celluleActuelleX and celluleAdjacenteY - 1 == celluleActuelleY:
        return 1
    # La cellule adjacente est en 2
    if celluleAdjacenteX + 1 == celluleActuelleX and celluleAdjacenteY == celluleActuelleY:
        return 2
    # La cellule adjacente est en 3
    if celluleAdjacenteX + 1 == celluleActuelleX and celluleAdjacenteY + 1 == celluleActuelleY:
        return 3
    # La cellule adjacente est en 4
    if celluleAdjacenteX == celluleActuelleX and celluleAdjacenteY + 1 == celluleActuelleY:
        return 4
    # La cellule adjacente est en 5
    if celluleAdjacenteX - 1 == celluleActuelleX and celluleAdjacenteY + 1 == celluleActuelleY:
        return 5
    # La cellule adjacente est en 6
    if celluleAdjacenteX - 1 == celluleActuelleX and celluleAdjacenteY == celluleActuelleY:
        return 6
    # La cellule adjacente est en 7
    if celluleAdjacenteX - 1 == celluleActuelleX and celluleAdjacenteY - 1 == celluleActuelleY:
        return 7    

def voisinsCelluleNonMur(carteDir, celluleX, celluleY):
    """
    Récupères les voisins de cellule qui ne sont pas des murs

    IN: carteDir(matrice), celluleX, celluleY

    OUT: Liste de cellules
    """
    listeCellules = voisinsCellule(carteDir, celluleX, celluleY)
    listeCellulesNonMur = []
    for cellule in listeCellules:
        if carteDir[cellule[0]][cellule[1]] != -1:
            listeCellulesNonMur.append(cellule)
    return listeCellulesNonMur

def recuperationCellulesValides(carteDijkstra):
    """
    Récupère les cellules valides

    IN: carteDijkstra(matrice)

    OUT: Liste de cellules
    """
    listeCellulesValides = []
    for x in range(len(carteDijkstra)):
        for y in range(len(carteDijkstra)):
            # Si la cellule n'est pas un mur
            if carteDijkstra[x][y] != -1:
                listeCellulesValides.append((x, y))
    return listeCellulesValides

def Dijkstra(Labyrinthe, celluleObjectif):
    """
    Effectue l'algorithme de Dijkstra afin de colorer la carte du Labyrinthe

    IN: Labyrinthe(matrice)

    OUT: carteLabyrinthe(matrice)
    """
    # Récupération de la carte
    carteLabyrinthe = initialisationDijkstra(Labyrinthe)
    compteur = 0
    nombreCelluleNone = recuperationNone(carteLabyrinthe)
    # Initialisation
    carteLabyrinthe[celluleObjectif[0]][celluleObjectif[1]] = 0
    # Tant qu'il y a des cellules avec -100 comme valeur
    while nombreCelluleNone != 1:
        # Pour chaque cellule ayant comme valeur compteur
        for x in range(len(carteLabyrinthe)):
            for y in range(len(carteLabyrinthe[x])):
                if carteLabyrinthe[x][y] == compteur:
                    cellulesAdjacentes = voisinsCellule(carteLabyrinthe, x, y)
                    for adjacent in cellulesAdjacentes:
                        # Si la cellule est adjacente et contient comme valeur -100
                        if verificationCelluleAdjacente(adjacent[0], adjacent[1], x, y) and carteLabyrinthe[adjacent[0], adjacent[1]] == -100:
                            carteLabyrinthe[adjacent[0]][adjacent[1]] = compteur+1
                            nombreCelluleNone -= 1
        compteur += 1
    return carteLabyrinthe

def carteDirectionnelle(carteLabyrinthe):
    """
    Construis une carte directionnelle à partir de la carte produite par Dijkstra

    IN: Labyrinthe(matrice), celluleObjectif

    OUT: carteDir(matrice)
    """
    # Récupération de la carte Dijkstra
    carteDir = carteLabyrinthe
    carteDirFinal = np.empty((len(carteDir), len(carteDir[0])))
    carteDirFinal.fill(np.nan)
    # Vérification des voisins
    for x in range(len(carteDir)):
        for y in range(len(carteDir[x])):
            # On évite de vérifier pour les murs
            if carteDir[x][y] != -1:
                cellulesAdjacentes = voisinsCelluleNonMur(carteDir, x, y)
                # On récupère le premier voisin
                cellulePlusPetite = cellulesAdjacentes[0]
                # On parcours ensuite la liste des voisins et on garde uniquement le plus petit voisin
                for adjacent in cellulesAdjacentes[1:]:
                    if carteDir[adjacent[0]][adjacent[1]] != -1 and carteDir[x][y] > carteDir[adjacent[0]][adjacent[1]] and carteDir[adjacent[0]][adjacent[1]] < carteDir[cellulePlusPetite[0]][cellulePlusPetite[1]]:
                        cellulePlusPetite = adjacent
                carteDirFinal[x][y] = positionCelluleVoisine(x, y, cellulePlusPetite[0], cellulePlusPetite[1])
    return carteDirFinal

def cheminSolution(carteDijkstra):
    """
    Donne le chemin solution

    IN: carteLabyrinthe(matrice)

    OUT: carteSolution(matrice), distanceObjectif(entier)
    """
    # Initialisation de la carte Solution
    carteSolution = np.empty((len(carteDijkstra), len(carteDijkstra[0])))
    carteSolution.fill(np.nan)
    # Récupération des cellules valides afin de ne pas choisir un mur
    listeCellulesValides = recuperationCellulesValides(carteDijkstra)
    # Récupération de la cellule de départ
    celluleDepart = random.choice(listeCellulesValides)
    # On initialise le début à 0
    carteSolution[celluleDepart[0]][celluleDepart[1]] = 0
    # Résolution du labyrinthe à partir de cette valeur
    compteur = carteDijkstra[celluleDepart[0]][celluleDepart[1]]
    # Tant que nous n'avons pas atteint la cellule objectif
    distanceObjectif = 1
    while compteur != 0:
        for x in range(len(carteDijkstra)):
            for y in range(len(carteDijkstra[x])):
                # Si la cellule correspond à celle de départ
                if x == celluleDepart[0] and y == celluleDepart[1]:
                    # On récupère les voisins de cette cellule
                    cellulesAdjacentes = voisinsCelluleNonMur(carteDijkstra, celluleDepart[0], celluleDepart[1])
                    # On récupère le premier voisin
                    cellulePlusPetite = cellulesAdjacentes[0]
                    # On parcours ensuite la liste des voisins et on garde uniquement le plus petit voisin
                    for adjacent in cellulesAdjacentes[1:]:
                        if carteDijkstra[adjacent[0]][adjacent[1]] != -1 and carteDijkstra[celluleDepart[0]][celluleDepart[1]] > carteDijkstra[adjacent[0]][adjacent[1]] and carteDijkstra[adjacent[0]][adjacent[1]] < carteDijkstra[cellulePlusPetite[0]][cellulePlusPetite[1]]:
                            cellulePlusPetite = adjacent
                    carteSolution[cellulePlusPetite[0]][cellulePlusPetite[1]] = distanceObjectif
        celluleDepart = cellulePlusPetite
        distanceObjectif += 1
        compteur -= 1
    return carteSolution, distanceObjectif

def listeSolution(cheminSolution):
    """
    Récupère la liste des cellules solution d'un labyrinthe

    IN: cheminSolution(matrice)

    OUT: Liste de cellules
    """
    listeCellules = []
    for x in range(len(cheminSolution)):
        for y in range(len(cheminSolution[x])):
            if cheminSolution[x][y] >= 0:
                listeCellules.append((x, y))
    return listeCellules