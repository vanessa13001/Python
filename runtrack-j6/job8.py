def my_sort(lst):
    n = len(lst)
    total_coups = 0  # Cette variable est pour compter le nombre total de coups (échanges)
    
    # On va répéter l'itération plusieurs fois pour être sûr que la liste soit triée et fonctionne
    for i in range(n):

        # On fait passer les plus grands éléments vers la fin à chaque itération
        for j in range(0, n - i - 1):

            # Comparer les éléments adjacents
            if lst[j] > lst[j + 1]:

                # Échangé si l'élément de gauche est plus grand que celui de droite
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                total_coups += 1  # On compte un échange
                
    # Affichons le nombre total de coups nécessaires pour trier la liste.
    print(f"Nombre total de coups (échanges) : {total_coups}")
    
    return lst

# Exemple d'utilisation
ma_liste = [64, 34, 25, 12, 22, 11, 90]
sorted_list = my_sort(ma_liste)
print("Liste triée :", sorted_list)
