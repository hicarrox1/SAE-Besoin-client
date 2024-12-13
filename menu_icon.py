from input_tool import ask_int, ask_str
import data
from display_tool import display_box
from clear import clear_terminal


def choose_icon() -> str:
    """
    Permet à un joueur de choisir une icône.

    Retourne :
        str: Icône choisie par le joueur.
    """
    icon: str = ".."  # Icône initiale (indéfinie)
    choice: int = 0
    change: bool = False
    # Liste des icônes disponibles
    icons: list = ["🌞", "🐵", "🦖", "🌷", "🍔", "🌵", "🐘"]

    # Tant que l'icône n'est pas choisie ou que l'utisateur n'a pas choisi de changer le menu attend
    while icon == ".." or not change:
        choice = 0
        display_box(
            "choisissez votre icon",
            f"icon: {icon} \n1.🌞 2.🐵 3.🦖 4.🌷 5.🍔 6.🌵 7.🐘\n 8. Change",
            center_texte=True,
            padding=2,
            icon="👤",
        )

        # S'assure que le choix est valide
        while choice not in [1, 2, 3, 4, 5, 6, 7, 8]:
            choice = ask_int("Votre choix : ", 0)

        # sort de la boucle si l'icon et choisi et que l'utisateur à choisi de changer
        if choice == 8 and icon != "..":
            change = True
        else:
            # si l'utilisateur n'a pas cliquer sur changer alors il a choisi une icon
            icon = icons[choice - 1]

        clear_terminal()

    return icon


def change_icon_menu():
    """
    Permet à un joueur de changer son icône.
    """
    icon: str = ".."
    pseudo: str = "..."
    choice: int = 0
    change: bool = False

    # Tant que l'icône ou le pseudo ne sont pas définis et que l'utisateur n'a pas choisi de changer le menu attend
    while icon == ".." or pseudo == ".." or not change:
        choice = 0
        display_box(
            "",
            f"1. pseudo: {pseudo} 2. icon: {icon}\n3. Change",
            center_texte=True,
            padding=2,
            icon="🦲",
        )

        # assure un choix valide soit 1 soit 2 soit 3
        while choice != 1 and choice != 2 and choice != 3:
            choice = ask_int("Votre choix : ", 0)

        # si le choix et de changer et que l'icon et le pseudo sont mis alors on change l'icon
        if choice == 3 and icon != ".." and pseudo != "...":
            change = True
        elif choice == 1:
            # sinon si l'utilisateur veut saisir sont pseudo on lui demande et regarde si il existe
            while pseudo == "...":
                pseudo = ask_str("quelle est votre pseudo: ", "...")
                if len(pseudo) >= 8 or data.get_player_id(pseudo) == -1:
                    pseudo = "..."
        elif choice == 2:
            # sinon on ouvre le menu de selection d'icon
            clear_terminal()
            icon = choose_icon()

        clear_terminal()

    data.set_player_icon(pseudo, icon)
