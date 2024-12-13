from input_tool import get_player, ask_int, ask_str
import data
from display_tool import (
    display_box,
    display_line_jump,
    display_center_text,
    display_paragraph,
)
from clear import special_print, clear_terminal
import time


# Fonction pour afficher le meilleur joueur d'un jeu
def display_best_player(game_name: str):
    """
    Affiche le meilleur joueur d'un jeu spécifique.

    Arguments :
        game_name (str): Nom du jeu.
    """
    # Récupération du meilleur joueur et de son score
    best_player: list = data.get_top_score(game_name, 1)
    player_name: str = data.get_player_name(best_player[0][0])
    # Affichage des informations dans une boîte formatée
    display_box(
        titre=f" meilleur joueur de {game_name}",
        text=f" {data.get_player_icon(player_name)} {player_name} avec {best_player[0][1]} point",
        icon="🟡",
        padding=2,
        center_texte=True,
    )


# Fonction pour afficher le classement des joueurs pour un jeu


def display_game_ranking(id: int, n: int):
    """
    Affiche le classement des joueurs pour un jeu.

    Arguments :
        id (int): ID du jeu.
        n (int): Nombre de joueurs à afficher dans le classement.
    """
    # Récupération du nom du jeu et du classement des joueurs
    game_name: str = data.get_game_name(id)
    ranking: list = data.get_top_score(game_name, n)
    player_name: str = ""

    # Affichage du titre et du cadre du classement
    special_print("\n🟡 -------------- Score --------------🟡")
    display_line_jump()
    display_center_text(f"---- {game_name} ----")
    display_line_jump()

    # Génération du texte du classement
    paragraph = ""
    for i in range(n):
        player_name = data.get_player_name(ranking[i][0])
        paragraph += f"{i+1}. {data.get_player_icon(player_name)} {player_name} avec {ranking[i][1]} point\n"
    paragraph += f"<-Q {id+1}/4 D->"

    # Affichage du classement dans un format centralisé
    display_paragraph(paragraph, center=True, jump_line=True)
    special_print("🟡 -----------------------------------🟡\n")


# Fonction pour afficher les scores d'un joueur spécifique
def display_player_score(player_id: int):
    """
    Affiche les scores d'un joueur donné.

    Arguments :
        player_id (int): ID du joueur.
    """
    # Récupération des scores du joueur
    texte: str = ""
    scores: list = data.get_player_scores(player_id)
    for i in range(len(scores)):
        texte += f"{data.get_game_name(i)} : {scores[i]}\n"

    # Affichage des scores dans une boîte formatée
    display_box(text=texte, center_texte=True)
    time.sleep(3)
    clear_terminal()


# Fonction pour naviguer dans les classements des jeux
def game_ranking():
    """
    Affiche et permet de naviguer dans les classements globaux des jeux.
    """
    game_id: int = 0
    choice = ""
    display: bool = True

    while display:
        # Affichage du classement actuel
        choice = ""
        display_game_ranking(game_id, 5)
        special_print("A pour quitter")

        # Lecture de la commande utilisateur
        while choice != "D" and choice != "Q" and choice != "A":
            choice = ask_str("-> ", "")

        # Navigation dans les jeux ou sortie
        if choice == "D":
            game_id = (game_id + 1) % 4
        elif choice == "Q":
            game_id = (game_id - 1) % 4
        elif choice == "A":
            display = False

        clear_terminal()


# Fonction principale pour gérer les scores
def manage_score():
    """
    Permet à l'utilisateur de choisir entre afficher le classement général ou les scores
    associés à un joueur spécifique.
    """
    choice: int = 0

    while choice == 0:
        # Affichage du menu principal
        display_box(
            "",
            "que voulez vous faire\n1. afficher le classement\n2. afficher votre score",
            center_texte=True,
            padding=2,
            icon="📈",
        )

        # Lecture du choix utilisateur
        choice = ask_int("-> ", 0)
        clear_terminal()

        # Appel des fonctions correspondantes
        if choice == 1:
            game_ranking()
        elif choice == 2:
            display_player_score(get_player())
