# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

nombre_de_filtre=1
nombre_lampes=3
quantité_chlore=0.5

water_quantity =int(input ("Quelle quantité d'eau faut-il assainir?"))

print("Voici le élements requis pour assainir ", water_quantity,"L d'eau:")
print("\t -Filtres:", (water_quantity*nombre_de_filtre/5))
print("\t -Lampes UV:", (water_quantity*nombre_lampes/5))
print("\t -Chlore: ",(water_quantity*quantité_chlore/5))

