L = [8, 24, 48, 2, 16]

# Initialisation du compteur de multiples de 3
compte_multiples_de_3 = 0

# Parcours de la liste et comptage des multiples de 3
for valeur in L:

     # Vérification si la valeur est un multiple de 3
    if valeur % 3 == 0: 
        compte_multiples_de_3 += 1


print("Le nombre de multiples de 3 dans la liste est :", compte_multiples_de_3)
