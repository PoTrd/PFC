# Jeu du Pierre Feuille Ciseaux

import random

liste = ["pierre", "feuille", "ciseaux"]

print("Bienvenue! prêt à jouer ?")


def game():

    bot = random.choice(liste)
    player = str(input("Fais ton choix (pierre, feuille, ciseaux) : "))

    def win_msg():
        print(player, "VS", bot, ">>> Bravo vous avez gagné !")

    def lose_msg():
        print(player, "VS", bot, ">>> Mince le robot à gagné..")

    if player == bot:
        print("Egalité, le robot a également choisi :", bot)
    elif player == "pierre" and bot == "ciseaux":
        win_msg()
    elif player == "feuille" and bot == "pierre":
        win_msg()
    elif player == "ciseaux" and bot == "feuille":
        win_msg()
    elif player == "pierre" and bot == "feuille":
        lose_msg()
    elif player == "feuille" and bot == "ciseaux":
        lose_msg()
    elif player == "ciseaux" and bot == "pierre":
        lose_msg()
    else:
        print(">>> ERROR")

    play_again()


def play_again():
    play = input("Voulez vous rejouer ? (Y/N)")
    if play == "y" or play == "Y" or play == "YES" or play == "yes" or play == "Yes":
        game()
    else:
        exit


game()
