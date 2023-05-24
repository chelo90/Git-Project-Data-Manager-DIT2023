import turtle

# Demander à l'utilisateur de saisir un nombre N
L = float(input("longeur ? : "))
l = float(input("largeur ? : "))
 
# définition de la surface du rectangle
S = L*l 
print("la surface est", S)

# définition du périmètre du rectangle
P = (L+l)*2 
print("le perimetre est", P)

Q = bool(input("Voulez-vous tracer un rectangle ? :      "))
if True :
  #Programme pour dessiner un rectangle avec le module turtle
  #Pour que le rectangle s'affiche un peu plus longtemps, utilisez des dimensions de L et l supérieures ou égale à 150
  tur = turtle.Turtle()
  tur.forward(L) # Déplace la tortue de L unités vers l'avant
  tur.left(90) # rotation de la tortue de 90 degrés
  tur.forward(l) # Déplace la tortue de l unités vers l'avant
  tur.left(90) # rotation de la tortue de 90 degrés
  tur.forward(L) # Déplace la tortue de L unités vers l'avant
  tur.left (90) # rotation de la tortue de 90 degrés
  tur.forward(l) # Déplace la tortue de l unités vers l'avant
  tur.left(90) # rotation de la tortue de 90 degrés
  #print(tur)
  print("aurevoir") 
else :
  print("aurevoir")
