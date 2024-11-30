def noter_etudiant(note):
    if note < 40:
        return "Échec", note  # L'étudiant échouera
    else:
        # Arrondir à la hausse si la note est à moins de 5 points d'un multiple de 10
        if note % 10 >= 5:
            note_arrondie = (note // 10 + 1) * 10  # Arrondir à la dizaine supérieure
        else:
            note_arrondie = note  # Pas d'arrondi si la note est déjà un multiple de 10 ou proche

        return "Réussi", note_arrondie

# Exemple de test
note = int(input("Entrez la note de l'étudiant (0 à 100) : "))

resultat, note_finale = noter_etudiant(note)

print(f"Résultat : {resultat}")
print(f"Note finale : {note_finale}")