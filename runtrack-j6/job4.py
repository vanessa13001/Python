def chiffre_cesar(message, decalage):
    resultat = []
    
    for char in message:

        # Vérifier si le caractère est une lettre minuscule
        if char.islower():

            # Décalage dans l'alphabet en tenant compte du dépassement
            new_char = chr((ord(char) - ord('a') + decalage) % 26 + ord('a'))

        # Vérifier si le caractère est une lettre majuscule
        elif char.isupper():

            # Décalage dans l'alphabet en tenant compte du dépassement
            new_char = chr((ord(char) - ord('A') + decalage) % 26 + ord('A'))

        else:
            # Si c'est pas une lettre, on garde telle quelle
            new_char = char
        
        # Ajouter le nouveau caractère à la liste du résultat
        resultat.append(new_char)
    
    # Joindre la liste des caractères en une seule chaîne et la renvoyer
    return ''.join(resultat)

# Exemple d'utilisation :
message = "Bonjour le monde!"
decalage = 3

#resultat
resultat = chiffre_cesar(message, decalage)
print(resultat)
