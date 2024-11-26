# Job 9
nom="nom"
prix_unitaire=100
quantite_stock=1

quantite_stock=quantite_stock+5
print(quantite_stock)

print(f'le nom du produit est: {nom}')
print(f'le prix unitaire est: {prix_unitaire}')
print(f'quantite_en_stock est: {quantite_stock}')

# Demander à l'utilisateur combien de produits il souhaite acheter
quantite_achetee = int(input("Combien de produits souhaitez-vous acheter ? "))

# Vérifier si la quantité demandée est disponible en stock
if quantite_achetee <= quantite_stock:
    # Mettre à jour le stock
    quantite_stock -= quantite_achetee
    print(f"Achat effectué. Il reste {quantite_stock} produits en stock.")
else:
    print(f"Désolé, il n'y a pas assez de produits en stock pour cette commande. Il reste {quantite_stock} produits disponibles.")

    quantite_achetee = int(input("Combien de produits souhaitez-vous acheter ? "))
    print(f"Achat effectué. Il reste {quantite_stock} produits en stock.")

# prix inital du produit 
# prix_unitaire=100
# Augmentation de 10% en raison de l'inflation
prix_avec_inflation = prix_unitaire * 1.10
#Affihage du nouveau prix 
print(f"Le prix après l'inflation est: {prix_avec_inflation}")

print(f'le nom du produit est: {nom}')
print(f'le prix unitaire est: {prix_unitaire}')
print(f'quantite_en_stock est: {quantite_stock}')