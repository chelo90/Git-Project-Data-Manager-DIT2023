"""
EXercice 2:
-----------
Ecrivez un programme qui demande à l'utilisateur
- "longeur? "
- "largeur? "

Le programme devra ensuite calculer et afficher:
- la surface est ...
- le perimetre est ...

Le programme devra ensuite demander à l'utilisateur s'il veut tracer le rectangle:
- Si l'utilisateur répond "oui", tracer la figure puis afficher "aurevoir"
- Si l'utilisateur répond "non", afficher un message: "aurevoir"
"""

import turtle

longueur = float(input("Veuillez entrer la longueur du rectangle : "))
largeur = float(input("Veuillez entrer la largeur du rectangle : "))

surface = longueur * largeur
perimetre = 2 * (longueur + largeur)

print("La surface est :", surface)
print("Le perimetre est :", perimetre)

tracer_rectangle = input("Voulez-vous tracer le rectangle ? (oui/non) ")

if tracer_rectangle.lower() == "oui":
    tur = turtle.Turtle()
    tur.forward(longueur)  # Déplace la tortue de la longueur vers l'avant
    tur.left(90)  # rotation de la tortue de 90 degrés
    tur.forward(largeur)  # Déplace la tortue de la largeur vers l'avant
    tur.left(90)  # rotation de la tortue de 90 degrés
    tur.forward(longueur)  # Déplace la tortue de la longueur vers l'avant
    tur.left(90)  # rotation de la tortue de 90 degrés
    tur.forward(largeur)  # Déplace la tortue de la largeur vers l'avant
    tur.left(90)  # rotation de la tortue de 90 degrés
    turtle.done()
else:
    print("Au revoir")

