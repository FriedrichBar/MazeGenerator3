# Projet Labyrinthe Maze Runner

## Promotion Cybersécurité du Logiciel 2020-2023

## Fonctionnement

## Partie 1

`python3 ProjetLabyrinthe.py`

Le programme renvoie une image du labyrinthe nommée Labyrinthe.png.

La cellule rouge correspond au point d'arrivé, les cellules noires aux murs et les cellules blanches aux chemins.

L'utilisateur peut se déplacer en 8.

### Benchmark

Le programme de benchmark est inclus dans l'archive zip. Pour l'exécuter, il suffit de faire `python3 benchmark.py`.

L = Largeur

l = longueur

N = Nombre de cellules

| L | l   |N      | Temps | N/Temps|
|---|-----|-------|-------|--------|
|5  |5    |25     |0.0020s|12500   |
|25 |25   |625    |0.0560s|11160   |
|50 |50   |2500   |0.2149s|11633   |
|75 |75   |5625   |0.4898s|11484   |
|100|100  |10000  |0.8967s|11152   |
|150|150  |22500  |2.0102s|11192   |
|175|175  |30625  |2.7111s|11296   |
|200|200  |40000  |3.5317s|11326   |
|250|250  |62500  |5.6758s|11011   |
|300|300  |90000  |7.9880s|11267   |
|500|500  |250000 |22.693s|11016   |
|750|750  |562500 |51.054s|11017   |
|1000|1000|1000000|90.844s|11008   |

En comparant ces résultats avec un autre étudiant qui n'a pas utilisé numpy, nous nous rendons compte que nos temps de générations sont largement supérieurs.

Cela est notamment dû lors de la vérification des voisins. En effet, numpy.sum() est beaucoup plus lent que sum() pour des listes.


![alt text](https://i.ibb.co/PgDhr9R/np.png "Graphe vitesse")

Manquant de temps, j'ai décidé de rester sur cette solution avec numpy. Toutefois, cela peut rester intéressant si l'on souhaite comparer différents algorithmes.

### Complexité

Après notre benchmark, lorsque nous comparons les valeures de N/temps, nous nous rendons compte que plus N augmente, moins nous possédons de différence.

Nous en déduisons alors que notre programme possède une complexité égale à O(n).

## Partie 2

`python3 ProjetLabyrinthe.py`

Le programme renvoie une image du labyrinthe nommée Labyrinthe.png.

Il va ensuite visualiser le labyrinthe après Dijkstra et l'enregistre également sous le nom CarteLabyrinthe.png.

Enfin, il renvoie une dernière image, SolutionLabyrinthe.png qui affiche le chemin solution depuis une cellule sélectionnée aléatoirement, et affiche dans la console la taille du chemin solution depuis cette cellule.

### Benchmark

Le programme de benchmark est inclus dans l'archive zip. Pour l'exécuter, il suffit de faire `python3 benchmark.py`.

|Taille du Labyrinthe|Nombre de répétition|Moyenne|
|--------------------|--------------------|-------|
|         8          |          10        |  10.0 |
|        16          |          10        |  30.2 |
|        32          |          10        |  101.5|
|        64          |          10        |  490.6|
|        128         |          10        |  798.3|
|        256         |          10        | 3691.0|
|        512         |          10        |13842.3|

### Partie 3

`python3 GeneticDemo.py`

Possibilité d'ajouter ` > résultats.txt` après la commande pour une meilleure visibilitée.

**GeneticEngine.py** contient les grandes étapes correspondant à un algorithme génétique, ainsi que la fonction de
pose de phéromones.

**GeneticFitness.py** contient les fonctions servant aux calculs de la pénalité et du score de fitness ; on remarque au
return de la fonction Fitness qu’on peut ajuster l’équilibre entre la distance et la pénalité.

**GeneticDemo.py** est le fichier à exécuter pour faire fonctionner facilement l’algorithme génétique : les paramètres
sont clairement indiqués et donc plus facilement ajustables. Il écrit dans le terminal diverses informations sur le déroulement de l’algorithme.

### Difficultés

Ayant un manque de temps conséquent, j'ai décidé de m'associer avec Cornichon622, camarade de mon ancienne école, et étant dans l'autre groupe de TP. Sur le PC de Cornichon622, nous avons eu beaucoup de mal à trouver des paramètres idéaux pour l'algorithme génétique, et nous n'avons pas pu parvenir à obtenir un chemin allant du départ à l'objectif.

Cependant, en recopiant le programme sur mon PC, et en l'adaptant avec mes fonctions (vu que l'on ne possède pas les mêmes), certaines fois, nous possédons des chemins allant du départ à l'objectif. Nous ne savons pas clairement pourquoi cela se produit.

Du côté de Cornichon622, nous avons plusieurs idées là dessus : la fonction *penalites* qui regarde le nombre de doublons présents dans la liste des cellules visitées par un programme ; la spécificité des algorithmes génétiques, pour lesquels il faut un ensemble de paramètres cohérents pour arriver à un résultat satisfaisant.

## Auteurs

Friedrich Bär, Cornichon622 (pour la partie 3)