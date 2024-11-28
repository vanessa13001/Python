def supprimer_doublons(L):

    # Liste pour stocker les éléments uniques
    result = []
    
    # Parcours de chaque élément de la liste
    for element in L:

        # Si l'élément n'est pas déjà dans la liste result, on le rajoute obligatoirement
        if element not in result:
            result.append(element)
    
    return result

L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

L_sans_doublons = supprimer_doublons(L)

print("Liste sans doublons :", L_sans_doublons)

