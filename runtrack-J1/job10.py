# job10
# montant_initial = float(input("Entrez le montant initial de l'investissement (€) : "))
# taux_rendement = float(input("Entrez le taux de rendement annuel en pourcentage : "))

montant_initial = 0.00
taux_rendement = 0.00

#L'investisseur augmente son capital de 5000€ et le taux de rendement augmente de 2%
montant_final = montant_initial + 5000
taux_rendement = taux_rendement + 2
print("Le montant initiale à augmenté de 5000€")
print("Le taux de rendement à augmenter de 2%")
# Calcul du nouveau gain après l'augmentation du capital et du taux
montant_final = montant_final * (1 + taux_rendement / 100)

# 3. L'investisseur retire 10% du montant total, ce qui diminue le taux de rendement de 1%
montant_final = montant_final * 0.90  # Retrait de 10%
taux_rendement = taux_rendement - 1  # Réduction du taux de rendement de 1%

# Calcul du montant final après le retrait et la réduction du taux
montant_final = montant_final * (1 + taux_rendement / 100) 