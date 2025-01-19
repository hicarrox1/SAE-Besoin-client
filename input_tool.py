from clear import special_input, clear_one_line, clear_terminal
from display_tool import display_box


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


def ask_pseudo():
    """
    Permet à un joueur de choisir son pseudo.

    Retourne :
        str: Pseudo du joueur.
    """
    pseudo: str = ""

    # Affichage de la boîte de dialogue
    display_box(
        "",
        "Veuillez saisir votre pseudo\n(entre 3 et 10 caractères)",
        center_texte=True,
        padding=2,
        icon="👤",
    )

    # Lecture du pseudo
    while len(pseudo) < 3 or len(pseudo) > 10:
        pseudo = ask_str("-> ", "")

    return pseudo


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
        icon="🤖",
    )

    while bot_level != 1 and bot_level != 2 and bot_level != 3:
        bot_level = ask_int("Your choice : ", 0)
    clear_terminal()
    return bot_level
