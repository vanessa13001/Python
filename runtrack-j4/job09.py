def moyenne(note1, note2, note3):
    
    # Calcul de la moyenne des trois notes
    return (note1 + note2 + note3) / 3

# Demander à l'utilisateur de saisir trois notes
note1 = float(input("Entrez la première note : "))
note2 = float(input("Entrez la deuxième note : "))
note3 = float(input("Entrez la troisième note : "))

# Calculer la moyenne avec la fonction
moyenne_etudiant = moyenne(note1, note2, note3)

# Afficher la phrase en fonction de la moyenne
if 15 <= moyenne_etudiant <= 20:
    print("Très bon élève")
elif 11 <= moyenne_etudiant < 15:
    print("Bon élève")
elif 8 <= moyenne_etudiant < 11:
    print("Élève moyen")
elif 0 <= moyenne_etudiant < 8:
    print("Élève devant faire des efforts")
else:
    print("Note invalide")


