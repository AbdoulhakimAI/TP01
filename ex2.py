# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.
# Exercice 2 Abdoulhakim
water_quantity = int(input("Quelle est la quantité d'eau à filtrer en litre ? : "))

nombre_de_filtre = water_quantity * 0.2
nombre_lampe = water_quantity * 0.6
quantité_de_chlore = water_quantity * 0.1

print("Voici les quantités nécessaires pour chacune des trois catégories pour ", water_quantity , "litres : ")
print("\t -Le nombre de filtre nécessaire est : ", nombre_de_filtre)
print("\t -Le nombre de lampe nécessaire est : ", nombre_lampe)
print("\t -La quantité de chlore en kg est : ", quantité_de_chlore)



