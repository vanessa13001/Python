def echanger_premiere_derniere_case(L):

    # Vérifier que la liste n'est pas vide
    if len(L) > 0:
        
        # Échange des valeurs entre la première et la dernière
        L[0], L[-1] = L[-1], L[0]
    return L

# Exemple d'une liste quelconque non vide
L = [10, 20, 30, 40, 50]

# Affichage avant l'échange
print("Liste avant échange :", L)

# Appel la fonction pour échanger les valeurs
L = echanger_premiere_derniere_case(L)

print("Liste après échange :", L)
