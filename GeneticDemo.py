from Labyrinthe import DFS
from Dijkstra import Dijkstra
from random import randint
from GeneticEngine import Evolution
from GeneticFitness import progToChemin

# definir les parametres du labyrinthe
tailleLab = 20
distanceMinDepart = 30
# definir les parametres de l'algo genetique
nbrProg = 50
tailleProg = 120
tauxSurvie = 0.35
tauxMutation = 0.5
apportMinParent = 0.4
nbrGen = 120

# generer labyrinthe
lab, objectif = DFS(tailleLab, tailleLab)

# calculer dijkstra
carte = Dijkstra(lab, objectif)

# choisir départ suffisamment éloigné
debut = (randint(0, len(lab) - 1), randint(0, len(lab[0]) - 1))
while lab[debut[0]][debut[1]] != 1 or carte[debut[0]][debut[1]] < distanceMinDepart:
        debut = (randint(0, len(lab) - 1), randint(0, len(lab[0]) - 1))

# lancer l'algo génétique
programmes, evoFitness = Evolution(nbrProg, tailleProg, tauxSurvie, tauxMutation, apportMinParent, nbrGen, carte, debut, objectif)

# afficher les résultats
print("### PARAMETRES")
print("tailleLab", tailleLab, "distanceMinDepart", distanceMinDepart, "nbrProg", nbrProg, "tailleProg", tailleProg, "tauxSurvie", tauxSurvie, "tauxMutation", tauxMutation, "apportMinParent", apportMinParent, "nbrGen", nbrGen)
print("### LABYRINTHE")
print(lab)
print("### CHEMIN")
print("de", debut, "a", objectif, "longueur", carte[debut[0]][debut[1]])
print("### EVOLUTION FITNESS")
print(evoFitness)
print("### PROGRAMMES")
print(programmes)
print("### CHEMINS")
chemins = []
for programme in programmes:
    chemins.append(progToChemin(programme, debut, carte))
print(chemins)
