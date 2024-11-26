# Demander à l'utilisateur de saisir un nombre entier N
N = int(input("Entrez un entier N : "))

# Initialiser un compteur pour afficher les premiers résultats
compteur = 1

# Utiliser une boucle while pour afficher les premiers résultats de la multiplication de N par 7
while compteur <= 10:  # Par exemple, afficher les 10 premiers résultats
    resultat = N * 7 * compteur
    print(f"{N} * 7 * {compteur} = {resultat}")
    compteur += 1
