import game_tool
import data
from clear import clear_terminal, special_print
import time
import bot
from PlayerInfo import PlayerInfo
import random

def get_bot_move(
    bot_level: int, max_limit: int, greater: bool, old_move: int, number_limit: list[int], first: bool
) -> int:
    bot_move: int = 0
    match bot_level:
        case 2:
            if first:
                return bot.random_bot([1, max_limit])
            else:
                bot_move = bot.middle_bot_devinette(greater, old_move, number_limit)
        case 3:
            if first:
                return bot.random_bot([1, max_limit])
            else:
                bot_move = bot.expert_bot_devinette(greater, old_move, number_limit)
        case 1 | _:
            bot_move = bot.random_bot([1, max_limit])
    return bot_move


def get_limit(name_player_choose: str):
    """
    Permet à un joueur de choisir une limite strictement superieur à 0 pour le jeux

    Arguments:
        name_player_choose (str): Le nom du joueur qui choisit le nombre.
    """

    limit: int = 0

    # affiche la boite de dialogue
    game_tool.display_box(
        text=f"{name_player_choose} veuillez choisir une limite",
        center_texte=True,
    )

    # attend un choix valide
    while limit <= 0:
        limit = game_tool.ask_int("-> ", 0)

    clear_terminal()

    return limit


def get_chosen_number(name_player_choose: str) -> list[int]:
    """
    Permet à un joueur de choisir un nombre entre 1 et 1000.

    Affiche une boîte de dialogue demandant au joueur de sélectionner un nombre valide
    et s'assure que la valeur choisie est comprise dans l'intervalle accepté.

    Arguments:
        name_player_choose (str): Le nom du joueur qui choisit le nombre.
    """
    chosen_number: int = 0

    limit: int = get_limit(name_player_choose)

    # affiche la boite de dialogue
    game_tool.display_box(
        text=f"{name_player_choose} veuillez choisir un nombre entre 1 et {limit} ? ",
        center_texte=True,
    )

    # attend un choix valide
    while chosen_number < 1 or chosen_number > limit:
        chosen_number = game_tool.ask_int("-> ", 0)

    clear_terminal()

    return chosen_number,limit


def guess_number(number_choose: int, player_info: PlayerInfo, limit: int) -> int:
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
    number_test: int = 0
    cmpt_try: int = 0
    player_name: str= player_info.pseudo
    greater: bool = False

    first: bool = True

    if greater:
        borne: list = [1,number_test]
    else:
        borne: list = [number_test,limit-1]

    # affiche une boite de dialogue qui apairait au debut quand aucune proposition n'a etait faite
    game_tool.display_box(
        text=f"limite: {limit}\nnombre d'essai: {cmpt_try} \n---------------------------",
        center_texte=True,
    )

    if player_info.is_bot:
        special_print(f"{player_name} a choisi : ...")

    # tant que le nombre que donne le joueur et diferent du nombre à trouver
    while number_test != number_choose:
        # demande un nombre

        if player_info.is_bot:
            number_test = get_bot_move(player_info.bot_level, limit-1, greater, number_test, borne, first)
            first = False
            time.sleep(1.5)
        else:
            number_test = game_tool.ask_int(
            f"{player_name}, devinez le nombre : ", None
        )
        # si le nombre est valide alors
        if number_test is not None and number_test >= 0 and number_test <= 1000:
            clear_terminal()

            # le nombre d'essai est augmenté de 1
            cmpt_try += 1

            # regarder si le nombre est le bon est affiche donc une boite de victoire avec le nombre d'essai
            if number_test == number_choose:
                game_tool.display_box(
                    text=f"Bravo {player_name} vous avez trouvé en : {cmpt_try} essai",
                    center_texte=True,
                    padding=2,
                )
                time.sleep(2)
                clear_terminal()

            # sinon teste si plus grand ou plus pettit et affiche la boite corespondante
            elif number_test < number_choose:
                if number_test > borne[0]:
                    borne[0] = number_test
                game_tool.display_box(
                    text=f"limite: {limit}\nnombre d'essai: {cmpt_try} \nTrop petit ↘",
                    center_texte=True,
                    icon="↘️",
                )
                greater=False
            else:
                if number_test < borne[1]:
                    borne[1] = number_test
                game_tool.display_box(
                    text=f"limite: {limit}\nnombre d'essai: {cmpt_try} \nTrop grand ↗",
                    center_texte=True,
                    icon="↗️",
                )
                greater=True

            if player_info.is_bot:
                special_print(f"{player_name} a choisi : {number_test}")

    return cmpt_try


def launch(players: list[PlayerInfo]):
    """
    Lance une partie de devinette entre deux joueurs.

    Chaque joueur choisit un nombre à faire deviner à son adversaire.
    Le joueur ayant deviné le nombre en moins de tentatives remporte la partie.
    En cas d'égalité, le résultat est un match nul.

    Arguments:
        players (list): Une liste contenant les noms des deux joueurs.
        Le premier joueur dans la liste commence la partie.
    """
    player_1: PlayerInfo = players[0]
    player_2: PlayerInfo = players[1]

    player_1_cmpt: int = 0
    player_2_cmpt: int = 0

    number_to_guess: int
    limit:int
    chosen_number: list[int] = []

    player_win: PlayerInfo

    # c'est au premier joueur de choisir un nombre et une limite puis a l'autre de devniner
    if player_2.is_bot:
        number_to_guess = bot.random_bot([1, 1000])
        limit = 1000
    else:
        chosen_number = get_chosen_number(player_2.pseudo)
        number_to_guess = chosen_number[0]
        limit = number_to_guess[1]
    player_1_cmpt = guess_number(number_to_guess, player_1, limit)

    # et les roles s'inverse
    if player_1.is_bot:
        number_to_guess = bot.random_bot([1, 1000])
        limit = 1000
    else:
        chosen_number = get_chosen_number(player_1.pseudo)
        number_to_guess = chosen_number[0]
        limit = number_to_guess[1]
    player_2_cmpt = guess_number(number_to_guess, player_2, limit)

    if player_1_cmpt < player_2_cmpt:
        player_win = player_1
    else:
        player_win = player_2

    # si les deux utilisateurs on autant d'essai chacun
    if player_1_cmpt == player_2_cmpt:
        game_tool.display_box("Match nul", " personne ne gagne de point")
    else:
        game_tool.display_victory(player_win.pseudo, 1)
        # rajoute un point à l'utilisateur qui à gagné
        if player_win.is_bot == False:
            data.add_score_point(player_win.pseudo, "devinette", 1)

    # tout effacer aprés 2s
    time.sleep(2)
    clear_terminal()


