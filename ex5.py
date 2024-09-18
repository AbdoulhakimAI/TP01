#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country=input("Pays concerné ?")
code_medals=input("Chaine représentant les médailles ?")

set1=set(code_medals)
set2=set("G" +"S" +"B")

if set1 == set2:
 print(f"""\n- {code_medals.count}("S") OR\n- {code_medals.count}("B") Argent\n- {code_medals.count}('G')Bronze\n""")

else: 
    print("Ceci est une chaîne invalide. Veuillez entrer une chaîne valide")
#github abdul