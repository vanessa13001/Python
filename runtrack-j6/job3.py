def afficher_tapis(n):
    for i in range(n + 1):
        # Créer la ligne avec n+1 colonnes
        ligne = ""
        for j in range(n + 1):
            if i == j:  # Diagonale (\)
                ligne += "\\"
            else:       # Autres cases (_)
                ligne += "_"
        print(ligne)

# Demander la taille du tapis
n = 10  # Exemple de taille

# Appeler la fonction pour afficher le tapis
afficher_tapis(n)
