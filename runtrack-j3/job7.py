# Définition de la chaîne
chaine = "abcdefghijklmnopqrstuvwxyz" * 10

# Initialisation des variables
i = 1  # Début de la première ligne avec 1 caractère
index = 0  # L'index de départ dans la chaîne

# Boucle pour afficher la suite pyramide
while index + i <= len(chaine):
    print(chaine[index : index + i])
    index += i  # Déplace l'index pour la prochaine ligne
    i += 1  # Augmente le nombre de caractères à afficher pour la ligne suivante
