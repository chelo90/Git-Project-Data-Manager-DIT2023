"""
Exercice 3
----------
Soit le programme suivant:

#Importation de la librairie Turtle
import turtle

#declaration de la variable 
polygon = turtle.Turtle()

#declaration de la valeur color et l'initialisation a "green"
color = "green"
#declaration de la valeur num_sides et l'initialisation a 6 : nombre de coté
num_sides = 6
#declaration de la valeur side_length et l'initialisation a 70 : longueur de coté
side_length = 70
#declaration de la valeur angle et l'initialisation a 360.0/ num_sides : angle = 360 divisé par le nombre de coté
angle = 360.0 / num_sides
#Determination de la couleur du polygon dans la fonction color du turtle
polygon.color(color)
#Boucle for qui par de 0 au nombre de cote-1
for i in range(num_sides):
#appel a la fonction forward et en paramètre la longueur du coté
    polygon.forward(side_length)
#appel a la fonction right et en parametre la taille de l'angle 
    polygon.right(angle)

turtle.exitonclick()

En vous inspirant du programme précédent, écrivez un programme qui demande à l'utilisateur
- "quelle figure voulez vous tracer?"
- "de quelle couleur doit être le contour de la figure?"

L'utilisateur devra saisir le nom d'un figure puis le nom d'une couleur
Le programme devra tracer cette figure en respectant la couleur choisie
Les figures acceptées sont:
- "cylindre", "cône", "pyramide", "prisme hexagonal"
"""

#Importation de la librairie Turtle
import turtle

#declaration de la variable 
polygon = turtle.Turtle()

#declaration de la valeur color et l'initialisation a "green"
color = "green"
#declaration de la valeur num_sides et l'initialisation a 6 : nombre de coté
num_sides = 6
#declaration de la valeur side_length et l'initialisation a 70 : longueur de coté
side_length = 70
#declaration de la valeur angle et l'initialisation a 360.0/ num_sides : angle = 360 divisé par le nombre de coté
angle = 360.0 / num_sides
#Determination de la couleur du polygon dans la fonction color du turtle
polygon.color(color)
#Boucle for qui par de 0 au nombre de cote-1
for i in range(num_sides):
#appel a la fonction forward et en paramètre la longueur du coté
    polygon.forward(side_length)
#appel a la fonction right et en parametre la taille de l'angle 
    polygon.right(angle)

turtle.exitonclick()


"""
En vous inspirant du programme précédent, écrivez un programme qui demande à l'utilisateur
- "quelle figure voulez vous tracer?"
- "de quelle couleur doit être le contour de la figure?"

L'utilisateur devra saisir le nom d'un figure puis le nom d'une couleur
Le programme devra tracer cette figure en respectant la couleur choisie
Les figures acceptées sont:
- "cylindre", "cône", "pyramide", "prisme hexagonal"
"""