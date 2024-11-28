L = [10, 20, 30, 40, 50]


# deuxième valeur de la liste : index 1
print("Deuxième valeur de la liste :", L[1])


# Fonction qui remplace L[3] par la somme des cases voisines L[2] et L[4]
def remplacer_case_voisines():
    L[3] = L[2] + L[4]

# Appel de la fonction pour modifier la liste

remplacer_case_voisines()

print("Liste après modification :", L)

print("Dernière valeur de la liste :", L[-1])
