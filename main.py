from os import close, read, times, write
from auth import *
from encrypt import *
from datetime import *

# Permet de détecter si il y a eu une intrusion
intrusionValide = open("intrusion.txt", "r")
if intrusionValide.read() == "Intrusion" :
    print("une intrusion a été détécté")
    supp = open("intrusion.txt", "w")
    supp.write("Pas d'intrusion pour le moment")
    supp.close()


user = None
tries = 0
mx_tries = 5

while tries < mx_tries:
    pseudo = input("Quel est ton pseudo ? ")
    mdp = input("Quel est ton mot de passe ? ")

# Vérifie si le pseudo et le mot de passe correspondent bien 
    if auth(pseudo, mdp):
        user = User(pseudo, mdp)
        print("===========================================================")
        print("")
        print("Vous êtes bien identifié !")
        print("")
        break

    tries += 1

# Permet décrire dans le fichier intrusion si l'utilisateur rate 5 fois
if user is None:
    intrusion = open("intrusion.txt", "w")
    intrusion.writelines("Intrusion")
    intrusion.close()
    exit()

while True:
    print("===========================================================")
    method = input("Quelle méthode veux-tu utiliser (encrypt/decrypt)? ")
    assert method == "encrypt" or method == "decrypt"

    nom_fichier = input(f"({method}) Quel est le nom de ton fichier text ? ")
    result = encrypt(nom_fichier) if method == "encrypt" else decrypt(nom_fichier)
    print(result)
