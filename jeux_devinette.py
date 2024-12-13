import game_tool
import data
from clear import clear_terminal
import time

def get_limite(name_player_choose: str):
    """
    Permet à un joueur de choisir une limite strictement superieur à 0 pour le jeux

    Arguments:
        name_player_choose (str): Le nom du joueur qui choisit le nombre.
    """

    limite: int = 0

    # affiche la boite de dialogue
    game_tool.display_box(
        text=f"{name_player_choose} veuillez choisir une limite",
        center_texte=True,
    )

    # attend un choix valide
    while limite <= 0:
        limite = game_tool.ask_int("-> ", 0)

    clear_terminal()

    return limite

def get_nombre_choisi(name_player_choose:str):
    """
    Permet à un joueur de choisir un nombre entre 1 et 1000.

    Affiche une boîte de dialogue demandant au joueur de sélectionner un nombre valide 
    et s'assure que la valeur choisie est comprise dans l'intervalle accepté.

    Arguments:
        name_player_choose (str): Le nom du joueur qui choisit le nombre.
    """
    number_choose: int = 0

    limite: int = get_limite(name_player_choose)

    # affiche la boite de dialogue
    game_tool.display_box(
        text=f"{name_player_choose} veuillez choisir un nombre entre 1 et {limite} ? ",
        center_texte=True,
    )

    # attend un choix valide
    while number_choose < 1 or number_choose > limite:
        number_choose = game_tool.ask_int("-> ", 0)

    clear_terminal()

    return number_choose


def deviner_nombre(number_choose: int, name_player_guess: str) -> int:
    """
    Permet à un joueur de deviner un nombre donné.

    Le joueur entre des propositions jusqu'à trouver la bonne réponse. À chaque tentative, 
    un message indique si le nombre proposé est trop grand, trop petit, ou correct.

    Arguments :
        number_choose (int): Le nombre que le joueur doit deviner.
        name_player_guess (str): Le nom du joueur qui devine le nombre.

    Retourne :
        int: Le nombre de tentatives nécessaires pour deviner le nombre.
    """
    number_test: int = None
    cmpt_try: int = 0

    # affiche une boite de dialogue qui apairait au debut quand aucune proposition n'a etait faite
    game_tool.display_box(
        text=f"nombre d'essai: {cmpt_try} \n---------------------------",
        center_texte=True,
    )

    # tant que le nombre que donne le joueur et diferent du nombre à trouver
    while number_test != number_choose:
        # demande un nombre
        number_test = game_tool.ask_int(
            f"{name_player_guess}, devinez le nombre : ", None
        )
        # si le nombre est valide alors
        if number_test is not None and number_test >= 0 and number_test <= 1000:
            clear_terminal()

            # le nombre d'essai est augmenté de 1
            cmpt_try += 1

            # regarder si le nombre est le bon est affiche donc une boite de victoire avec le nombre d'essai
            if number_test == number_choose:
                game_tool.display_box(
                    text=f"Bravo {name_player_guess} vous avez trouvé en : {cmpt_try} essai",
                    center_texte=True,
                    padding=2,
                )
                time.sleep(2)
                clear_terminal()
                
            # sinon teste si plus grand ou plus pettit et affiche la boite corespondante
            elif number_test < number_choose:
                game_tool.display_box(
                    text=f"nombre d'essai: {cmpt_try} \nTrop petit ↘",
                    center_texte=True,
                    icon="↘️",
                )
            else:
                game_tool.display_box(
                    text=f"nombre d'essai: {cmpt_try} \nTrop grand ↗",
                    center_texte=True,
                    icon="↗️",
                )
    return cmpt_try


def launch(players: list):
    """
    Lance une partie de devinette entre deux joueurs.

    Chaque joueur choisit un nombre à faire deviner à son adversaire. 
    Le joueur ayant deviné le nombre en moins de tentatives remporte la partie. 
    En cas d'égalité, le résultat est un match nul.

    Arguments:
        players (list): Une liste contenant les noms des deux joueurs.
        Le premier joueur dans la liste commence la partie.
    """
    player_1: str = players[0]
    player_2: str = players[1]

    player_1_cmpt: int = 0
    player_2_cmpt: int = 0

    nombre_a_deviner: int

    name_player_win: str

    # c'est au premier joueur de choisir un nombre et une limite puis a l'autre de devniner
    nombre_a_deviner = get_nombre_choisi(player_2)
    player_1_cmpt = deviner_nombre(nombre_a_deviner, player_1)

    # et les roles s'inverse
    nombre_a_deviner = get_nombre_choisi(player_1)
    player_2_cmpt = deviner_nombre(nombre_a_deviner, player_2)

    if player_1_cmpt < player_2_cmpt:
        name_player_win = player_1
    else:
        name_player_win = player_2

    # si les deux utilisateurs on autant d'essai chacun
    if player_1_cmpt == player_2_cmpt:
        game_tool.display_box("Match nul", " personne ne gagne de point")
    else:
        game_tool.display_victory(name_player_win, 1)
        # rajoute un point à l'utilisateur qui à gagné
        data.add_score_point(name_player_win, "devinette", 1)

    # tout effacer aprés 2s
    time.sleep(2)
    clear_terminal()
