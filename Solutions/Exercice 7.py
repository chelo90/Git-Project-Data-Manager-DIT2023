"""
Exercice 7:
-----------
Soit le programme suivant,
- saisissez le à l'aide de Idle,
- sauvegardez le dans un fichier nommé triangle_while_loop.py, puis executez le:

#Imprtation de la librairie turtle pour dessiner
import turtle
#Creation de la variable tr en l'utilisant comme alias de de la librairie turtle()
tr = turtle.Turtle()

#Declaration de la variable pixels et affectation de la valeur 200
pixels = 200
#Declaration de la variable side_count et initialisation a 0 
side_count = 0

#Declaration d'une boucle While et utilsation de la condition side_count < 3
#Repeter la boucle while tant que la variable side_count<3
while side_count < 3:
#Condition si side_count est égal a la valeur initial 0, la prémière itération de la boucle
    if side_count == 0:
#Declaration et initalisation de la variable angle a 0 lors de la première itération de la boucle while
        angle = 0
#Si la variable side_count est différent de 0, donc la boucle n'est pas à la prémière itération le programme execute le sinon
    else:
#Si la boucle n'est pas a sa premiere ittération la variable angle reçois la valeur 120 
        angle = 120
# la variable tr de la librairie dessine en utilsant la fonction left(valeur) pour changer de direction avec une valeur en parametre mesurer en dégré ou radian
    tr.left(angle)
 # la variable tr de la librairie dessine en utilsant la fonction forward(valeur) pour avancer avec une valeur en parametre qui determine la distance a avancé 
    tr.forward(pixels)
#incrementation de la variable side_count pour la bouble 
    side_count = side_count + 1
#Cette fonction est utilisée pour entrer dans la boucle principale jusqu'à ce que la souris soit cliquée
turtle.exitonclick()

- Expliquez ce que fait le programme, ligne par ligne.
- Inspirez vous du programme précédent et écrivez en un pour tracer un carré orange incliné de 30 degré sur la gauche
- Inspirez vous du programme précédent et écrivez en un pour tracer un rectangle bleu incliné de 45 degré sur la droite

"""

#Importation de la librairie turtle pour dessiner
import turtle
#Creation de la variable tr en l'utilisant comme alias de de la librairie turtle()
tr = turtle.Turtle()

#Declaration de la variable pixels et affectation de la valeur 200
pixels = 200
#Declaration de la variable side_count et initialisation a 0 
side_count = 0

#Declaration d'une boucle While et utilsation de la condition side_count < 3
#Repeter la boucle while tant que la variable side_count<3
while side_count < 3:
#Condition si side_count est égal a la valeur initial 0, la prémière itération de la boucle
    if side_count == 0:
#Declaration et initalisation de la variable angle a 0 lors de la première itération de la boucle while
        angle = 0
#Si la variable side_count est différent de 0, donc la boucle n'est pas à la prémière itération le programme execute le sinon
    else:
#Si la boucle n'est pas a sa premiere ittération la variable angle reçois la valeur 120 
        angle = 120
# la variable tr de la librairie dessine en utilsant la fonction left(valeur) pour changer de direction avec une valeur en parametre mesurer en dégré ou radian
    tr.left(angle)
 # la variable tr de la librairie dessine en utilsant la fonction forward(valeur) pour avancer avec une valeur en parametre qui determine la distance a avancé 
    tr.forward(pixels)
#incrementation de la variable side_count pour la bouble 
    side_count = side_count + 1
#Cette fonction est utilisée pour entrer dans la boucle principale jusqu'à ce que la souris soit cliquée
turtle.exitonclick()




#- Inspirez vous du programme précédent et écrivez en un pour tracer un carré orange incliné de 30 degré sur la gauche
import turtle as tr
tr.color("orange")
pixels = 100 
side_count = 0
while side_count < 4: 
    if side_count == 0: 
        angle = 0 
    elif side_count == 1:
        angle = 150
    elif side_count == 2:
        angle = 30
    else:
        angle = 150
    tr.left(angle)
    tr.forward(pixels)
    side_count = side_count + 1



#- Inspirez vous du programme précédent et écrivez en un pour tracer un rectangle bleu incliné de 45 degré sur la droite
import turtle as tr
tr.color("orange")
Longueur = 200 
Largeur = 100
side_count = 0
while side_count < 4: 
    if side_count == 0: 
        angle = 0 
        tr.left(angle)
        tr.forward(Longueur)
    elif side_count == 1:
        angle = 45
        tr.left(angle)
        tr.forward(Largeur)

    elif side_count == 2:
        angle = 135
        tr.left(angle)
        tr.forward(Longueur)

    else:
        angle = 45
        tr.left(angle)
        tr.forward(Largeur)

    side_count = side_count + 1