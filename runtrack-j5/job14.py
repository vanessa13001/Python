# Fonction pour récupérer les mots plus longs qu'un chiffre donné
def my_long_word(longueur, phrase):
    # Initialisation de la liste de mots plus longs
    mots_long = []
    
    # Découper la phrase en mots
    mot = ""
    for char in phrase:
        if char == " " or char == "," or char == "." or char == "\n":

            # Quand on rencontre un espace ou une ponctuation, on a un mot complet
            if mot != "" and count_char(mot) > longueur:

                mots_long.append(mot)  # Ajout du mot si sa longueur est plus grande
                
            # Réinitialiser le mot pour le prochain mot
            mot = ""  

        # Construire le mot caractère par caractère
        else:
            mot += char  
    
    # Si un dernier mot existe : sans espace à la fin
    if mot != "" and count_char(mot) > longueur:
        mots_long.append(mot)
    
    # Retourner les mots longs sous forme de chaîne

    return " ".join(mots_long)

# Fonction pour compter le nombre de caractères d'un mot (simuler len())

def count_char(mot):
    compteur = 0
    for _ in mot:
        compteur += 1
    return compteur


phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
resultat = my_long_word(3, phrase)
print(resultat)
