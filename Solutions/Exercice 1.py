"""
Exercice 1:
-----------
Ecrire un programme qui demande à l'utilisateur de saisir un nombre N.
Le programme devra ensuite calculer puis afficher la somme des nombres compris entre 1 et N.


Par exemple, si l'utilisateur tape le nombre 10,
Le programme devra afficher 55 çad: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
"""
try:
  N = input("Entrer un entier : ")
  val = int(N)
  somme = 0
  for i in range(1,val+1):
    somme+=i
  print("La somme est :",somme)
except:
  print("La valeur saisie n'est un entier")




