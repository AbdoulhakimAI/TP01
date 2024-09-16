# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = int(input("Pourcentage de batterie ?"))

if 50<battery_level<= 100:
    print(round(battery_level*2,1),"km\n")

if 25<battery_level<=50:
    print(round(battery_level*0.5, 1),"km\n")

if 10<battery_level<=25:
    print(round(battery_level*1, 1),"km\n")

if 5<battery_level<=10:
    print(round(battery_level*2.5, 1),"km\n")

if 0<battery_level<=5:
    print(round(battery_level*6, 1),"km\n")

if battery_level==0:
    print("La batterie est vide\n")