# Boucle allant de 0 à 100 inclus
for i in range(101):
    # Si le nombre est 26, 37 ou 88, on passe à l'iteration suivante
    if i == 26 or i == 37 or i == 88:
        continue
    # Affichage du nombre
    print(i)
