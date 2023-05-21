# Git-Project
Projet Git_DAMA du Groupe 04
Membres du Groupe:
1- SANOU Marcellin
2- DIALLO Saifoulaye

**********************************************************************************************************************************************************
DIRECTIVES DE L'ENSEIGNANT
Crééer un dépôt contenant au moins deux repertoires: énoncés et solutions dans le repertoire solutions: plusieurs fichier Python, un fichier par solution
si nécessaire: travaillez à deux ou à trois, en utilisant des branches.
Bon courage à tous et à toutes
**********************************************************************************************************************************************************

Exercice 0
----------
- Executez chacune des boucles suivantes

for i in range(10, 15):
    print(i)

for i in range(20,40,2):
    print(i)

for i in range(20):
    if i%2 == 0:
       print(i)

for i in range(20):
    if i%2 != 0:
       print(i)

- Analysez puis expliquez avec un maximum de détail ce que fait chaque boucle
- En vous inspirant des boucles précédentes, écrire une boucle:
  - qui affiche les nombres de 0 à 1000 de 2 en 2
  - qui affiche les nombres de 0 à 1000 de 10 en 10
  - qui affiche les nombres de 0 à 1000 de 100 en 100
  - qui affiche les nombres de -15 à 15
  - qui affiche les nombres de -30 à 30 de 5 en 5
  - qui affiche les nombres de 50 à 100 de 3 en 3

Exercice 1:
-----------
Ecrire un programme qui demande à l'utilisateur de saisir un nombre N.
Le programme devra ensuite calculer puis afficher la somme des nombres compris entre 1 et N.

Par exemple, si l'utilisateur tape le nombre 10,
Le programme devra afficher 55 çad: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10


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


Exercice 2
----------
Soit le programme suivant:

import turtle

polygon = turtle.Turtle()

color = "green"
num_sides = 6
side_length = 70
angle = 360.0 / num_sides

polygon.color(color)

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.exitonclick()

En vous inspirant du programme précédent, écrivez un programme qui demande à l'utilisateur
- "quelle figure voulez vous tracer?"
- "de quelle couleur doit être le contour de la figure?"

L'utilisateur devra saisir le nom d'un figure puis le nom d'une couleur
Le programme devra tracer cette figure en respectant la couleur choisie
Les figures acceptées sont:
- "cylindre", "cône", "pyramide", "prisme hexagonal"


Exercice 3:
-----------
Ecrivez un programme qui demande à l'utilisateur d'entrer
- t: sa taille en m (convertir t en nombre réel)
- m: sa masse en kg (convertir m en nombre réel)

Le programme devra ensuite calculer et afficher l'indice de masse corporelle et l'afficher:
- IMC = m / t²

Si IMC est:
- inférieur à 16,5: le programme devra afficher le message: "dénutrition"
- compris entre 16,5 et 18,5: "maigreur"
-         entre 18,5 et 25: "masse normale"
-         entre 25 et 30: "surpoids"
- supérieur à 30: "obésité"


Exercice 4:
-----------
- Ecrire un programme qui utilise turtle pour écrire (dessiner) votre nom
- Ecrire un programme qui utilise turtle pour écrire (dessiner) votre nom (chaque lettre ayant une couleur différente)


Exercice 5:
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


Exercice 6:
-----------
Soit le programme suivant,
- saisissez le à l'aide de Idle,
- sauvegardez le dans un fichier nommé triangle_while_loop.py, puis executez le:

import turtle
tr = turtle.Turtle()

pixels = 200
side_count = 0

while side_count < 3:
    if side_count == 0:
        angle = 0
    else:
        angle = 120

    tr.left(angle)
    tr.forward(pixels)
    side_count = side_count + 1

turtle.exitonclick()

- Expliquez ce que fait le programme, ligne par ligne.
- Inspirez vous du programme précédent et écrivez en un pour tracer un carré orange incliné de 30 degré sur la gauche
- Inspirez vous du programme précédent et écrivez en un pour tracer un rectangle bleu incliné de 45 degré sur la droite


Exercice 7:
-----------
Soit la liste de coordonnées de points x,y sous la forme d'une liste de tuples:
coordinates = [(4,5), (9,3), (12,8), (13,7), (18,6), (20,9)]
- Créez une liste vide d’ordonnées: ordinates = [].
- Remplissez la liste d’ordonnées en parcourant la liste coordinates.
- Affichez la liste ordinates.
- Créez un dictionnaire dict_coordinates à partir de la liste coordinates

On veut borner à 7 toutes les ordonnées y de la liste coordinates qui sont supérieures à 7
Après votre traitement, affichez coordinates, qui devrait contenir :
[(4,5), (9,3), (12,7), (13,7), (18,6), (20,7)]
Vous proposerez trois manières de faire


Exercice 8:
-----------
- importez le module math
- parcourez la documentation du module: help(math)
- choisissez dix fonctions dans ce module
- pour chaque fonction choisie, donnez une explication et deux démonstrations
https://docs.python.org/fr/3.10/library/math.html

Exercice 9:
-----------
écrire un programme qui :
- demande à l'utilisateur de saisir le rayon de la base du cylindre,
- demande à l'utilisateur de saisir la hauteur du cylindre
- calcule le volume du cylindre
- affiche le volume du cylindre arrondi à 3 chiffres après la virgule

Exercice 10:
------------
écrire un programme qui :
- demande à l'utilisateur de saisir le rayon de la base du cylindre,
- demande à l'utilisateur de saisir la hauteur du cylindre
- définit une fonction f qui:
  - prend 3 paramètres: rayon r, hauteur h, nombre n
  - calcule le volume v du cylindre de rayon r et de hauteur h
  - renvoie le volume v, arrondi à n chiffres après la virgule
- utilise la fonction f pour calculer le volume v
- affiche v

Exercice 11:
-----------
écrire un programme qui
- demande à l'utilisateur de saisir un nombre
- stocke ce nombre dans une variable n
- additionne chaque chiffre du nombre n
- affiche cette somme
Vous proposerez deux solutions: avec un for et avec un while

Exercice 12:
------------
écrire un programme qui
- demande à l'utilisateur de saisir des nombres séparés par des "@"
- enregistre chacun de ces nombres dans une liste
- classe les nombres par ordre décroissant
- affiche la liste

Exercice 13:
------------
écrire un programme qui:
- définit une fonction h
  - qui prend en paramètre un nombre n
  - calcule le reste de la division n/2
- demande à l'utilisateur un nombre N
- appelle la fonction h avec le nombre N

D'après vous, comment écrire une fonction qui vous dit
- si vrai ou faux un nombre est impair ?
- si vrai ou faux un nombre est pair ?


Exercice 14:
------------
écrire un programme qui:
- définit une liste ne contenant que des voyelles
- définit une liste ne contenant que des consonnes
- définit une liste ne contenant que la lettre "y"
- demande à l'utilisateur de saisir une lettre
- vérifie si la lettre saisie est une voyelle ou une consonne
- affiche l'un des 2 messages suivants
  - disant à l'utilisateur: "vous avez saisi une ..."
  - "y est parfois considéré comme une voyelle, parfois non"

Exercice 15:
------------
écrire un programme qui:
- définit un dictionnaire contenant des célébrations, ex: {"Nouvel an": "1 Janvier", "Tabaski": "10 Juillet", "Pentecote": "5 Juin"}
- demande à l'utilisateur de:
  - saisir le jour
  - saisir le mois
- vérifie si la date saisie correspond à une date de célébration
  - si oui, afficher la célébration en question
  - si non, afficher le message: "Cette date ne correspond à aucune célébration"

* Attention:
- même si l'utilisateur saisit "1 jAnViEr", le programme sera capable de reconnaitre qu'il s'agit du nouvel an


Exercice 16:
------------
Soit le programme suivant:

import random
import math

lower = int(input("saisir borne inférieure: "))
upper = int(input("saisir borne supérieure: "))

x = random.randint(lower, upper)
print("\n\tVous avez ",
	round(math.log(upper - lower + 1, 2)),
	" chances pour trouver le nombre exact!\n")

count = 0

while count < math.log(upper - lower + 1, 2):
	count += 1
	guess = int(input("Devinez le nombre:- "))
	if x == guess:
		print("Felicitations vous avez trouvé en ",
			count, " essais")
		break
	elif x > guess:
		print("Trop petit!")
	elif x < guess:
		print("Trop grand!")

if count >= math.log(upper - lower + 1, 2):
	print("\nLe nombre était %d" % x)
	print("\tLa prochaine fois peut-être!")

- saisissez le
- executez le
- expliquez ce que fait ce programme globalement
- précédez chaque ligne de code d'un commentaire et expliquez chaque ligne de code


Exercice 17:
------------
il existe un module nommé time dans votre système
et à l'intérieur de ce module, il y a une fonction: asctime
lire la doc, donner un exemple d'utilisation de cette fonction

Exercice 4:
Soit le programme suivant:
course = input("Course ? ")
grade = input("Grade ? ")
result = [course, grade]
line = ": ".join(result)
save = input("save to a file ? (yes or no) ")
if save == "yes":
    filename = input("file name (ending with '.txt' for saving ? ")
    f = open(filename, "a")
    f.write(f"{line} \n")
    f.close()

- executez le programme et expliquez ce qu'il fait
- expliquez chaque ligne en détails
- écrire une procédure qui
  - prend 4 paramètres ayant des valeurs par défaut
  - et effectue le même traitement


Exercice 18:
------------
Soit le tableau suivant (matériau --> densité)
Polystyrene: 20 kg/m3
Liège: 220 kg/m3
Rhénium: 21020 kg/m3
Platine: 21450 kg/m3

Soit un cube de 858g et de volume 40cm3.
Ecrire le programme qui détermine
- la densité de ce cube
- le matériau utilisé pour faire ce cube
Transformez le programme en fonction prenant 4 paramètres que vous définirez


Exercice 19:
------------
Ecrire une fonction qui prend:
- 4 paramètres, r1, u1, r2, u2
- r1 et r2 sont des nombres flottants, representant des valeurs de résistances
- u1 et u2 sont des chaines de caractères representant l'unité de ces résistances
La fonction devra
- effectuer l’affichage formaté (deux chiffres significatifs) de la résistance équivalente en
série et en parallèle. Ne pas oublier l’unité
inside: on peut utiliser "\u2126" pour afficher un joli Ω


Exercice 20:
------------
Ecrire une fonction qui
- demande un entier de depart i et un entier d'arrivée j
- calcule la somme des entiers compris entre i et j de trois façons différentes :
  - en utilisant la formule classique : s = n n 1 / 2
  - en utilisant une boucle while
  - en utilisant une boucle for

Exercice 21:
------------
A.
Soit la variable chaine suivante:
chaine = "Un pays que je veux remttre sur pied"
- Ecrire un programme qui prend n'importe quelle chaine de caractères
- Et dans cette chaine, remplace "je veux" (s'il existe) par "Assim veut".

B.
Découper ensuite chaine en une liste de mots, stockée dans une variable liste_mots.
Vous proposerez deux manières de faire.

C.
A partir de liste_mots:
- créer un dictionnaire qui contiendra:
  - comme clés, chaque mot,
  - comme valeurs, le nombre d'occurence de chaque mot
Vous proposerez deux manières de faire.

Faites, A, B, et C à l'aide de fonctions dont vous définirez:
- les paramètres
- les valeurs retournées

Exercice 22:
------------
Écrire une fonction piepie
- qui prend n.
- et retourne une valeur approchée de π, sachant que:

∞
∑ 1/i^2 = 2/6
i=1

Vous aurez besoin:
- d'une boucle
- du module math (from math import sqrt, pi)

Ensuite ecrire un programme qui
- fait varier n
- et pour chaque n:
  - affiche la valeur retournée par la fonction piepie et l'erreur
  - affiche l’erreur relative (en pourcentage) entre la valeur de pi calculée et celle fournie par le module mat

Exercice 23:
------------
Soit la fonction suivante:

def test(n):
    return n % 34 == 4 and n > 4 ** 4

Pouvez vous expliquer en détail ce que fait cette fonction?
Pouvez vous la réécrire d'une autre manière ?

Exercice 24:
-----------
Écrire un programme qui
- demande à l’utilisateur de saisir une liste de mots séparés par des virgules.
- fabrique un dictionnaire vide “D”
- parcourt la liste de mots
- si le mot possède au moins 3 lettres
  * ajoute dans le dictionnaire “D” le mot comme étant la clé, la longueur du mot comme étant la valeur

Par exemple, si la liste de mots est : ['cat', 'at', 'car', 'fear', 'center'],
alors le dictionnaire sera {'cat': 3, 'car': 3, 'fear': 4, 'center: 5'}


Exercice 25:
------------
Soit (lat1, lng1) and (lat2, lng2), la latitude et la longitude deux deux points sur la surface de la Terre.
La distance en kilomètres entre ces deux points se calcule en utilisant la formule suivante :
- distance = 6371.01 × arccos(sin(lat1) × sin(lat2) + cos(lat1) × cos(lat2) × cos(lng1 − lng2))

Écrire un programme qui devra :
• définir une fonction calculant la distance
• demander à l’utilisateur de :
  – saisir lat1 (on assume que cette valeur est en degrés)
  – saisir lng1 (on assume que cette valeur est en degrés)
  – saisir lat2 (on assume que cette valeur est en degrés)
  – saisir lng2 (on assume que cette valeur est en degrés)
• convertir les 4 valeurs saisies en radians
• calculer la distance en utilisant la fonction définie plus haut
• afficher : “la distance entre le point de coordonnées (lat1, lng1) et le point de coordonnées (lat2, lng2) est de
XXX kilometres”

Exercice 26:
------------
Soit le programme suivant:

import operator

lst1 = list(range(1200, 2000, 135)) # (1)
lst2 = [i * 2 for i in lst1 if i % 2 == 0] # (2)
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
o = list(filter(lambda x: operator.mod(x 2) == 0, numbers))
e = list(filter(lambda x: operator.mod(x, 2) != 0, numbers))

print(lst1)
print(lst2)
print(o)
print(e)

Après avoir bien compris ce que fait le programme précédent, écrivez en un autre qui fait exactement la même chose (en utilisant des boucles et des conditions). Il existe une autre manière d’additionner deux nombres entiers, pouvez vous dire quelle est cette manière et ensuite donner un exemple?


Exercice 27:
------------
Exercice:
Ecrire un programme qui demande à l'user de saisir:
- nom
- prenom
- age
- adresse
- nombre de notes à saisir
- pour quelle matière saisir ces notes
- les notes en question

Le programme devra ensuite fabriquer un dictionnaire tel que:
student1 = {"Fullname": "Patrick Nsukami", "birthdate": "1980/01/01", "matières": {"maths": [45, 56, 78]}}


Exercice 28:
------------
En partant du dictionnaire suivant:
student1 = {"Fullname": "Patrick Nsukami", "birthdate": "1980/01/01", "matières": {"maths": [45, 56, 78]}}

Demandez à l'utilisateur de saisir:
- une nouvelle matière
- le nombre de notes pour cette nouvelle matière
- les notes en question

Le programme devra ensuite modifier le dictionnaire initial tel que:
student1 = {"Fullname": "Patrick Nsukami",
            "birthdate": "1980/01/01",
            "matières": {"maths": [45, 56, 78], "english": [34, 67, 89]}}

Le programme devra enfin afficher
"Votre nom est: ..., votre date de naissance est: ..., vous avez une moyenne de ... en ... et vous avez une moyenne de ... en ..."

Exercice 29:
------------
Ecrire une fonction qui prend en paramètre une chaine de caractère
La fonction devra renvoyer vrai si la chaine est un palindrome, faux autrement.

Exercice 30:
------------
Initialisez deux entiers : x = 0 et y = 10.
Écrire une boucle affichant et incrémentant la valeur de x tant qu’elle reste inférieure à celle de y.
Écrire une autre boucle décrémentant la valeur de y et affichant sa valeur si elle est impaire.
Boucler tant que y n’est pas nul.

Exercice 31:
------------
Définir la liste suivante:
lst = [55, 17, 38, 10, 25, 72, 567, 122, 369]

puis effectuez les actions suivantes :
– triez et affichez la liste ;
– ajoutez l’élément 12 à la liste et affichez la liste ;
– renversez et affichez la liste ;
– affichez l’indice de l’élément 17 ;
– enlevez l’élément 38 et affichez la liste ;
– affichez la sous-liste du 2eau 3eélément ;
– affichez la sous-liste du début au 2eélément ;
– affichez la sous-liste du 3eélément à la fin de la liste ;
– affichez la sous-liste complète de la liste ;

Exercice 32:
------------
Définir deux ensembles suivants :
X = {'a', 'b', 'c', 'd' }
Y = {'s', 'b', 'd' }

puis affichez les résultats suivants :
– les ensembles initiaux ;
– le test d’appartenance de l’élément 'c' à X ;
– le test d’appartenance de l’élément 'a' à Y ;
– les ensembles X − Y et Y − X ;
– l’ensemble X ∪ Y (union) ;
– l’ensemble X ∩ Y (intersection).

Exercice 33:
------------
Écrire une fonction compterMots ayant un argument (une chaîne de caractères)
La fonction renvoie un dictionnaire qui contient la fréquence de tous les mots de la chaîne entrée.

Exercice 34:
------------
Un entier naturel supérieur à 1 est dit premier s'il possède exactement 2 diviseurs, 1 et lui-même.
On appelle diviseur propre de n, un diviseur quelconque de n, n exclu.
Un entier naturel est dit parfait s’il est égal à la somme de tous ses diviseurs propres ;
Les nombres a tels que : (a + n + n2) est premier pour tout n tel que 0 6 n < (a − 1), sont appelés nombres chanceux.

Écrire un module (nombres.py) définissant quatre fonctions : somDiv, estParfait, estPremier, estChanceux:
• la fonction somDiv retourne la somme des diviseurs propres de son argument;
• les trois autres fonctions vérifient la proprriété donnée par leur définition et retourne un booléen.


Exercice 35:
------------
On désire simuler Pile ou Face à l'aide d'un script dans lequel le chiffre 0 sera associé à Pile et le chiffre 1 à Face.
Écrire le script.

Exercice 36:
------------
Un sac est rempli de 6 billes jaunes et de 14 billes vertes, toutes indiscernables au toucher.
On effectue un tirage au hasard d'une bille du sac et on appelle « succès » le fait d'obtenir la couleur jaune.
Ecrire le programme permettant de calculer la probabilité de chaque couleur en fonction du nbre de billes.
Ecrire le prorgamme qui simule le tirage d'une couleur


Exercice 37:
------------
Veuillez compléter le programme qui suit:

from cmath import sqrt
import matplotlib.pyplot as plt  # type:ignore

class Poly2:
    """ Classe permettant de representer un polynôme de degré 2."""

    def __init__(self, *coeffs):
        """ Méthode constructeur qui prend en paramètre, les coefficients du polynôme"""
        pass

    def __add__(self, other):
        """Addition 2 polynômes et qui renvoi du nouveau polynôme"""
        pass

    def __sub__(self, other):
        """Soustraction de 2 polynômes et renvoi du nouveau polynôme"""
        pass

    def __repr__(self):
        msg = 'Poly2(' + ', '.join([str(c) for c in sorted(self.coeffs.values())]) + ')'
        return msg

    def __str__(self):
        result = [""]+[f"{c}x^{i}" for i, c in sorted(self.coeffs.items()) if c]+[""]
        result = "+".join(reversed(result))
        result = result.replace("+1x", "+x")
        result = result.replace("-1x", "-x")
        result = result.replace("x^0", "")
        result = result.replace("x^1+", "x+")
        result = result.replace("+-", "-")
        result = result.strip("+")
        result = result.replace("+", " + ")
        result = result[:1]+result[1:].replace("-", " - ")
        return result.strip()

    def solve(self):
        """ Méthode qui renvoie les solutions si elles existent."""
        pass

    def __val(self, x):
        """ Méthode qui calcule et renvoie la valeur de y en fonction de x.
        Si: y = x^2 + 1
        Si: x prend pour valeur 5
        Alors: y = 5^2 + 1 = 26
        """
        pass

    def draw(self, x_points=None):
        """ Méthode qui trace la courbe."""
        pass

bar = [1, 2, 3]
p1 = Poly2(*bar)

baz = [1, 2, 3]
p2 = Poly2(*baz)

print(p1+p2)
# --> affiche 2x^2 + 4x + 6

print(p1.solve())
# --> affiche ((-0.3333333333333333+0.47140452079103173j), (-0.3333333333333333-0.47140452079103173j))

p1.draw()



Exercice 38:
------------
Completez le programme suivant:

import turtle

class Shape(turtle.Turtle):
    def __init__(self, color, vertices):
        # pass

    def trace(self):
        # pass

if __name__ == "__main__":
    vertices_list = [[(90, 10), (140, 50), (-10, 60)],  # 3 sommets
                     [(10, 10), (50, 5), (50, 30), (10, 30)],  # 4 sommets
                     [(-10, -10), (-30, 50), (50, 50), (80, 30), (60, -30)]  # 5 sommets
                     ]
    colors_list = ["green", "red", "purple"]
    for v,c in zip(vertices_list, colors_list):
        t = Shape(c, v)
        t.trace()
    turtle.exitonclick()



Exercice 39:
------------
Compléter le programme suivant:

class Currency:
    # dico permettant de faire les conversions entre différentes monnaies
    currencies =  {'CHF': 1.0821202355817312,
                   'CAD': 1.488609845538393,
                   'GBP': 0.8916546282920325,
                   'JPY': 114.38826536281809,
                   'EUR': 1.0,
                   'USD': 1.11123458162018}

    def __init__(self, value, unit="EUR"):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def change(self, new_unit):
        """
        Méthode permettant de convertir l'objet courant vers une autre monnaie
        """
        pass

    def __add__(self, other):
        """
        Addition de monnaies entre elles.
        Si other est un objet de type monnaie,
        alors, convertir vers la monnaie de l'objet self puis additionner
        Si other est un objet de type entier ou réel,
        alors, considérer qu'il s'agit de l'Euro.
        """
        pass

    def __sub__(self, other):
        """
        Soustraction de monnaies entre elles.
        Si other est un objet de type monnaie,
        alors, convertir vers la monnaie de l'objet self puis soustraire
        Si other est un objet de type entier ou réel,
        alors, considérer qu'il s'agit de l'Euro.
        """
        pass

    def __mul__(self, other):
        """
        Multiplication d'une monnaie uniquement avec un nombre.
        Il n'est pas possible de multiplier des monnaies entre elles.
        """
        pass


def main():
    a = Currency(10.00, "EUR")  # Objet de type Currency, valeur 10, monnaie Euro
    b = Currency(10.00, "GBP")
    c = a + b
    d = c * 3
    e = b * 3.5
    f = e - a
    g = f + 3
    print(a)  # 10.00 EUR
    print(b)  # 10.00 GBP
    print(c)  # 21.22 EUR
    print(d)  # 63.65 EUR
    print(e)  # 35.00 GBP
    print(f)  # 26.08 GBP
    f.change("JPY")
    print(f)  # 3346.18 JPY
    print(g)  # 28.76 GBP

if __name__ == "__main__":
    main()


Exercice 40:
------------
Définir une classe Fraction qui aura:

- deux attributs: numérateur et dénominateur
- 7 méthodes:
  - `invert`: renvoie un objet de type Fraction en inversant l'objet lui même.
  - `simplify`: simplifie et renvoie un objet de type Fraction.
  - `__mul__`: multiplie deux objets de type Fraction et renvoie un objet de type Fraction.
  - `__add__`: additionne deux objets de type Fraction et renvoie un objet de type Fraction.
  - `__sub__`: soustrait deux objets de type Fraction et renvoie un objet de type Fraction.
  - `__div__`: divise deux objets de type Fraction et renvoie un objet de type Fraction.
  - `__str__` : affiche l'objet fraction sous la forme "numérateur/dénominateur".
  - `from_string`: crée un objet de type Fraction à partir d'une chaine de caractère. **/!\\**

# complétez le programme suivant afin que la fonction main s'execute sans erreurs:

from math import gcd

class Fraction:
    # votre programme ici
    pass

def main():
    # ne rien changer dans le corps de cette fonction
    f1 = Fraction(2,4); f2 = Fraction(1,4)
    f3 = f1 + f2; f4 = f1 - f2
    f5 = f1 * f2; f6 = f1 / f2
    f7 = Fraction(4,10)
    f8 = Fraction.from_string('5/10')
    print(f3) # affiche: 3/4
    print(f4) # affiche: 1/4
    print(f5) # affiche: 1/8
    print(f6) # affiche: 2
    print(f7.simplify()) # affiche: 2/5
    print(f7.invert()) # affiche: 10/4
    print(f8) # affiche: 5/10

if __name__ == "__main__":
    main()


Exercice 41:
------------
Completer le programme suivant

class Dist:
    __metric = {"mm" : 0.001, "cm" : 0.01, "m" : 1, "km" : 1000,
                "in" : 0.0254, "ft" : 0.3048, "yd" : 0.9144,
                "mi" : 1609.344 }

    def to_metres(self):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, fac):
        pass

    def __str__(self):
        pass

# ne rien changer dans le corps de cette fonction
def run():
    d = Dist(3)
    print(d)  # affiche ====> 3 m

    x = Dist(5, "ft")
    print(x)  # affiche ====> 5 ft

    y = x * 4
    print(y)  # affiche ====> 20 ft

    print(x.to_metres())  # affiche ====> 1.524
    z = Dist(6.5, "yd") + Dist(2)
    print(z)  # affiche ====> 8.687226596675416 yd


run()


Exercice 42:
------------
- A l'aide de matplotlib tracer la courbe telle que x = [1, 2, 3, 4] et y = [1, 4, 9, 16]
- A l'aide de matplotlib tracer le nuage de point tel quel que x = [1, 2, 3, 4] et y = [1, 4, 9, 16].
- Ensuite, ecrire un programme qui demande à l'utilisateur:
  - la liste des abscices
  - la liste des ordonnées
  - s'il veut tracer une courbe ou un nuage de point
  - le programme devra ensuite faire le tracé suivant ce que l'utilisateur aura saisi


Exercice 43:
------------
- Qu'est ce qu'un diagramme en barre ? Dans quel cas il s'utilise ?
- A l'aide de matplotlib, tracer un diagramme en barre representant les données suivantes:
x = ['Pommes, 'Bananes, 'Oranges', Mangues']
y = [20, 15, 25, 10]
- refaire la même chose cette fois ci avec des barres horizontales
- Ensuite, écrire un programme qui trace un diagramme en barre,
  - cette fois ci les données doivent venir d'une table SQL contenant deux colonnes: "nom", "quantité"


Exercice 44:
------------
- Soit l'image suivante: https://imgur.com/a/if5RzBY
- Pouvez vous l'interpreter ?
- A l'aide de mpl, tracer l'histogramme des données suivantes:
x = [1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 4]


Exercice 45:
------------
A l'aide d'un programme Python, creer une table contenant les données suivantes:
- tarif = [20, 30, 10, 40]
- étiquette = ['Pommes, 'Bananes, 'Oranges', Mangues']
écrire le programme Python qui récupère ces données de la table et trace un diagramme en camembert


Exercice 46:
------------
Ecrire un programme demandant à l'utilisateur de saisir
- une liste d'abscisses
- une liste d'ordonnées
- une liste de 0 et de 1
Par exemple:
- x = [1, 2, 3, 4, 5]  # on a 5 x
- y = [2, 4, 6, 8, 10] # on a 5 y
- c = [0, 1, 0, 1, 0]  # on a 5 c

- Le programme devra prendre ces valeurs et les stocker dans une table
- Le programme devra ensuite tracer un nuage de points en utilisant les valeurs de x et de y
- Attention:
  - la colonne c represente une couleur de point
  - 0 --> bleu
  - 1 --> rouge
  - ex: le premier point, de coordonnées (1, 2) doit avoir la couleur bleue


Exercice 47:
-------------

- Créez 1 array unidimensionnel d'entiers de 0 à 9.
- Créez 1 array bidimensionnel de forme (3, 4) contenant des zéros.
- Créez 1 array bidimensionnel de forme (4, 5) contenant des uns.
- Créez 1 array bidimensionnel de forme (4, 4) contenant des entiers aléatoires entre 0 et 9.
- Créez 1 array bidimensionnel de forme (3, 3) contenant la matrice identité.

Exercice 48:
------------
- Créez 1 array unidimensionnel contenant les nombres de 1 à 5,
  - reformez-le en un tableau bidimensionnel de forme (5, 1).

- Créez 1 array bidimensionnel de forme (3, 3) contenant les nombres de 0 à 8.
  - tranchez-le pour extraire le sous-tableau contenant les 2e, 3e lignes puis les 2 premières colonnes.

- Créez un tableau unidimensionnel de forme contenant les nombres de 1 à 6.
  - utilisez les fonctions NumPy pour calculer la moyenne, la médiane et l'écart type du tableau.

- Créez deux tableaux bidimensionnels de forme (3, 3) contenant des entiers aléatoires entre 0 et 9.
  - utilisez les fonctions NumPy pour calculer
    - la somme  (élément par élément des deux tableaux)
    - la différence  (élément par élément des deux tableaux)
    - le produit  (élément par élément des deux tableaux)
    - le quotient  (élément par élément des deux tableaux)

- Créez un tableau unidimensionnel de forme contenant des entiers aléatoires entre 0 et 9.
  - utilisez les fonctions NumPy pour calculer
    - l'index de la valeur maximale,
    - l'index de la valeur minimale
    - le tableau trié.

Exercice 49:
------------
- Qui est Fibonacci ? Pour quel travail est-il connu ?


Exercice 50:
------------

- écrire une fonction récursive qui renverse une chaine de caractère
- écrire une fonction récursive qui vérifie si une chaine de caractère est un palindrome
- écrire une fonction récursive qui calcule la puissance d'un nombre


Exercice 51:
------------
- écrire la fonction de Fibonacci sous sa forme récursive et sous sa forme iterative,
  - mesurer et comparer les temps d'execution

- écrire la fonction de Tribonacci sous sa forme récursive et sous sa forme iterative,
  - mesurer et comparer les temps d'execution

- Write a recursive function to compute the greatest common divisor (GCD) of two non-negative integers.

Exercice 52:
------------
- écrire une fonction récursive qui calcule le nombre de chiffre d'un nombre positif.

Exercice 53:
------------
- écrire une fonction récursive qui calcule le produit de deux nombres positifs en utilisant seulement l'addition et la récursion (ne pas utiliser de multiplication).

- écrire une fonction récursive qui calcule la divisition de deux nombres positifs en utilisant seulement la soustraction et la récursion (ne pas utiliser de division).


Exercice 54:
------------
- Écrivez une classe pour représenter un nombre complexe avec des méthodes pour:
  - ajouter, soustraire et multiplier des nombres complexes.

- Écrivez une classe pour représenter un polygone avec des méthodes pour
  - calculer son aire et son périmètre.

- Écrivez une classe pour représenter une date avec des attributs tels que
  - le jour, le mois et l'année.
  - vous determinerez et ajouterez les méthodes magiques pour
    - additionner, soustraire, multiplier, diviser des objets de type Date

- Écrivez une classe pour représenter une heure avec des attributs tels que
  - l'heure, la minute et la seconde.
  - vous determinerez et ajouterez les méthodes magiques pour
    - additionner, soustraire, multiplier, diviser des objets de type Date

- Écrivez une classe pour représenter un chronomètre avec des méthodes pour:
  - démarrer, arrêter et réinitialiser le timer.

- Écrivez une classe pour représenter un fichier avec des méthodes pour:
  -  lire, écrire et ajouter des données.


Exercice 53:
------------
- Qu'est ce qu'un diagramme en barre empilé ? Quand est ce qu'on s'en sert ?
- proposez des exemples d'illustration


Exercice 54:
------------
Prendre le contenu de la table Invoices se trouvant dans la base de données Chinook. Charger ce contenu dans un dataframe Pandas et afficher les 5 premières lignes. Indice: read_sql

Exercice 55:
------------
Filtrer les lignes du dataframe pour n'inclure que les lignes où une certaine colonne répond à une certaine condition:
- le billing city est égal à "Paris"
- le customer id est égal à 37
- le billing city est égal à "Paris" et le customer id est égal à 39

Exercice 56:
------------
Regrouper les lignes du dataframe par la colonne: CustomerId et calculer:
- la somme totale dépensée par chaque client
- le nombre total de facture par client
- la moyenne des achats par client

Exercice 57:
------------
Fusionner deux colonnes du dataframe: BillingCity et BillingAddress, stockez la fusion dans la colonne BillingAdress.

Exercice 58:
------------
Utiliser la fonction .describe() pour résumer les données dans le dataframe. Interpreter chaque ligne du résultat.

Exercice 57:
------------
Le type de la colonne InvoiceDate est "object". Changer le type de cette colonne en datetime.

Exercice 58:
------------
Récupérer tous les enregistrements du DataFrame compris entre le 15 janvier 2012 et le 30 janvier 2012.

Exercice 59:
------------
Trier les lignes du dataframe en fonction d'une certaine colonne. Par exemple, la colonne "Total".

Exercice 60:
------------
Renommer toutes les colonnes du dataframe en utilisant des noms en français.

Exercice 61:
------------
Supprimez la colonne BillingState et la colonne BillingCity.

Exercice 62:
------------
Remplir les valeurs manquantes dans le dataframe avec une certaine valeur.

Exercice 63:
------------
Extraire la valeur de la colonne "Total" pour les clients 19 et 25.

Exercice 64:
------------
Extraire la valeur de la colonne "Total" pour les clients 19 et 25. On désire offrir une réduction à ces 2 clients, mettre à jour le total en divisant la valeur existante par 2.

Exercice 65:
------------
Expliquer en détail ce que fait le programme suivant:

import matplotlib.pyplot as plt
df2 = df.groupby("CustomerId" , as_index = False)["Total"].sum()
df2.plot.scatter(x="CustomerId", y="Total", c="red")
plt.show()

Exercice 66:
------------
Tracer un nuage de point montrant le nombre total de factures par ville.



Exercices pour aller encore plus loin:
--------------------------------------
- https://www.kaggle.com/learn/python
- https://colab.research.google.com/github/ryanorsinger/101-exercises/blob/main/101-exercises.ipynb
- https://edabit.com/challenges
- https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt

