import random
import toolbox
from clear import clear
import time


def afficher_allumettes(allumettes):
    toolbox.afffichage_box(
        texte=f"Nombre d'allumettes restantes : {allumettes}\n"
        + "Allumettes : "
        + "|" * allumettes,
        padding=1,
        center_texte=True,
    )


def jeu_allumettes_2_joueurs():
    game: bool = True

    while game:
        allumettes = 21
        print("Bienvenue au jeu des allumettes pour 2 joueurs !")
        print("Il y a 21 allumettes au départ.")
        print("Vous pouvez retirer entre 1 et 3 allumettes à chaque tour.")
        print("Le joueur qui prend la dernière allumette perd la partie.\n")

        toolbox.afffichage_box(
            texte="Qui commence ? \n'1': Joueur 1\n'2': Joueur 2\n'A': aléatoire",
            center_texte=True,
        )

        choix = input("").strip()
        joueur_actuel = int(choix) if choix in [1, 2] else random.choice([1, 2])
        print(f"C'est le Joueur {joueur_actuel} qui commence.\n")

        while allumettes > 0:
            afficher_allumettes(allumettes)

            choix_allumettes = toolbox.demander_info_entier(
                f"Joueur {joueur_actuel}, combien d'allumettes souhaitez-vous retirer ? (1, 2 ou 3) : ",
                1,
            )

            if 1 <= choix_allumettes <= 3 and choix_allumettes <= allumettes:
                allumettes -= choix_allumettes
            else:
                print("Choix invalide, essayez à nouveau.")
                continue

            if allumettes == 0:
                print(
                    f"Le joueur {joueur_actuel} a pris la dernière allumette. Le joueur {joueur_actuel} a perdu !"
                )
                break

            joueur_actuel = 2 if joueur_actuel == 1 else 1

    choix = toolbox.demander_info_entier(
        "\nvoulez vous rejouer taper 0. Non 1. Oui \n", 0
    )
    clear(0)
    time.sleep(1)

    if choix == 1:
        game = True
    else:
        game = False
