from Affichage import *

Labyrinthe, celluleDepart = DFS(100, 100)
pixelsLabyrinthe = conversionLabyrintheAPixels(Labyrinthe, celluleDepart)
enregistrementLabyrinthe('Labyrinthe.png', pixelsLabyrinthe)

carteLabyrinthe = Dijkstra(Labyrinthe, celluleDepart)
affichageGraphique(carteLabyrinthe)

solutionLabyrinthe, distanceObjectif = cheminSolution(carteLabyrinthe)
listeSolution = listeSolution(solutionLabyrinthe)
pixelsSolutionLabyrinthe = conversionSolutionAPixels(Labyrinthe, listeSolution)
enregistrementLabyrinthe('SolutionLabyrinthe.png', pixelsSolutionLabyrinthe)
print("Taille du chemin solution :", distanceObjectif)