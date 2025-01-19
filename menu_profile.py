from input_tool import ask_int, ask_pseudo
import data
from display_tool import display_box
from clear import clear_terminal, special_print
import time


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
            f"icon: {icon} \n1.🌞 2.🐵 3.🦖 4.🌷 5.🍔 6.🌵 7.🐘\n 8. selectioner",
            center_texte=True,
            padding=2,
            icon="🦲",
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


def manage_profil():
    """
    Permet au joueur de gérer leur profils.
    """
    run: bool = True
    choice: int = 0
    player_name: str

    while run:
        # boite de dialogue qui demande au joueur de choisir une action
        display_box(
            "profil",
            "1. Créer un profil\n2. Gérer un profil\n3. Quitter",
            center_texte=True,
            padding=2,
            icon="👤",
        )

        choice = ask_int("-> ", 0)

        # En fonction du choix de l'utilisateur on lance une action
        if choice == 1:
            # Création d'un profil
            clear_terminal()
            create_profil()
            run = False
        elif choice == 2:
            # Gestion d'un profil
            clear_terminal()
            player_name = ask_pseudo()
            # Vérification de l'existence du joueur
            if data.get_player_id(player_name) != -1:
                # Si le joueur existe on affiche le menu de gestion de profil
                clear_terminal()
                profil_menu(player_name)
                run = False
            else:
                # Si le joueur n'existe pas on affiche un message d'erreur
                special_print("Ce joueur n'existe pas !")
                time.sleep(2)
                clear_terminal()
        elif choice == 3:
            # fin du menu
            run = False
            clear_terminal()


def create_profil():
    """
    Permet à un joueur de créer un profil.
    """
    pseudo: str = ""
    player_icon: str

    # boite de dialogue qui demande au joueur de choisir un pseudo et une icône
    display_box(
        "Profil",
        "Veuillez choisir un pseudo et une icône.",
        center_texte=True,
        padding=0,
        icon="👤",
    )
    time.sleep(2)
    clear_terminal()

    # Tant que le pseudo n'est pas choisi ou qu'il est déjà pris on demande au joueur de choisir un pseudo
    while pseudo == "" or data.get_player_id(pseudo) != -1:
        pseudo = ask_pseudo()
        if data.get_player_id(pseudo) == -1:
            clear_terminal()
        else:
            special_print("Ce pseudo est déjà pris !")
            time.sleep(2)
            clear_terminal()

    player_icon = choose_icon()
    clear_terminal()

    # Ajout du joueur au données
    data.add_player(pseudo, player_icon)
    data.save_player_data()

    display_box(
        "Profil",
        "Profil créé avec succès !",
        center_texte=True,
        padding=0,
        icon="🟢",
    )
    time.sleep(1)
    clear_terminal()


def profil_menu(pseudo: str):
    """
    Permet à un joueur de gérer son profil.
    Args:
        pseudo (str): Pseudo du joueur.
    """
    text: str = f"\n{data.get_player_score_text(data.get_player_id(pseudo))}"
    run: bool = True
    choice: int = 0
    player_icon: str = data.get_player_icon(pseudo)
    first_pseudo: str = pseudo
    modif: bool = False
    pseudo_test: str

    # Boucle principale jusqu'à ce que l'utilisateur quitte le menu
    while run:
        display_box(
            titre=f"{player_icon} {pseudo}",
            text=f"{text}\n{'-' * 25}\n1. Changer de pseudo\n2. Changer d'icon\n3. Save\n{'-' * 25}",
            center_texte=False,
            padding=2,
            icon="👤",
        )

        choice = ask_int("-> ", 0)

        # En fonction du choix de l'utilisateur on lance une action
        if choice == 1:
            # Changement du pseudo du joueur
            clear_terminal()
            pseudo_test = ask_pseudo()
            # Vérification de la disponibilité du pseudo
            if data.get_player_id(pseudo_test) != -1:
                special_print("Ce pseudo est déjà pris !")
                time.sleep(2)
                clear_terminal()
                modif = False
            else:
                pseudo = pseudo_test
                modif = True
        elif choice == 2:
            # Changement de l'icône du joueur
            clear_terminal()
            player_icon = choose_icon()
            modif = True
        elif choice == 3:
            # fin du menu
            run = False

        clear_terminal()

    if modif:
        # Sauvegarde des données du joueur si des modifications ont été apportées
        data.set_player_icon(first_pseudo, player_icon)
        if pseudo != first_pseudo:
            data.set_player_name(first_pseudo, pseudo)
        data.save_player_data()
