# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = float(input("Pourcentage de batterie ?"))

if 50<battery_level<= 100:
    variable1= (5*6) + (5*2.5) + (15*1) + (25*0.5) + (battery_level-50)*2
    print(f"{variable1: .1f} km")

elif 25<battery_level<=50:
    variable2= (5*6) + (5*2.5) + (15*1) + (battery_level-25)*0.5
    print(f"{variable2: .1f} km")

elif 10<battery_level<=25:
    variable3= (5*6) + (5*2.5) + (battery_level-10)*1
    print(f"{variable3: .1f} km")

elif 5<battery_level<=10:
    variable4= (5 * 6) + (battery_level-5)*2.5
    print(f"{variable4: .1f} km")

elif 0<battery_level<=5:
    variable5= battery_level *6
    print(f"{variable5: .1f} km")

if battery_level== 0:
    print(" La batterie est vide")