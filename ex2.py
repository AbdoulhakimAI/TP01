# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

nombre_de_filtre=1
nombre_lampes=3
quantité_chlore=0.5

water_quantity =int(input ("Quelle quantité d'eau faut-il assainir?"))

n_filtre= water_quantity*nombre_de_filtre/5
n_light= water_quantity*nombre_lampes/5
Kg_Chlorine= water_quantity*quantité_chlore/5

print("Voici les éléments requis pour assainir {water_quantity}L d'eau:\n"
     "\t- Filtre(s) : {n_filter}\n"
     "\t- Lampe(s) UV : {n_light}\n"
     "\t- Chlore : {kg_chlorine}kg\n")
