# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

nombre_de_filtre=1
nombre_lampes=3
quantité_chlore=0.5

water_quantity =float(input ("Quelle quantité d'eau faut-il assainir ?"))

n_filtre= int(water_quantity*nombre_de_filtre/5)
n_light= int(water_quantity*nombre_lampes/5)
Kg_Chlorine= float(water_quantity*quantité_chlore/5)

print(f""" Voici les éléments requis pour assainir {water_quantity}L d'eau:
\t- Filtre(s) : {n_filtre}
\t- Lampe(s) UV : {n_light}
\t- Chlore : {Kg_Chlorine}kg""")
