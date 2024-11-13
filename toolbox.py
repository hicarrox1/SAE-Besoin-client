import filler_animation
import clear
import math
import data


def launch_game(name: str, function):
    # recupere les data du jeux lancer
    game_data = data.get_select_game(name)

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
    filler_animation.launch_load_anim(2, 36, game_data[1], "▪️", "▫️")

    # efface l'ecran aprés la fin du filler de 5s avec la taille de la presentation et celle du filler
    clear.clear(taille + 2)
    player1 = data.get_name(1)
    player2 = data.get_name(2)
    # lance la fonction de {jeux}
    afffichage_box(texte=f"Choisissez quelle joueur commence:\n1. {player1} \n2. {player2}",center_texte=True, padding= 2)
    player_begin = 0
    while player_begin!= 1 and player_begin != 2:
        player_begin = demander_info_entier("Votre choix : ",0)
    clear.clear(7)
    function(player_begin)


def present_game(name, description, regle, icon):
    # affichage debut du menu pour presenter le jeux
    print(f"\n{icon} -------------- Game ---------------{icon}")
    print("| Bienvenue sur le jeux:                |")

    # centre le nom
    affichage_text_centre_box(name)
    # ajoute espace
    affichage_text_centre_box("---- desc ----")
    # affichage de la description
    affichage_text_centre_box(description)
    # ajoute espace
    affichage_text_centre_box("---- regle ----")
    # affichage des regle
    affichage_paragraphe_box(regle)
    print(f"{icon} -----------------------------------{icon}\n")

def affichage_paragraphe_box(texte: str):
    # affichage du texte en sautant de ligne si nécessaire
    affichage_texte = ""
    ligne_texte = "|"
    for c in texte:
        if c == "\n":
            affichage_texte += ligne_texte + " " * (40-len(ligne_texte)) + "|\n"
            ligne_texte = "|"
        else:
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


def affichage_paragraphe_centre_box(texte: str, padding: int = 4):

    # affichage du texte en sautant de ligne si nécessaire
    liste_ligne = []
    ligne_texte = ""
    for c in texte:
        if c == "\n":
            liste_ligne.append(ligne_texte)
            ligne_texte = ""
        else:
            ligne_texte += c
        if len(ligne_texte) >= 40-(2*padding):
            liste_ligne.append(ligne_texte)
            ligne_texte = ""
    if ligne_texte != "":
        liste_ligne.append(ligne_texte)

    for ligne in liste_ligne:
        affichage_text_centre_box(ligne)

def affichage_jump_lines():
    print("|                                       |")


def afffichage_box(titre: str = "", texte: str = "", icon: str = "🔘", center_texte: bool = False, padding = 4):
    print(f"\n{icon} -------------- Game ---------------{icon}")

    if titre != "":
        affichage_text_centre_box(titre)
    if texte != "":
        if center_texte:
            affichage_paragraphe_centre_box(texte, padding)
        else:
            affichage_paragraphe_box(texte)
    else:
        affichage_jump_lines()

    print(f"{icon} -----------------------------------{icon}\n")


def affiche_victoire(joueur:str, point: int):
    afffichage_box(titre="Victoire", texte=f" bravo {joueur} vous gagnez {point} point", icon="🟢")


def afficher_score(jeux: str):
    score = data.get_score(jeux)
    player_1_score = score[0]
    player_2_score = score[1]
    print(f"perso 1: {player_1_score}   perso 2: {player_2_score}")

def afficher_all_score():
    score_data = data.get_score_data()
    jeux = ""

    print(f"🟡 -------------- Score --------------🟡")

    for data_lines in score_data:
       
       if data_lines[1] != jeux:
           affichage_text_centre_box(f"---- {data_lines[1]} ----")
           jeux = data_lines[1]

       affichage_paragraphe_centre_box(f"{data.get_name(int(data_lines[0]))} : {data_lines[2]} \n",2)

    print(f"🟡 -----------------------------------🟡\n")


def demander_info_entier(question: str, default):
    choix = default
    try:
        choix =  int(input(question))
        clear.clear(0)
    except:
        clear.clear(0)
    return choix