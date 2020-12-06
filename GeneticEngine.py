from GeneticFitness import Fitness, progToChemin
import random
from Labyrinthe import voisinsCellule

'''
Copié collé https://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python
Utilisé pour éviter d'importer numpy entier et de trop ralentir
le programme alors que je n'ai besoin que d'argsort
'''
def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)

def Genese(nbrProg, tailleProg):
    programmes = []

    for _ in range(nbrProg):
        programme = []
        for _ in range(tailleProg):
            direction = random.choice([0, 1, 2, 3, 4, 5, 6, 7])
            programme.append(direction)
        programmes.append(programme)
    
    return programmes

def Selection(tauxSurvie, programmes, carte, debut, objectif):
    # calcul des fitness
    scores = []
    for programme in programmes:
        scores.append(Fitness(programme, carte, debut, objectif))

    # conservation des tauxSurvie % meilleurs (lower is better)
    ordre = argsort(scores)
    nbrConserves = round(len(programmes) * tauxSurvie)
    conserves = []
    for i in range(nbrConserves):
        indice = ordre[i]
        conserves.append(programmes[indice])
    
    return conserves, scores

def Reproduction(nbrProg, programmes, apportMinParent):
    nvProgrammes = []
    
    # on récupère les programmes sélectionnés
    for programme in programmes:
        nvProgrammes.append(programme)
    
    # tant qu'on a pas assez de prorgammes, on reproduit
    while len(nvProgrammes) < nbrProg:
        # on choisit 2 parents
        p1 = random.choice(programmes)
        p2 = random.choice(programmes)
        
        # on choisit où on coupe
        cut = 0
        cuts = [i for i in range(len(programmes[0]))]
        while cut < len(programmes[0]) * apportMinParent or cut > len(programmes[0]) * (1 - apportMinParent):
            cut = random.choice(cuts)
        
        # on construit l'enfant
        nvProgrammes.append(p1[:cut] + p2[cut:])
    
    return nvProgrammes


def Mutation(programmes, tauxMutation):
    tailleProg = len(programmes[0])
    # on calcule le nombre de mutations à effectuer
    nbrMutations = int(len(programmes) * tauxMutation)

    # on effectue les mutations une à une
    for _ in range(nbrMutations):
        # choix d'un programme aléatoire
        programme = random.choice(programmes)
        # choix de l'endroit de la mutation
        indexMut = random.choice([i for i in range(tailleProg)])
        # mutation
        valeurs = [0, 1, 2, 3, 4, 5, 6, 7]
        valeurs.pop(valeurs.index(programme[indexMut])) # pour ne pas avoir la même valeur qu'à l'origine
        programme[indexMut] = random.choice(valeurs)

    return programmes

def Pheromones(programmes, debut, carte):
    # on vérifie toutes les cellules visitées par tous les programmes
    for programme in programmes:
        chemin = progToChemin(programme, debut, carte)
        for cellule in chemin:
            # si la cellule n'est pas le départ
            if cellule[0] != debut[0] and cellule[1] != debut[1]:
                # on compte les voisins qui sont des chemins
                voisins = voisinsCellule(carte, cellule[0], cellule[1])
                cellulesVidesAdjacentes = 0
                for voisin in voisins:
                    if carte[voisin[0]][voisin[1]] != -100:
                        cellulesVidesAdjacentes += 1
                # si elle a un seul chemin adjacent, c'est un cul de sac, on rebouche
                if cellulesVidesAdjacentes == 1:
                    carte[cellule[0]][cellule[1]] = -100
    return carte

def Evolution(nbrProg, tailleProg, tauxSurvie, tauxMutation, apportMinParent, nbrGen, carte, debut, objectif):
    programmes = Genese(nbrProg, tailleProg)
    evoFitness = []

    for _ in range(nbrGen):
        # phéromones
        carte = Pheromones(programmes, debut, carte)
        # sélection
        progConserves, scores = Selection(tauxSurvie, programmes, carte, debut, objectif)
        evoFitness.append(scores) # on conserve une trace des fitness
        # reproduction
        programmes = Reproduction(nbrProg, progConserves, apportMinParent)
        # mutation
        programmes = Mutation(programmes, tauxMutation)
    
    _, fitnessDerniereGen = Selection(tauxSurvie, programmes, carte, debut, objectif)
    evoFitness.append(fitnessDerniereGen)
    return programmes, evoFitness