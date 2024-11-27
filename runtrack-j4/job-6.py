def verifier_signe(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("négatif")
    else:
        print("le nombre est zéro")

nombre= int(input("chiffre"))
verifier_signe(nombre)