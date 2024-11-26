# Demander à l'utilisateur d'entrer la valeur de N
N = int(input("Entrez un entier N (supérieur à zéro) : "))

# Vérifier que N est positif
if N <= 0:
    print("Veuillez entrer un entier supérieur à zéro.")
else:
    # Boucle pour afficher les tables de multiplication de 1 à N
    for i in range(1, N+1):
        print(f"Table de multiplication de {i}:")
        for j in range(1, N+1):  # Les résultats de 1 à 10
            print(f'{i} x {j} = {i*j}')
        print()  # Pour une ligne vide entre chaque table
