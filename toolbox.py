import filler_animation
import data
from clear import (
    clear,
    clear_terminal,
    special_print,
    special_input,
    clear_one_line,
)
import unicodedata


# INPUT
def ask_int(question: str, default):
    choix = default
    try:
        choix = int(special_input(question))
        clear_one_line()
    except ValueError:
        clear_one_line()
    return choix


def ask_str(question: str, default):
    choix = default
    try:
        choix = special_input(question)
        clear_one_line()
    except ValueError:
        clear_one_line()
    return choix


# DISPLAY

# utility


def char_width(char):
    if unicodedata.east_asian_width(char) in ["W", "F"]:
        return 2
    else:
        return 1


def string_width(s):
    return sum(char_width(char) for char in s)


def display_text(text: str, padding: int):
    text_display = "|" + " " * padding + text
    text_display = text_display + " " * (40 - int(string_width(text_display))) + "|"
    special_print(text_display)


def display_center_text(text: str):
    text_display: str = "|" + " " * (19 - int(string_width(text) / 2)) + text
    text_display = text_display + " " * (40 - int(string_width(text_display))) + "|"
    special_print(text_display)


def display_line_jump():
    special_print("|                                       |")


def display_paragraph(
    text: str, padding: int = 4, center: bool = False, jump_line: bool = False
):
    # affichage du texte en sautant de ligne si nécessaire
    all_text_line: list = []
    text_line: str = ""
    mot: str = ""
    for c in text:
        if c == " " or c == "\n":
            if text_line == "" and len(mot)>1:
                text_line += mot
            else:
                text_line += " " + mot
            mot = ""
            if c == "\n":
                all_text_line.append(text_line)
                text_line = ""
        else:
            mot += c
            if string_width(mot) >= 39 - (2 * padding):
                if text_line != "":
                    all_text_line.append(text_line)
                all_text_line.append(mot)
                mot = ""
                text_line = ""
        if (string_width(text_line) + string_width(mot)) >= 39 - (2 * padding):
            all_text_line.append(text_line)
            text_line = ""

    if mot != "":
        if text_line == "":
            text_line += mot
        else:
            text_line += " " + mot
    if text_line != "":
        all_text_line.append(text_line)

    for ligne in all_text_line:
        if center:
            display_center_text(ligne)
        else:
            display_text(ligne, padding)
        if jump_line:
            display_line_jump()


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


# prefab


def display_game_presentation(name: str, description: str, regle: str, icon: str):
    # affichage debut du menu pour presenter le jeux
    special_print(f"\n{icon} -------------- Game ---------------{icon}")
    special_print("| Bienvenue sur le jeux:                |")

    # centre le nom
    display_center_text(name)
    # ajoute espace
    display_center_text("---- desc ----")
    # affichage de la description
    display_paragraph(description, padding=1, center=False)
    # ajoute espace
    display_center_text("---- regle ----")
    # affichage des regle
    display_paragraph(regle, center=True)
    special_print(f"{icon} -----------------------------------{icon}\n")


def display_victory(player: str, point: int):
    display_box(
        titre="Victoire",
        texte=f"bravo {player} vous gagnez {point} point",
        icon="🟢",
        padding=2,
        center_texte=True,
    )


def display_best_player(game_name: str):
    best_player: list = data.get_top_score(game_name, 1)
    player_name: str = data.get_player_name(best_player[0][0])
    display_box(
        titre=f" meilleur joueur de {game_name}",
        texte=f" {data.get_player_icon(player_name)} {player_name} avec {best_player[0][1]} point",
        icon="🟡",
        padding=2,
        center_texte=True,
    )


def display_game_ranking(id: int, n: int):
    game_name: str = data.get_game_name(id)
    ranking: list = data.get_top_score(game_name, n)
    player_name: str = ""

    special_print("🟡 -------------- Score --------------🟡")

    display_line_jump()
    display_center_text(f"---- {game_name} ----")
    display_line_jump()

    paragraph = ""
    for i in range(n):
        player_name = data.get_player_name(ranking[i][0])
        paragraph += f"{i+1}. {data.get_player_icon(player_name)} {player_name} avec {ranking[i][1]} point\n"
    paragraph += f"<-Q {id+1}/4 D->"

    display_paragraph(paragraph, center=True, jump_line=True)

    special_print("🟡 -----------------------------------🟡\n")


# GAME TOOLS
def launch_game(game_name: str, function):
    players: list = []

    # recupere les data du jeux lancer
    game_data: list = data.get_game_line(game_name)

    # affiche une presentation du jeux lancer
    display_game_presentation(
        game_data[1],
        game_data[3],
        game_data[4],
        game_data[2],
    )

    # afiche un filler pendant 5s qui aura 36 case qui vont se remplir au fur a mesure des 5s avec sur le coté l'icon du jeux
    filler_animation.slider(10, 36, game_data[2], "▪️", "▫️")
    # efface l'ecran aprés la fin du filler de 5s avec la taille de la presentation et celle du filler
    clear(1)
    clear_terminal()
    # lance la fonction de {jeux}
    players = who_played()
    function(players)


def who_played() -> list:
    player_1_name: str = "..."
    player_2_name: str = "..."
    pseudo: str = ""
    choice: int = 0
    start: bool = False

    while player_1_name == "..." or player_2_name == "..." or not start:
        choice = 0
        pseudo = ""
        display_box(
            "quelle sont vos pseudo",
            f"1. {player_1_name} 2. {player_2_name}\n3. Start",
            center_texte=True,
        )

        while choice != 1 and choice != 2 and choice != 3:
            choice = ask_int("Votre choix : ", 0)

        if choice == 3 and player_1_name != "..." and player_2_name != "...":
            start = True
        elif choice == 1 or choice == 2:
            while pseudo == "":
                pseudo = ask_str("quelle est votre pseudo: ", "")
                if len(pseudo) >= 8:
                    pseudo = ""
            if choice == 1:
                player_1_name = pseudo
            else:
                player_2_name = pseudo
        clear_terminal()

    if data.get_player_id(player_1_name) == -1:
        data.add_player(player_1_name, "🧟")

    if data.get_player_id(player_2_name) == -1:
        data.add_player(player_2_name, "🧟")

    return [player_1_name, player_2_name]


def choose_icon() -> str:
    icon: str = ".."
    choice: int = 0
    change: bool = False
    icons: list = ["🌞", "🐵", "🦖", "🌷", "🍔", "🌵", "🐘"]

    while icon == ".." or not change:
        choice = 0
        display_box(
            "choisissez votre icon",
            f"icon: {icon} \n1.🌞 2.🐵 3.🦖 4.🌷 5.🍔 6.🌵 7.🐘\n 8. Change",
            center_texte=True,
            padding=2,
            icon="👤",
        )

        while choice not in [1, 2, 3, 4, 5, 6, 7, 8]:
            choice = ask_int("Votre choix : ", 0)

        if choice == 8 and icon != "..":
            change = True
        else:
            icon = icons[choice - 1]

        clear_terminal()

    return icon


def change_icon():
    icon: str = ".."
    pseudo: str = "..."
    choice: int = 0
    change: bool = False

    while icon == ".." or pseudo == ".." or not change:
        choice = 0
        display_box(
            "",
            f"1. pseudo: {pseudo} 2. icon: {icon}\n3. Change",
            center_texte=True,
            padding=2,
            icon="🦲",
        )

        while choice != 1 and choice != 2 and choice != 3:
            choice = ask_int("Votre choix : ", 0)

        if choice == 3 and icon != ".." and pseudo != "...":
            change = True
        elif choice == 1:
            while pseudo == "...":
                pseudo = ask_str("quelle est votre pseudo: ", "...")
                if len(pseudo) >= 8 or data.get_player_id(pseudo) == -1:
                    pseudo = "..."
        elif choice == 2:
            clear_terminal()
            icon = choose_icon()

        clear_terminal()

    data.set_player_icon(pseudo, icon)


def game_ranking():
    game_id: int = 0
    choice = ""
    display: bool = True

    while display:
        choice = ""
        display_game_ranking(game_id, 5)
        special_print("A pour quitter")

        while choice != "D" and choice != "Q" and choice != "A":
            choice = ask_str("-> ", "")

        if choice == "D":
            game_id = (game_id + 1) % 4
        elif choice == "Q":
            game_id = (game_id - 1) % 4
        elif choice == "A":
            display = False

        clear_terminal()
