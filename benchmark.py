from Dijkstra import *

print("Taille du labyrinthe : 8")
print("Nombre de répétition : 10")
moyenneDistanceObjectif = 0
for _ in range(10):
    Labyrinthe, celluleDepart = DFS(8,8)
    carteLabyrinthe = Dijkstra(Labyrinthe, celluleDepart)
    solutionLabyrinthe, distanceObjectif = cheminSolution(carteLabyrinthe)
    moyenneDistanceObjectif += distanceObjectif
print("Moyenne : ", moyenneDistanceObjectif/10)
print("")
print("Taille du labyrinthe : 16")
print("Nombre de répétition : 10")
moyenneDistanceObjectif = 0
for _ in range(10):
    Labyrinthe, celluleDepart = DFS(16,16)
    carteLabyrinthe = Dijkstra(Labyrinthe, celluleDepart)
    solutionLabyrinthe, distanceObjectif = cheminSolution(carteLabyrinthe)
    moyenneDistanceObjectif += distanceObjectif
print("Moyenne : ", moyenneDistanceObjectif/10)
print("")
print("Taille du labyrinthe : 32")
print("Nombre de répétition : 10")
moyenneDistanceObjectif = 0
for _ in range(10):
    Labyrinthe, celluleDepart = DFS(32,32)
    carteLabyrinthe = Dijkstra(Labyrinthe, celluleDepart)
    solutionLabyrinthe, distanceObjectif = cheminSolution(carteLabyrinthe)
    moyenneDistanceObjectif += distanceObjectif
print("Moyenne : ", moyenneDistanceObjectif/10)
print("")
print("Taille du labyrinthe : 64")
print("Nombre de répétition : 10")
moyenneDistanceObjectif = 0
for _ in range(10):
    Labyrinthe, celluleDepart = DFS(64,64)
    carteLabyrinthe = Dijkstra(Labyrinthe, celluleDepart)
    solutionLabyrinthe, distanceObjectif = cheminSolution(carteLabyrinthe)
    moyenneDistanceObjectif += distanceObjectif
print("Moyenne : ", moyenneDistanceObjectif/10)
print("")
print("Taille du labyrinthe : 128")
print("Nombre de répétition : 10")
moyenneDistanceObjectif = 0
for _ in range(10):
    Labyrinthe, celluleDepart = DFS(128,128)
    carteLabyrinthe = Dijkstra(Labyrinthe, celluleDepart)
    solutionLabyrinthe, distanceObjectif = cheminSolution(carteLabyrinthe)
    moyenneDistanceObjectif += distanceObjectif
print("Moyenne : ", moyenneDistanceObjectif/10)
print("")
print("Taille du labyrinthe : 256")
print("Nombre de répétition : 10")
moyenneDistanceObjectif = 0
for _ in range(10):
    Labyrinthe, celluleDepart = DFS(256,256)
    carteLabyrinthe = Dijkstra(Labyrinthe, celluleDepart)
    solutionLabyrinthe, distanceObjectif = cheminSolution(carteLabyrinthe)
    moyenneDistanceObjectif += distanceObjectif
print("Moyenne : ", moyenneDistanceObjectif/10)
print("")
print("Taille du labyrinthe : 512")
print("Nombre de répétition : 10")
moyenneDistanceObjectif = 0
for _ in range(10):
    Labyrinthe, celluleDepart = DFS(512,512)
    carteLabyrinthe = Dijkstra(Labyrinthe, celluleDepart)
    solutionLabyrinthe, distanceObjectif = cheminSolution(carteLabyrinthe)
    moyenneDistanceObjectif += distanceObjectif
print("Moyenne : ", moyenneDistanceObjectif/10)