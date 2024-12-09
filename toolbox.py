import filler_animation
import data
import time
from clear import (
    clear,
    clear_terminal,
    special_print,
)
from display_tool import (
    display_center_text,
    display_box,
    display_paragraph,
    display_line_jump,
)
from input_tool import ask_int, ask_str


# prefab
def display_game_presentation(name: str, description: str, regle: str, icon: str):
    """
    Affiche une présentation du jeu, comprenant le nom, la description et les règles.

    :param name: Nom du jeu.
    :param description: Description du jeu.
    :param regle: Règles du jeu.
    :param icon: Icône représentant le jeu.
    """

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
    """
    Affiche un message de victoire pour un joueur.

    :param player: Nom du joueur gagnant.
    :param point: Points gagnés par le joueur.
    """
    display_box(
        titre="Victoire",
        text=f"bravo {player} vous gagnez {point} point",
        icon="🟢",
        padding=2,
        center_texte=True,
    )


def display_best_player(game_name: str):
    """
    Affiche le meilleur joueur d'un jeu spécifique.

    :param game_name: Nom du jeu.
    """
    best_player: list = data.get_top_score(game_name, 1)
    player_name: str = data.get_player_name(best_player[0][0])
    display_box(
        titre=f" meilleur joueur de {game_name}",
        text=f" {data.get_player_icon(player_name)} {player_name} avec {best_player[0][1]} point",
        icon="🟡",
        padding=2,
        center_texte=True,
    )

def display_game_ranking(id: int, n: int):
    """
    Affiche le classement des joueurs pour un jeu.

    :param id: ID du jeu.
    :param n: Nombre de joueurs à afficher dans le classement.
    """
    game_name: str = data.get_game_name(id)
    ranking: list = data.get_top_score(game_name, n)
    player_name: str = ""
    
    special_print("\n🟡 -------------- Score --------------🟡")

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

def display_player_score(player_id: int):
    """
    Affiche les scores d'un joueur donné.
    """
    texte: str = ""
    scores: list = data.get_player_scores(player_id)
    for i in range(len(scores)):
        texte += f"{data.get_game_name(i)} : {scores[i]}\n"

    display_box(text=texte, center_texte=True)
    time.sleep(3)
    clear_terminal()

# GAME TOOLS
def launch_game(game_name: str, function):
    """
    Lance un jeu, affiche une présentation et exécute sa logique principale.

    :param game_name: Nom du jeu à lancer.
    :param function: Fonction principale du jeu à exécuter.
    """
    players: list = []
    choice: int = 1

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

    display_best_player(game_name)
    time.sleep(2)
    clear_terminal()

    while choice == 1:
        function(players)
        display_box(text="voulez vous rejouer taper \n0. Non 1. Oui", center_texte=True)
        choice = ask_int("-> ", 0)
        clear_terminal()


# tools
def who_played() -> list:
    """
    Permet aux joueurs de s'identifier.

    :return: Liste contenant les pseudos des deux joueurs.
    """
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
                if (
                    len(pseudo) >= 14 or len(pseudo) <= 2
                    or (choice == 1 and pseudo == player_2_name)
                    or (choice == 2 and pseudo == player_1_name)
                ):
                    pseudo = ""
            if choice == 1:
                player_1_name = pseudo
            else:
                player_2_name = pseudo
        clear_terminal()

    if data.get_player_id(player_1_name) == -1:
        data.add_player(player_1_name, "🌵")

    if data.get_player_id(player_2_name) == -1:
        data.add_player(player_2_name, "🌵")

    return [player_1_name, player_2_name]


def choose_icon() -> str:
    """
    Permet à un joueur de choisir une icône.

    :return: Icône choisie par le joueur.
    """
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
    """
    Permet à un joueur de changer son icône.
    """
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
    """
    Affiche et permet de naviguer dans les classements globaux des jeux.
    """
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


def get_player() -> int:
    """
    Permet à un joueur de saisir son pseudo et retourne son ID s'il existe.

    :return: ID du joueur (entier) ou -1 si le joueur quitte ou si le pseudo n'existe pas.
    """
    answer: str = ""
    player_id: int = -1
    
    while answer == "" and answer != "A":
        display_box("","quelle est votre pseudo:\napuyer sur A pour quitter", center_texte= True)

        answer = ask_str("-> ","")

        if answer != 'A':
            if answer != "":
                player_id = data.get_player_id(answer)
                if player_id == -1:
                    answer = ""
                    special_print("se pseudo n'existe pas")
                time.sleep(1)
                clear_terminal()

    if answer == 'A':
        player_id = -1
    return player_id

def manage_score():
    """
    Permet à l'utilisateur de choisir entre afficher le classement général ou les scores
    associés à un joueur spécifique.
    """
    choice: int = 0

    while choice == 0:
        display_box(
            "",
            "que voulez vous faire\n1. afficher le classement\n2. afficher votre score",
            center_texte=True,
            padding=2,
            icon="📈",
        )

        choice = ask_int("-> ", 0)

        clear_terminal()

        if choice == 1:
            game_ranking()
        elif choice == 2:
            display_player_score(get_player())