# Fonction pour trier une liste dans l'ordre croissant sans utiliser de fonctions système
def trier_liste(L):

    # On parcourt toute la liste
    for i in range(len(L)):

        # On trouve la position du plus petit élément à partir de la position i
        for j in range(i + 1, len(L)):

            # Si on trouve un élément plus petit, on les échange
            if L[j] < L[i]:
                L[i], L[j] = L[j], L[i]
    return L

# liste à trier
L = [7, 11, 42, 39, 2]

# appel de la fonction pour trier la liste
L_triee = trier_liste(L)


print("Liste triée dans l'ordre croissant :", L_triee)
