# -*-coding:Utf-8 -*
import os
print("quel table de multiplication voulez vous ? ")
nb = int(input())
while nb == 0:
    print("le nombre ne peux etre 0, veuillez rentrer un nombre plus grand")
    nb = int(input())
nbDepart = 0 
print("table de multiplication de ",nb)
print("-----------------------------")
while 10 > nbDepart:
    print(nbDepart + 1, " * ", nb , " = ", (nbDepart+1) * nb)
    nbDepart += 1

os.system("pause")
