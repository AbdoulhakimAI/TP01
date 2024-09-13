# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math
speed = float(input("Quelle est la vitesse initiale : "))
angle = float(input("Quelle est l'angle de lancé : "))
distance = abs(round(((speed**2 * math.sin(2*angle))/9.8), 2))

print("La distance maximale du lancer est : ", distance)

