import game_tool
from clear import clear, clear_terminal, special_print
import time
import data
import random
from PlayerInfo import PlayerInfo


def expert_bot_alumette(matche_count: int) -> int:
    """
    Détermine le meilleur coup à jouer pour le bot de niveau 3 en fonction du nombre d'allumettes restantes.
    Arguments:
        matche_count (int): Nombre d'allumettes restantes dans le jeu.
    Returns:
        int: Nombre d'allumettes à retirer pour le bot.
    """
    best_option: int

    # La position perdante est celle où il reste 1 allumette (n == 1) ou un multiple de 4 + 1.
    if matche_count % 4 == 1:
        # Aucun coup possible pour gagner, l'adversaire a déjà une position perdante
        best_option = random.randint(1, 3)
    else:
        # Le meilleur coup consiste à ramener l'adversaire à une position perdante
        # Trouver le plus grand coup possible pour laisser un nombre d'allumettes multiple de 4 + 1
        for i in range(1, 4):
            if (matche_count - i) % 4 == 1:
                best_option = i  # On retourne le nombre d'allumettes à enlever

    return best_option


def get_bot_move(bot_level: int, matche_count: int) -> int:
    """
    Determine le coup à jouer pour le bot en fonction de son niveau de difficulté.
    Arguments:
        bot_level (int): Niveau de difficulté du bot (1, 2 ou 3).
        matche_count (int): Nombre d'allumettes restantes dans le jeu.
    Returns:
        int: Nombre d'allumettes à retirer par le bot.
    """
    bot_move: int = 0
    # Déterminer le coup à jouer en fonction du niveau de difficulté du bot.
    match bot_level:
        case 2:
            # Le bot de niveau 2 choisit un coup aléatoire ou expert de manière aléatoire.
            if (random.randint(1, 2)) == 1:
                bot_move = random.randint(1, 3)
            else:
                bot_move = expert_bot_alumette(matche_count)
        case 3:
            # Le bot de niveau 3 choisit un coup pour gagner a chaque fois (sauf si le joueur commence et joue parfaitement).
            bot_move = expert_bot_alumette(matche_count)
        case 1 | _:
            # Le bot de niveau 1 choisit un coup aléatoire.
            bot_move = random.randint(1, 3)
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


def matche_game(players: list[PlayerInfo]):
    """
    Gère le déroulement du jeu des allumettes entre deux joueurs.

    Les joueurs retirent à tour de rôle 1, 2 ou 3 allumettes d'un total initial de 21.
    Le joueur qui doit retirer la dernière allumette perd la partie.

    Arguments:
        players (list): Une liste contenant les noms des deux joueurs.
        Le premier joueur dans la liste commence la partie.
    """
    # Initialisation des variables pour suivre le jeu.
    current_player: PlayerInfo
    other_player: PlayerInfo
    matche_count: int = 21
    choice: int
    temp: PlayerInfo

    # Définition des joueurs en fonction de l'ordre donné.
    current_player = players[0]
    other_player = players[1]

    while matche_count > 0:
        # Afficher l'état actuel des allumettes.
        display_game(matche_count)

        choice = 0
        while choice != 1 and choice != 2 and choice != 3:
            # Si le joueur actuel est un bot, choisir un coup automatiquement. Sinon, demander au joueur de choisir.
            if not current_player.is_bot:
                # Demander au joueur actuel combien d'allumettes retirer.
                choice = game_tool.ask_int(
                    f"Joueur {current_player.pseudo}, combien d'allumettes souhaitez-vous retirer ? (1, 2 ou 3) : ",
                    0,
                )
                clear(0)
            else:
                # Le bot choisit un coup en fonction de son niveau de difficulté.
                choice = get_bot_move(current_player.bot_level, matche_count)
                special_print(
                    f"Le bot {current_player.pseudo} retire {choice} allumettes."
                )
                time.sleep(2)
                clear_terminal()

        # Mettre à jour le nombre d'allumettes restantes.
        matche_count -= choice

        if matche_count <= 0:
            # Annoncer la défaite du joueur qui doit prendre la dernière allumette.
            special_print(
                f"Le joueur {current_player.pseudo} a pris la dernière allumette. Le joueur {other_player.pseudo} a perdu !"
            )

        # Alterner les rôles des joueurs.
        temp = current_player
        current_player = other_player
        other_player = temp

        clear_terminal()

    # Afficher la victoire du joueur gagnant et mettre à jour les scores.
    game_tool.display_victory(current_player.pseudo, 1)
    if not current_player.is_bot:
        data.add_score_point(current_player.pseudo, "allumetes", 1)
    time.sleep(4)
    clear_terminal()
