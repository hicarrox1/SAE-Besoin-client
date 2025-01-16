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
