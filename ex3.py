# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math

speed = float(input("Vitesse initiale (en m/s):"))
angle = float(input("Angle de lancement (en degrés):"))
gravitational_constant=9.8
distance=((speed**2)*(math.sin(math.radians(2*angle))))/gravitational_constant

distance=abs(round(distance,2))
print("Distance parcourue: {distance}m\n")