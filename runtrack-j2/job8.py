# Initialiser le numéro du tour précédent à 0
precedent = 0

# Boucle qui effectue 12 tours
for tour in range(1, 13):
    # Calculer le résultat en ajoutant 2 au numéro du tour précédent
    resultat = precedent + 2
    print(f"Tour {tour}: {resultat}")
    
    # Mettre à jour le numéro du tour précédent avec le résultat actuel
    precedent = resultat
