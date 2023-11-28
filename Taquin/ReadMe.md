# Résolution du Puzzle Taquin en Python

Ce programme implémente des algorithmes pour résoudre le puzzle taquin, un jeu de plateau classique.

## Importations de Modules
Le code utilise trois modules Python :
- `collections.deque` pour implémenter des files d'attente.
- `random` pour mélanger les tuiles du taquin.
- `heapq` pour la gestion de la file de priorité dans l'algorithme A*.

## Fonctions Principales

### liste_initial(degre)
Crée une grille initiale pour le puzzle taquin.
- **Paramètre** : `degre` - la taille de la grille.
- **Retourne** : Une grille carrée sous forme de liste de listes avec les tuiles numérotées et un espace vide (0).

### afficher(tableau)
Affiche la grille du taquin de manière formatée.
- **Paramètre** : `tableau` - la grille du taquin à afficher.

### melanger_liste(liste)
Mélange les tuiles dans la grille du taquin.
- **Paramètre** : `liste` - la grille du taquin.
- **Retourne** : Une grille mélangée.

### trouver_vide(tableau)
Trouve la position de l'espace vide dans la grille.
- **Paramètre** : `tableau` - la grille du taquin.
- **Retourne** : Les coordonnées de l'espace vide.

### generer_etats_suivants(tableau, i, j)
Génère tous les états possibles à partir de l'état actuel en déplaçant l'espace vide.
- **Paramètres** : `tableau` - l'état actuel, `i`, `j` - position de l'espace vide.
- **Retourne** : Liste des états possibles après un mouvement.

### bfs(tableau_initial, tableau_cible)
Implémente l'algorithme de recherche en largeur (BFS).
- **Paramètres** : `tableau_initial` et `tableau_cible`.
- **Retourne** : Chemin de l'état initial à l'état cible, s'il existe.

### dfs(tableau_initial, tableau_cible, limite_profondeur)
Implémente l'algorithme de recherche en profondeur (DFS) avec une limite de profondeur.
- **Paramètres** : `tableau_initial`, `tableau_cible`, `limite_profondeur`.
- **Retourne** : Chemin de l'état initial à l'état cible, s'il existe.

### heuristique(tableau, tableau_cible)
Calcule le nombre de tuiles mal placées.
- **Paramètres** : `tableau` et `tableau_cible`.
- **Retourne** : Nombre de tuiles mal placées.

### a_star(tableau_initial, tableau_cible)
Implémente l'algorithme A* pour résoudre le puzzle.
- **Paramètres** : `tableau_initial` et `tableau_cible`.
- **Retourne** : Chemin de l'état initial à l'état cible, s'il existe.

### resoudre_taquin_[bfs/dfs/A](degre)
Fonctions pour résoudre le puzzle taquin en utilisant les algorithmes BFS, DFS, et A*.
- **Paramètre** : `degre` - la taille de la grille du taquin.
- **Comportement** : Affiche le chemin de la solution, s'il existe.

## Utilisation du Programme
Pour utiliser le programme, il suffit de choisir la taille de la grille et l'algorithme de résolution, puis d'exécuter la fonction correspondante. Le programme affichera la grille mélangée et tentera de trouver un chemin vers la configuration cible.
