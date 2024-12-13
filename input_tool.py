from clear import special_input, special_print, clear_one_line, clear_terminal
from display_tool import display_box
import time
import data


# INPUT
def ask_int(question: str, default: int):
    """
    Demande une entrée entière à l'utilisateur et retourne cette valeur.
    Si l'utilisateur saisit une valeur non valide, la valeur par défaut est retournée.

    Arguments :
        question (str) : La question à afficher à l'utilisateur.
        default (int) : La valeur par défaut si l'entrée est invalide.

    Retourne :
        int : La valeur entière saisie par l'utilisateur ou la valeur par défaut.
    """
    choice: int = default
    try:
        # Demande une entrée utilisateur et tente de la convertir en entier
        choice = int(special_input(question))
        clear_one_line()  # Efface la ligne de saisie dans le terminal
    except ValueError:
        # Si une valeur non entière est saisie ou autre erreur, retourne la valeur par défaut
        clear_one_line()  # Efface la ligne de saisie dans le terminal
    return choice


def ask_str(question: str, default: str):
    """
    Demande une entrée texte à l'utilisateur et retourne cette valeur.
    Si une exception survient, la valeur par défaut est retournée.

    Arguments :
        question (str) : La question à afficher à l'utilisateur.
        default (str) : La valeur par défaut si une erreur survient.

    Retourne :
        str : La chaîne saisie par l'utilisateur ou la valeur par défaut.
    """
    choice: str = default
    try:
        # Demande une entrée utilisateur sous forme de texte
        choice = special_input(question)
        clear_one_line()  # Efface la ligne de saisie dans le terminal
    except ValueError:
        # Si une exception survient, retourne la valeur par défaut
        clear_one_line()  # Efface la ligne de saisie dans le terminal
    return choice


# Fonction pour récupérer l'ID d'un joueur à partir de son pseudo
def get_player() -> int:
    """
    Permet à un joueur de saisir son pseudo et retourne son ID s'il existe.

    Retourne :
        int: ID du joueur (entier) ou -1 si le joueur quitte ou si le pseudo n'existe pas.
    """
    answer: str = ""
    player_id: int = -1

    while answer == "" and answer != "A":
        # Affichage de la boîte pour demander le pseudo
        display_box(
            "", "quelle est votre pseudo:\napuyer sur A pour quitter", center_texte=True
        )

        # Lecture de l'entrée utilisateur
        answer = ask_str("-> ", "")

        if answer != "A":
            if answer != "":
                # Vérification de l'existence du pseudo
                player_id = data.get_player_id(answer)
                if player_id == -1:
                    answer = ""
                    special_print("se pseudo n'existe pas")
                time.sleep(1)
                clear_terminal()

    # Si le joueur choisit de quitter, on retourne -1
    if answer == "A":
        player_id = -1
    return player_id
