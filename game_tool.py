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
from PlayerInfo import PlayerInfo

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
    filler_animation_tool.slider(5, 36, game_data[2], "▪️", "▫️")
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
    # Boucle principale jusqu'à ce que les deux joueurs soient enregistrés et que le jeu commence
    player1_info = who_play2(1)
    player2_info = who_play2(2)

    # Ajoute les joueurs à la base de données s'ils n'existent pas encore
    if player1_info.is_bot == False:
        if data.get_player_id(player1_info.pseudo) == -1:
            data.add_player(player1_info.pseudo, "🌵")

    if player2_info.is_bot == False:
        if data.get_player_id(player2_info.pseudo) == -1:
            data.add_player(player2_info.pseudo, "🌵")

    return [player1_info, player2_info]

def who_play2(player_number: int) -> PlayerInfo:
    """     
    Permet aux joueurs de s'identifier.

    Arguments :
        player_number (int): Numéro du joueur en cours (1 ou 2).
    
    Retourne : 
        PlayerInfo: Informations du joueur.

    """

    # Initialisation des noms de joueurs et variables de contrôle
    pseudo: str = "..."
    choice: int = 0

    bot: bool = False
    bot_level: int = 0

    titre= "Player 1" if player_number == 1 else "Player 2"

    # Boucle principale jusqu'à ce que les deux joueurs soient enregistrés et que le jeu commence
    
    choice = 0
    pseudo = ""
    display_box(
        f"{titre}",
        f"1. Player 2. Bot   \n3.Start",
        center_texte=True,
    )

    # Attente d'un choix valide (1, 2)
    while choice != 1 and choice != 2:
        choice = ask_int("Votre choix : ", 0)

    if choice == 1:
        while pseudo == "":
            bot = False
            pseudo = ask_str("quelle est votre pseudo: ", "")
            # Vérification des contraintes sur le pseudo
            if len(pseudo) >= 14 or len(pseudo) <= 2 or pseudo == "":
                pseudo = ""
        clear_terminal()

    elif choice == 2:
        bot = True

        clear_terminal()

        bot_level = get_bot_level()

        pseudo = f"Bot{player_number} {"Easy" if bot_level == 1 else "Medium" if bot_level == 2 else "Hard"}"

    return PlayerInfo(pseudo,bot, bot_level)



def get_bot_level():
    """
    Permet de choisir le niveau de difficulté du bot.

    Retourne :
        int: Niveau de difficulté du bot (1, 2 ou 3).
    """

    bot_level: int = 0

    display_box(
        "Bot level",
        "1. Easy\n2. Medium\n3. Hard",
        center_texte=True,
    )

    while bot_level != 1 and bot_level != 2 and bot_level != 3:
        bot_level = ask_int("Your choice : ", 0)
    clear_terminal()
    return bot_level

