def afficher_aliments(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print("Poire, fraise, cassis")
    elif type == "légume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légume" and saison == "été":
        print("artichaut, aubergine, navet")
    else:
        print("Saison ou type inconnu")

afficher_aliments("fruits", "hiver")
afficher_aliments("légume", "été")
afficher_aliments("fruits", "printemps")
afficher_aliments("fruits", "été")
