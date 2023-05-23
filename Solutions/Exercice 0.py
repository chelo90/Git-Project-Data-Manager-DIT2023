#Executez chacune des boucles suivantes

# L'exécution de cette boucle permet d'afficher les valeurs comprise entre 10 et 15 sauf la valeur 15
for i in range(10, 15):
    print(i)

# L'exécution de cette boucle permet d'afficher les valeurs comprise entre 20 et 40 par pas de 2 sauf la valeur 40
for i in range(20,40,2):
    print(i)

# L'exécution de cette boucle permet d'afficher les valeurs comprises entre 0 et 20 dont le reste de la division par 2 est égale à 0
for i in range(20):
    if i%2 == 0:
       print(i)

# L'exécution de cette boucle permet d'afficher les valeurs comprises entre 0 et 20 dont le reste de la division par 2 est différent de 0. 
# Ce sont les nombres impairs compris entre 0 et 20
for i in range(20):
    if i%2 != 0:
       print(i)

# La fonction Range renvoie un objet qui produit une séquence d'entiers depuis le début (étape 0 inclusif) pour s'arrêter en fonction de la dernière position et du pas qui a été défini. 
# Ex : range(i, j) produit i, i+1, i+2, ..., j-1. La position initiale est 0 par défaut et la dernière position est omise.
# Ex : range(4) produit 0, 1, 2, 3. Ce sont exactement les indices valides pour une liste de 4 éléments. 
# Lorsque le pas est donné, elle spécifie l'incrément (ou le décrément).

# L'exécution de cette boucle permet d'afficher les nombres de 0 à 1000 de 2 en 2
for i in range(0,1000,2):
    print(i)

# L'exécution de cette boucle permet d'afficher les nombres de 0 à 1000 de 10 en 10
for i in range(0,1000,10):
    print(i)

# L'exécution de cette boucle permet d'afficher les nombres de 0 à 1000 de 100 en 100
for i in range(0,1000,100):
    print(i)

# L'exécution de cette boucle permet d'afficher les nombres de -15 à 15
for i in range(-15, 16):
    print(i)

# L'exécution de cette boucle permet d'afficher les nombres de -15 à 15
for i in range(-15, 15):
    print(i)

# L'exécution de cette boucle permet d'afficher les nombres de -30 à 30 de 5 en 5
for i in range(-30, 30, 5):
    print(i)

# L'exécution de cette boucle permet d'afficher les nombres de 50 à 100 de 3 en 3
for i in range(50, 100, 3):
    print(i)

