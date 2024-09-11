# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity =int(input ("Entrez la quantité d'eau à assainer:"))

nbfiltreinitial=1
nblampesintial=3
qttechloreinitial=0.52

print("le nombre de filtre utilisé est :", (water_quantity*nbfiltreinitial/5))
print("Le nombre de lampes utilisées est:", (water_quantity*nblampesintial/5))
print("La qunatité de chlore utilisée est: ",(water_quantity*qttechloreinitial/5))

