# Demander à l'utilisateur de saisir un nombre N
N = int(input("Saisir un nombre N : "))
 
# définir et initialiser la somme
somme = 0
for i in range(1,N+1):
    somme = somme + i 
print("La somme de 1 + 2 + 3 + ... +",N," = ", somme)
