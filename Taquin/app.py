from collections import deque
import random
import heapq


def liste_initial(degre):
    resultat = []
    numero = 1
    total_elements = degre ** 2
    for _ in range(degre):
        sous_liste = []
        for _ in range(degre):
            if numero < total_elements:
                sous_liste.append(numero)
                numero += 1
            else:
                sous_liste.append(0)
        resultat.append(sous_liste)
    return resultat


def afficher(tableau):
    taille_chiffre = len(str(len(tableau)**2))
    ligne_separatrice = "+" + ("-" * (taille_chiffre + 2) + "+") * len(tableau)
    print(ligne_separatrice)
    for ligne in tableau:
        ligne_a_afficher = "| "
        for element in ligne:
            if element == 0:
                element = '.'
            ligne_a_afficher += f"{element:>{taille_chiffre}} | "
        print(ligne_a_afficher)
        print(ligne_separatrice)


def melanger_liste(liste):
    liste_plate = [element for sous_liste in liste for element in sous_liste]
    random.shuffle(liste_plate)
    degre = len(liste)
    return [liste_plate[i:i + degre] for i in range(0, len(liste_plate), degre)]


def trouver_vide(tableau):
    for i, ligne in enumerate(tableau):
        for j, element in enumerate(ligne):
            if element == 0:
                return i, j
    return None


def generer_etats_suivants(tableau, i, j):
    etats_suivants = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    n, m = len(tableau), len(tableau[0])
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m:
            nouveau_tableau = [ligne[:] for ligne in tableau]
            nouveau_tableau[i][j], nouveau_tableau[ni][nj] = nouveau_tableau[ni][nj], nouveau_tableau[i][j]
            etats_suivants.append(nouveau_tableau)
    return etats_suivants


def bfs(tableau_initial, tableau_cible):
    queue = deque([(tableau_initial, [])])
    visites = set()
    while queue:
        etat_actuel, chemin = queue.popleft()
        if etat_actuel == tableau_cible:
            return chemin + [etat_actuel]
        visites.add(str(etat_actuel))
        i, j = trouver_vide(etat_actuel)
        for nouvel_etat in generer_etats_suivants(etat_actuel, i, j):
            if str(nouvel_etat) not in visites:
                queue.append((nouvel_etat, chemin + [etat_actuel]))
    return None


def dfs(tableau_initial, tableau_cible, limite_profondeur=30):
    pile = [(tableau_initial, [], 0)]
    visites = set()
    while pile:
        etat_actuel, chemin, profondeur = pile.pop()
        if etat_actuel == tableau_cible:
            return chemin + [etat_actuel]
        if profondeur >= limite_profondeur:
            continue
        visites.add(str(etat_actuel))
        i, j = trouver_vide(etat_actuel)
        for nouvel_etat in generer_etats_suivants(etat_actuel, i, j):
            if str(nouvel_etat) not in visites:
                pile.append(
                    (nouvel_etat, chemin + [etat_actuel], profondeur + 1))
    return None


def heuristique(tableau, tableau_cible):
    mal_places = 0
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if tableau[i][j] != tableau_cible[i][j]:
                mal_places += 1
    return mal_places


def a_star(tableau_initial, tableau_cible):
    file_priorite = [
        (heuristique(tableau_initial, tableau_cible), 0, tableau_initial, [])]
    visites = set()
    while file_priorite:
        f, g, etat_actuel, chemin = heapq.heappop(file_priorite)
        if etat_actuel == tableau_cible:
            return chemin + [etat_actuel]
        visites.add(str(etat_actuel))
        i, j = trouver_vide(etat_actuel)
        for nouvel_etat in generer_etats_suivants(etat_actuel, i, j):
            if str(nouvel_etat) not in visites:
                nouveau_g = g + 1
                f = nouveau_g + heuristique(nouvel_etat, tableau_cible)
                heapq.heappush(file_priorite, (f, nouveau_g,
                               nouvel_etat, chemin + [etat_actuel]))
    return None


def resoudre_taquin_bfs(degre):
    liste_initiale = liste_initial(degre)
    liste_melangee = melanger_liste(liste_initiale)
    afficher(liste_melangee)
    chemin_solution = bfs(liste_melangee, liste_initiale)
    if chemin_solution:
        print("Il y a une solution.")
        for etape in chemin_solution:
            afficher(etape)
            print()
    else:
        print("Il n'y a pas de solution.")


def resoudre_taquin_dfs(degre):
    liste_initiale = liste_initial(degre)
    liste_melangee = melanger_liste(liste_initiale)
    afficher(liste_melangee)
    chemin_solution = dfs(liste_melangee, liste_initiale)
    if chemin_solution:
        print("Il y a une solution.")
        for etape in chemin_solution:
            afficher(etape)
            print()
    else:
        print("Il n'y a pas de solution.")


def resoudre_taquin_A(degre):
    liste_initiale = liste_initial(degre)
    liste_melangee = melanger_liste(liste_initiale)
    afficher(liste_melangee)
    chemin_solution = a_star(liste_melangee, liste_initiale)
    if chemin_solution:
        print("Il y a une solution.")
        for etape in chemin_solution:
            afficher(etape)
            print()
    else:
        print("Il n'y a pas de solution.")


resoudre_taquin_A(3)
