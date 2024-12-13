import filler_animation_tool
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
)
from menu_score import display_best_player
from input_tool import ask_int, ask_str


# Outil du jeux


# affichage prefabriquer


def display_game_presentation(name: str, description: str, regle: str, icon: str):
    """
    Affiche une présentation du jeu, comprenant le nom, la description et les règles.

    Arguments :
        name (str): Nom du jeu.
        description (str): Description du jeu.
        regle (str): Règles du jeu.
        icon (str): Icône représentant le jeu.
    """

    # affichage debut du menu pour presenter le jeux

    special_print(f"\n{icon} -------------- Game ---------------{icon}")
    special_print("| Bienvenue sur le jeux:                |")

    # Centre le nom
    display_center_text(name)
    # Affichage de la description
    display_center_text("---- desc ----")
    display_paragraph(description, padding=1, center=False)
    # Affichage des règles
    display_center_text("---- regle ----")
    display_paragraph(regle, center=True)

    special_print(f"{icon} -----------------------------------{icon}\n")


def display_victory(player: str, point: int):
    """
    Affiche un message de victoire pour un joueur.

    Arguments :
        player (str): Nom du joueur gagnant.
        point (int): Points gagnés par le joueur.
    """
    display_box(
        titre="Victoire",
        text=f"bravo {player} vous gagnez {point} point",
        icon="🟢",
        padding=2,
        center_texte=True,
    )


# lancer un jeux


def launch_game(game_name: str, function):
    """
    Lance un jeu, affiche une présentation et exécute sa logique principale.

    Arguments :
        game_name (str): Nom du jeu à lancer.
        function (function): Fonction principale du jeu à exécuter.
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
    filler_animation_tool.slider(10, 36, game_data[2], "▪️", "▫️")
    # efface l'ecran aprés la fin du filler de 5s avec la taille de la presentation et celle du filler
    clear(1)
    clear_terminal()

    # lance la fonction de {jeux}

    # demande qui joue
    players = who_played()

    # affiche le meilleur joueur du jeux
    display_best_player(game_name)
    time.sleep(2)
    clear_terminal()

    # lance le jeux puis demande lorsque le jeux et finis si ils veuleut rejouer
    while choice == 1:
        function(players)

        # lorsque sort du jeux
        display_box(text="voulez vous rejouer taper \n0. Non 1. Oui", center_texte=True)
        choice = ask_int("-> ", 0)
        clear_terminal()


def who_played() -> list:
    """
    Permet aux joueurs de s'identifier.

    Retourne :
        list: Liste contenant les pseudos des deux joueurs.
    """
    # Initialisation des noms de joueurs et variables de contrôle
    player_1_name: str = "..."
    player_2_name: str = "..."
    pseudo: str = ""
    choice: int = 0
    start: bool = False

    # Boucle principale jusqu'à ce que les deux joueurs soient enregistrés et que le jeu commence
    while player_1_name == "..." or player_2_name == "..." or not start:
        choice = 0
        pseudo = ""
        display_box(
            "quelle sont vos pseudo",
            f"1. {player_1_name} 2. {player_2_name}\n3. Start",
            center_texte=True,
        )

        # Attente d'un choix valide (1, 2 ou 3)
        while choice != 1 and choice != 2 and choice != 3:
            choice = ask_int("Votre choix : ", 0)

        # Si choix == 3 et que les deux pseudos sont valides, on peut commencer
        if choice == 3 and player_1_name != "..." and player_2_name != "...":
            start = True
        # Sinon, permet de modifier le pseudo d'un joueur
        elif choice == 1 or choice == 2:
            while pseudo == "":
                pseudo = ask_str("quelle est votre pseudo: ", "")
                # Vérification des contraintes sur le pseudo
                if (
                    len(pseudo) >= 14
                    or len(pseudo) <= 2
                    or (choice == 1 and pseudo == player_2_name)
                    or (choice == 2 and pseudo == player_1_name)
                ):
                    pseudo = ""
            # Assigne le pseudo au joueur correspondant
            if choice == 1:
                player_1_name = pseudo
            else:
                player_2_name = pseudo
        clear_terminal()

    # Ajoute les joueurs à la base de données s'ils n'existent pas encore
    if data.get_player_id(player_1_name) == -1:
        data.add_player(player_1_name, "🌵")

    if data.get_player_id(player_2_name) == -1:
        data.add_player(player_2_name, "🌵")

    return [player_1_name, player_2_name]
