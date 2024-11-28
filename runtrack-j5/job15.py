nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# arrondir les nombres de la liste
arrondis = []
for nombre in nombres:

    # arrondir à l'entier le plus proche: en arrondissant vers l'entier le plus proche
    if nombre - int(nombre) >= 0.5:
        arrondis.append(int(nombre) + 1)
    else:
        arrondis.append(int(nombre))

# Étape 2: Trier la liste par ordre croissant

# Implenté un tri par sélection
for i in range(len(arrondis)):
    for j in range(i + 1, len(arrondis)):
        if arrondis[i] > arrondis[j]:
            
            # Échanger les éléments
            temp = arrondis[i]
            arrondis[i] = arrondis[j]
            arrondis[j] = temp


print(arrondis)
