"""Exercice 6:
-----------
Soit le programme suivant:

counter = 0
end_value = 100
print("counter value", counter)
while counter <= end_value:
    print(counter)
    counter = counter + 1
print("counter value", counter)

- Expliquez ce que fait le programme, ligne par ligne
- Quelle est la différence entre une boucle for et une boucle while?
- Ecrivez le programme précédent en utilisant une boucle for
- Inspirez vous du programme précédent pour en écrire un qui:
  - affiche les nombres allant de 10 à 20 en comptant de 2 en 2
  - affiche les nombres allant de 20 à 10 en comptant de 4 en 4
"""
#Initialisation d'un compteur a 0
counter = 0
#Valeu finale
end_value = 100
#Affichage du compteur
print("counter value", counter)
#Boucle while qui reperatera son instruction tant que le compteur est inferieur a la valeur finale
while counter <= end_value:
#Affichage du compteur dans la boucle
    print(counter)
#Incrementation du compteur dans la boucle
    counter = counter + 1
#Affichage du compteur finale apres la bouclee
print("counter value", counter)

#la principale différence entre une boucle foret une boucle whileréside dans le fait que la boucle forest utilisée pour un nombre d'itérations déterminées à l'avance, tandis que la boucle whileest utilisée lorsque vous devez répéter un bloc de code tant qu' une condition est vraie.

for i in range(0,end_value+1):
    print(i)
    counter =+i
print("counter value", counter)

# - affiche les nombres allant de 10 à 20 en comptant de 2 en 2
for i in range(10,20,2):
    print(i)

# - affiche les nombres allant de 20 à 10 en comptant de 4 en 4
for i in range(20,10,-4):
    print(i)