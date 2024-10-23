import filler_animation
import clear
import math
from data import get_select_game


def launch_game(name: str, function):
    # recupere les data du jeux lancer
    game_data = get_select_game(name)

    # affiche une presentation du jeux lancer
    present_game(
        game_data[0],
        game_data[2],
        game_data[3],
        game_data[1],
    )
    # calcul de la taille de la presentation
    taille = 6 + math.ceil(len(game_data[2]) / 39) + math.ceil(len(game_data[3]) / 39)
    # afiche un filler pendant 5s qui aura 36 case qui vont se remplir au fur a mesure des 5s avec sur le coté l'icon du jeux
    filler_animation.launch_load_anim(5, 36, game_data[1], "▪️", "▫️")

    # efface l'ecran aprés la fin du filler de 5s avec la taille de la presentation et celle du filler
    clear.clear(taille + 2)
    # lance la fonction de jeux
    function()


def present_game(name, description, regle, icon):
    # affichage debut du menu pour presenter le jeux
    print(f"\n{icon} -------------- Game ---------------{icon}")
    print("| Bienvenue sur le jeux:                |")

    # centre le nom
    affichage_text_centre_box(name)
    # ajoute espace
    affichage_text_centre_box("---- desc ----")
    # affichage de la description
    affichage_text_box(description)
    # ajoute espace
    affichage_text_centre_box("---- regle ----")
    # affichage des regle
    affichage_text_box(regle)
    print(f"{icon} -----------------------------------{icon}\n")


def affichage_text_box(texte: str):
    # affichage du texte en sautant de ligne si nécessaire
    affichage_texte = ""
    ligne_texte = "|"
    for c in texte:
        ligne_texte += c
        if len(ligne_texte) >= 40:
            affichage_texte += ligne_texte + "|\n"
            ligne_texte = "|"
    affichage_texte += ligne_texte + " " * (40 - len(ligne_texte)) + "|"
    print(affichage_texte)


def affichage_text_centre_box(texte: str):
    affichage_texte = "|" + " " * (19 - int(len(texte) / 2)) + texte
    affichage_texte = affichage_texte + " " * (40 - int(len(affichage_texte))) + "|"
    print(affichage_texte)


def affichage_jump_lines():
    print("|                                       |")


def afffichage_box(titre: str = "", texte: str = "", icon: str = "🔘"):
    print(f"\n{icon} -------------- Game ---------------{icon}")

    if titre != "":
        affichage_text_centre_box(titre)
    if texte != "":
        affichage_text_box(texte)
    else:
        affichage_jump_lines()

    print(f"{icon} -----------------------------------{icon}\n")


def affiche_victoire(point: int):
    afffichage_box(titre="Victoire", texte=f" Vous gagnez {point} point", icon="🟢")
