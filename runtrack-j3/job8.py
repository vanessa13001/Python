import math
# demander à l'utilisateur de saisir les trois longueurs
a = float (input("Entrez la longueur a : "))
b = float (input ("Entrer la longueur b : "))
c = float (input("Entrer la lngueur c : "))

# verifier si les longueurs peuvent former un triangle
if a + b > c and a + c > b and b + c > a: 

    # verfier si le triangle est rectangle
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print("Le triangle est rectangle")

    # verifier si le triangle est équilatéral
    elif a == b == c :
        print("Le triangle est équilatéral")

    # verifier si le triangle isocèle 

    elif a == b or a == c or b == c:
        print(" Le triangke est isocéle")

    # si aucune des conditions précédentes, le triangle est quelconque
    else:
        print("Le triangle est quelconque")

else:
    print("Les longueurs saisies ne forment pas un triangle")