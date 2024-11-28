L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Initialisation de la variable pour la somme des valeurs paires
somme_paires = 0

# liste et addition des valeurs paires
for valeur in L:

    # Vérifiez si la valeur est paire
    if valeur % 2 == 0:  
        somme_paires += valeur

print("La somme des valeurs paires de la liste est :", somme_paires)
