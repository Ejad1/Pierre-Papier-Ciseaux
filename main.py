# -*-coding:Utf-8 -*
import os
import random

print("Bienvenu sur le jeu de pierre papier ciseaux de EJAD")

print("Voici les choix possibles : \n1- Pierre\n2- Papier\n3- Ciseaux")


def demande():
    choix = input("Veuillez entrer votre choix (entrez juste le numéro du choix que vous voulez-faire): ")

    if not choix.isdigit():
        print("Vous n'avez pas entrez un nombre")
        return demande()
    else:
        choix = int(choix)
        if not (choix in [1, 2, 3]):
            print("Entrer un nombre égal à 1, 2 ou 3")
            return demande()
        else:
            return choix


joueur = demande()
joueur = int(joueur)

# Liste contenant les possibilités de l'ordinateur
possible = ["pierre", "papier", "ciseaux"]
ordinateur = random.randrange(len(possible))

print("L'ordinateur a choisi...", possible[ordinateur])


def verification():
    if joueur == 1:
        if possible[ordinateur] == "pierre":
            print("Il y'a égalité")
        elif possible[ordinateur] == "papier":
            print("Vous avez perdu dommage")
        elif possible[ordinateur] == "ciseaux":
            print("Vous avez gagner félicitations!!!")

    if joueur == 2:
        if possible[ordinateur] == "pierre":
            print("Vous avez gagner")
        elif possible[ordinateur] == "papier":
            print("Il y'a égalité")
        elif possible[ordinateur] == "ciseaux":
            print("Vous avez perdu")

    if joueur == 3:
        if possible[ordinateur] == "pierre":
            print("Vous avez perdu")
        elif possible[ordinateur] == "papier":
            print("Vous avez gagner")
        elif possible[ordinateur] == "ciseaux":
            print("Il y'a égalité")


verification()

os.system("pause")
