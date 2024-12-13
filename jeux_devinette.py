import game_tool
import data
from clear import clear_terminal
import time


def get_nombre_choisi(name_player_choose):
    number_choose = 0
    game_tool.display_box(
        text=f"{name_player_choose} veuillez choisir un nombre entre 1 et 1000 ? ",
        center_texte=True,
    )
    while number_choose < 1 or number_choose > 1000:
        number_choose = game_tool.ask_int("-> ", 0)
    clear_terminal()
    return number_choose


def deviner_nombre(number_choose, name_player_guess):
    number_test = None
    cmpt_try = 0
    game_tool.display_box(
        text=f"nombre d'essai: {cmpt_try} \n---------------------------",
        center_texte=True,
    )
    while number_test != number_choose:
        number_test = game_tool.ask_int(
            f"{name_player_guess}, devinez le nombre : ", None
        )
        if number_test is not None and number_test >= 0 and number_test <= 1000:
            clear_terminal()
            cmpt_try += 1
            if number_test == number_choose:
                game_tool.display_box(
                    text=f"Bravo {name_player_guess} vous avez trouvé en : {cmpt_try} essai",
                    center_texte=True,
                    padding=2,
                )
                time.sleep(2)
                clear_terminal()
                return cmpt_try
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


def launch(players: list):
    player_1 = players[0]
    player_2 = players[1]

    player_1_cmpt = 0
    player_2_cmpt = 0

    nombre_a_deviner = get_nombre_choisi(player_2)
    player_1_cmpt = deviner_nombre(nombre_a_deviner, player_1)

    nombre_a_deviner = get_nombre_choisi(player_1)
    player_2_cmpt = deviner_nombre(nombre_a_deviner, player_2)

    if player_1_cmpt < player_2_cmpt:
        name_player_win = player_1
    else:
        name_player_win = player_2

    if player_1_cmpt == player_2_cmpt:
        game_tool.display_box("Match nul", " personne ne gagne de point")
        time.sleep(4)
        clear_terminal()
    else:
        game_tool.display_victory(name_player_win, 1)
        data.add_score_point(name_player_win, "devinette", 1)
        time.sleep(2)
        clear_terminal()
