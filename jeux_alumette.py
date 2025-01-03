import game_tool
from clear import clear, clear_terminal, special_print
import time
import data
import bot
import random


def get_bot_move(bot_level: int, matche_count: int) -> int:
    bot_move: int = 0
    match bot_level:
        case 2:
            if (random.randint(1, 3)) < 3:
                bot_move = bot.random_bot([1, 3])
            else:
                bot_move = bot.expert_bot_alumette(matche_count)
        case 3:
            bot_move = bot.expert_bot_alumette(matche_count)
        case 1 | _:
            bot_move = bot.random_bot([1, 3])
    return bot_move


def display_game(matche_count: int):
    """
    Affiche le nombre d'allumettes restantes avec une représentation visuelle.

    Arguments :
        matches_number (int): Nombre d'allumettes restantes dans le jeu.
    """
    # Affichage des allumettes restantes avec un visuel utilisant des emojis.
    game_tool.display_box(
        text=f"Nombre d'allumettes restantes : {matche_count}\n"
        + "Allumettes : \n"
        + "🔥" * matche_count,
        padding=1,
        center_texte=True,
    )


def matche_game(players: list):
    """
    Gère le déroulement du jeu des allumettes entre deux joueurs.

    Les joueurs retirent à tour de rôle 1, 2 ou 3 allumettes d'un total initial de 21.
    Le joueur qui doit retirer la dernière allumette perd la partie.

    Arguments:
        players (list): Une liste contenant les noms des deux joueurs.
        Le premier joueur dans la liste commence la partie.
    """
    # Initialisation des variables pour suivre le jeu.
    current_player: str
    other_player: str
    matche_count: int = 21
    choice: int
    temp: str

    # Définition des joueurs en fonction de l'ordre donné.
    current_player = players[0]
    other_player = players[1]

    while matche_count > 0:
        # Afficher l'état actuel des allumettes.
        display_game(matche_count)

        choice = 0
        while choice != 1 and choice != 2 and choice != 3:
            # Demander au joueur actuel combien d'allumettes retirer.
            choice = game_tool.ask_int(
                f"Joueur {current_player}, combien d'allumettes souhaitez-vous retirer ? (1, 2 ou 3) : ",
                0,
            )
            clear(0)

        # Mettre à jour le nombre d'allumettes restantes.
        matche_count -= choice

        if matche_count <= 0:
            # Annoncer la défaite du joueur qui doit prendre la dernière allumette.
            special_print(
                f"Le joueur {current_player} a pris la dernière allumette. Le joueur {other_player} a perdu !"
            )

        # Alterner les rôles des joueurs.
        temp = current_player
        current_player = other_player
        other_player = temp

        clear_terminal()

    # Afficher la victoire du joueur gagnant et mettre à jour les scores.
    game_tool.display_victory(current_player, 1)
    data.add_score_point(current_player, "allumetes", 1)
    time.sleep(4)
    clear_terminal()
