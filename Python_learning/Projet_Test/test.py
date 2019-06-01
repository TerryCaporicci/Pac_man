# -*-coding:Utf-8 -*
import os
majority = 18
age = input("quel age avez vous ? ")
age = int(age)
if age > majority:
    print("tu as plus de 18 ans, formidable tu peux venir !")
elif age == majority :
    print("tout juste 18 ans a ce que je vois. c'est juste mais bienvenu a toi !")
else :
    print("desoler tu n'a pas 18 ans, revient dans quelque année !")
os.system("pause")