L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Initialisation du produit
produit = 1

# Boucle pour parcourir les éléments de la liste
for val in L:

    # Vérifiez si l'élément est dans l'intervalle [25, 90]
    if 25 <= val <= 90:  

        #multiplier le produit
        produit *= val 


print(f"Le produit des valeurs dans l'intervalle [25, 90] est : {produit}")
