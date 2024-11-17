import filler_animation
import data
from clear import *
import time

# INPUT
def demander_info_entier(question: str, default):
    choix = default
    try:
        choix = int(input(question))
        clear.clear(0)
    except ValueError:
        clear.clear(0)
    return choix

# DISPLAY

# utility

def display_text(text: str, padding: int):
    text_display = "|" + " "*padding + text
    text_display = text_display + " " * (40 - int(len(text_display))) + "|"
    special_print(text_display)

def display_center_text(text: str):
    text_display: str = "|" + " " * (19 - int(len(text) / 2)) + text
    text_display = text_display + " " * (40 - int(len(text_display))) + "|"
    special_print(text_display)

def display_paragraph(text: str, padding: int = 4, center: bool = False, jump_line: bool = False):
    # affichage du texte en sautant de ligne si nécessaire
    all_text_line: list = []
    text_line: str = ""
    mot: str = ""
    for c in text:
        if c == " " or c == "\n":
            if text_line == "": text_line += mot 
            else: text_line += " " + mot
            mot = ""
            if c == "\n":
                all_text_line.append(text_line)
                text_line = ""
        else:
            mot += c
            if len(mot) >= 39 - (2 * padding):
                if text_line != "":
                    all_text_line.append(text_line)
                all_text_line.append(mot)
                mot = ""
                text_line = ""
        if (len(text_line) + len(mot)) >= 39 - (2 * padding):
            all_text_line.append(text_line)
            text_line = ""

    if mot != "":
        if text_line == "": text_line += mot 
        else: text_line += " " + mot
    if text_line != "":
        all_text_line.append(text_line)

    for ligne in all_text_line:
        if center:
            display_center_text(ligne)
        else:
            display_text(ligne,padding)
        if jump_line:
            display_line_jump()

def display_line_jump():
    special_print("|                                       |")

# prefab

def display_game_presentation(name:str, description:str, regle:str, icon: str):
    # affichage debut du menu pour presenter le jeux
    special_print(f"\n{icon} -------------- Game ---------------{icon}")
    special_print("| Bienvenue sur le jeux:                |")

    # centre le nom
    display_center_text(name)
    # ajoute espace
    display_center_text("---- desc ----")
    # affichage de la description
    display_paragraph(description,padding=1,center=False)
    # ajoute espace
    display_center_text("---- regle ----")
    # affichage des regle
    display_paragraph(regle,center=True)
    special_print(f"{icon} -----------------------------------{icon}\n")

def display_box(
    titre: str = "",
    texte: str = "",
    icon: str = "🔘",
    center_texte: bool = False,
    padding=4,
):
    special_print(f"\n{icon} -------------- Game ---------------{icon}")

    if titre != "":
        display_center_text(titre)
    if texte != "":
        display_paragraph(texte, padding, center_texte)
    else:
        display_line_jump()

    special_print(f"{icon} -----------------------------------{icon}\n")

def display_victory(player: str, point: int):
    display_box(
        titre="Victoire", texte=f"bravo {player} vous gagnez {point} point", icon="🟢",padding=2,center_texte=True
    )


def display_game_ranking(id: int, n: int):
    game_name: str = data.get_game_name(id)
    ranking: list = data.get_top_score(game_name,n)
    
    special_print("🟡 -------------- Score --------------🟡")

    display_line_jump()
    display_center_text(f"---- {game_name} ----")
    display_line_jump()

    paragraph = ""
    for i in range(n):
        paragraph += f"{i+1}. {data.get_player_name(ranking[i][0])} avec {ranking[i][1]}\n"
    paragraph += f"<-Q {id+1}/4 D->"

    display_paragraph(paragraph,center=True,jump_line=True)

    special_print("🟡 -----------------------------------🟡\n")


#LAUNCH
def launch_game(game_name: str, function):
    # recupere les data du jeux lancer
    game_data = data.find_data_line(game_name,1,data.get_game_data())

    # affiche une presentation du jeux lancer
    display_game_presentation(
        game_data[1],
        game_data[3],
        game_data[4],
        game_data[2],
    )
    
    # afiche un filler pendant 5s qui aura 36 case qui vont se remplir au fur a mesure des 5s avec sur le coté l'icon du jeux
    filler_animation.launch_load_anim(10, 36, game_data[1], "▪️", "▫️")
    # efface l'ecran aprés la fin du filler de 5s avec la taille de la presentation et celle du filler
    clear(1)
    clear_terminal()
    # lance la fonction de {jeux}
    """display_box(
        texte=f"Choisissez quelle joueur commence:\n1. {player1} \n2. {player2}",
        center_texte=True,
        padding=2,
    )
    player_begin = 0
    while player_begin != 1 and player_begin != 2:
        player_begin = demander_info_entier("Votre choix : ", 0)
    clear.clear(7)
    function(player_begin)"""

def who_played():
    player_1_name: str = "..."
    player_2_name: str = "..."
    pseudo: str = ""
    while player_1_name == "..." and player_2_name == "...":
        display_box("quelle sont vos pseudo",f"1. {player_1_name} 2. {player_2_name}",center_texte=True)

        while choice != 1 and choice != 2:
            choice = demander_info_entier("Votre choix : ", 1)

            pseudo = input("quelle est votre pseudo")



who_played()