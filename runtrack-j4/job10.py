def verifier_pair_impair(nombre):

    # Vérifier si le nombre est un entier positif
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            print(f"{nombre} est un nombre pair.")
        else:
            print(f"{nombre} est un nombre impair.")
    else:
        print("Veuillez entrer un nombre entier positif.")

# Appel de la fonction avec différentes valeurs
verifier_pair_impair(4) 
verifier_pair_impair(7)  
verifier_pair_impair(-3) 
verifier_pair_impair(10.5)