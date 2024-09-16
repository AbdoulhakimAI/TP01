# TODO: Créer un script permettant le formattage du livre des records des JO.

#TODO: pour la categorie si c nul comment fait on pour fixer une valeur?


#exercice 1 alexa
country =str(input("De quelle nationalité est l'athlète ? "))
athlete = str(input("C'est quoi le nom de l'athlète?"))
date = str(input("Quelle est la date du record?"))
sport= str(input("C'est quoi sa discipline?"))
category= str(input("Dans quelle catégorie spécifiquement?"))
record= str(input("Quel est son record?"))
print(f"\nNouveau Record:\n--------------------\n {date} - {sport} - {category}:\n\t{athlete} ({country}) - {record}\n")
        
