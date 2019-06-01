# -*-coding:Utf-8 -*
import os
i = 10
toi = 0
chaine_useless = "je fais 21 caracteres"
compt = 0


while i >= toi:
    print("i avais une puissance de ", i, "alors que tu as une puissance de ", toi, ", la defaite etait le seul chemin !")
    toi += 1
print("bravo ! avec ta puissance de ", toi, "tu a enfin reussi a battre i, force et honneur a toi !")

for letter in chaine_useless:
    print(letter)
    compt += 1
print(compt) 
os.system("pause")