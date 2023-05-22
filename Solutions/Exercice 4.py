"""
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
"""


t = float(input("Entrez votre taille en m : "))
m = float(input("Entrez votre masse en kg : "))

bmi = m / (t ** 2)


if bmi < 16.5:
    category = "dénutrition"
elif 16.5 <= bmi < 18.5:
    category = "maigreur"
elif 18.5 <= bmi < 25:
    category = "masse normale"
elif 25 <= bmi < 30:
    category = "surpoids"
else:
    category = "obésité"


print("Votre indice de masse corporelle (IMC) est :", bmi)
print("Catégorie : ", category)
