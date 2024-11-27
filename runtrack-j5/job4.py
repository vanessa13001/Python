def ajouter_mangue():
    fruits = ["pomme", "cerise", "orange", "melon"]
    fruits.insert(3, "mangue")  # Ajoute "mangue" à l'index 2
    return fruits

# Appel de la fonction
resultat = ajouter_mangue()
print(resultat)
