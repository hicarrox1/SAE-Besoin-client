import game_tool
import data
from clear import clear_terminal
import time
import random
from PlayerInfo import PlayerInfo


def best_move(board: list, token: str) -> list[int]:
    """
    Cette fonction analyse le plateau de jeu pour déterminer le meilleur coup à jouer.

    Arguments:
        board (list): Une liste 2D représentant le plateau de jeu.
        token (str): Le symbole du joueur ("🔴" ou "🟡") pour lequel trouver le meilleur coup.
    Retourne:
        int: La colonne du meilleur coup possible
    """
    # Définit l'adversaire
    adversaire: str = "🔴" if token == "🟡" else "🟡"
    bot_move: int
    find: bool = False

    # Cherche tout les position ou le bot peut jouer
    token_positions: list = []
    for col in range(7):
        for i in range(len(board)):
            if board[i][col] == "🔘":
                row = i
        token_positions.append([row, col])

    # Parcourt toutes les cases pour trouver le meilleur coup pour gagner
    for token_position in token_positions:
        if check_if_win(board, token, token_position):
            bot_move = token_position[1] + 1
            find = True

    # Si le bot ne peut pas gagner, il bloque l'adversaire
    if not find:
        for token_position in token_positions:
            if check_if_win(board, adversaire, token_position):
                bot_move = token_position[1] + 1
                find = True

    if not find:
        # Si aucun coup gagnant ou de blocage, choisir une case libre
        bot_move = random.randint(1, 7)

    return bot_move


def get_bot_move(bot_level: int, board: list, current_token: str) -> list[int]:
    """
    Détermine le coup à jouer pour le bot en fonction de son niveau de difficulté.

    Arguments:
        bot_level (int): Niveau de difficulté du bot (1, 2 ou 3).
        board (list): Une liste 2D représentant le plateau de jeu.
        current_token (str): Le symbole du joueur actuel ("🔴" ou "🟡").
    Returns:
        Int: La colonne où le bot va jouer.
    """
    bot_move: int = 1
    match bot_level:
        case 2:
            # Le bot de niveau 2 choisit un coup aléatoire ou expert de manière aléatoire.
            if (random.randint(1, 2)) == 2:
                bot_move = random.randint(1, 7)
            else:
                bot_move = best_move(board, current_token)
        case 3:
            # Le bot de niveau 3 choisit le meilleur coup possible.
            bot_move = best_move(board, current_token)
        case 1 | _:
            # Le bot de niveau 1 choisit un coup aléatoire.
            bot_move = random.randint(1, 7)
    return bot_move


def display_board(board: list):
    """
    Affiche l'état actuel du plateau de jeu.

    Le plateau est une grille 6x7 où chaque emplacement peut être vide ("🔘")
    ou occupé par un jeton ("🔴" ou "🟡"). La méthode formate et affiche la grille.

    Arguments:
        board (list): Une liste 2D représentant le plateau de jeu.
    """
    board_display: str = ""
    # Boucle pour formater l'affichage du plateau
    for i in range(len(board)):
        board_display += " | ".join(board[i]) + "\n"
        if i != len(board) - 1:
            board_display += "-----" * 7 + "\n"
    board_display += "\n"

    # Affichage du plateau dans une boîte centrée
    game_tool.display_box(titre=" ", text=board_display, center_texte=True, padding=1)


def add_token(board: list, column: int, token: str) -> bool:
    """
    Ajoute un jeton dans une colonne donnée.

    Le jeton est inséré à la position la plus basse disponible dans la colonne choisie.
    La fonction vérifie si ce mouvement permet de gagner la partie.

    Arguments:
        board (list): Une liste 2D représentant le plateau de jeu.
        column (int): L'indice de la colonne (0-indexée) où insérer le jeton.
        jeton (str): Le symbole du joueur ("🔴" ou "🟡").

    Retourne:
        bool: True si le joueur a gagné après ce coup, False sinon.
    """
    row: int
    # Recherche de la première ligne vide dans la colonne
    for i in range(len(board)):
        if board[i][column] == "🔘":
            row = i
    # Placement du jeton à la position trouvée
    board[row][column] = token

    ## Vérifie si le joueur a gagné après ce coup
    return check_if_win(board, token, [row, column])


def check_if_win(board: list, token: str, token_position: list) -> bool:
    """
    Vérifie si un joueur a gagné la partie.

    Analyse les directions (horizontale, verticale, et diagonales) pour détecter une série de 4 jetons alignés.

    Arguments:
        board (list): Une liste 2D représentant le plateau de jeu.
        token (str): Le symbole du joueur à vérifier ("🔴" ou "🟡").
        pos (list): La position [ligne, colonne] où le dernier jeton a été ajouté.

    Retourne:
        bool: True si le joueur a une ligne de 4 jetons ou plus, False sinon.
    """
    win: bool = False
    total_neighbors: int = 1
    directions: list = [
        [(0, 1), (0, -1)],  # Vérification horizontale
        [(1, 0), (-1, 0)],  # Vérification verticale
        [(1, 1), (-1, -1)],  # Vérification diagonale montante
        [(1, -1), (-1, 1)],  # Vérification diagonale descendante
    ]
    current_pos: list

    # Vérification dans toutes les directions possibles
    for direction in directions:
        for dx, dy in direction:
            current_pos = [token_position[0], token_position[1]]
            try:
                # Exploration dans la direction actuelle
                while (
                    board[current_pos[0] + dx][current_pos[1] + dy] == token
                    and (current_pos[0] + dx) >= 0
                    and (current_pos[1] + dy) >= 0
                ):
                    total_neighbors += 1
                    current_pos[0] = current_pos[0] + dx
                    current_pos[1] = current_pos[1] + dy
            except:
                pass
        if total_neighbors >= 4:
            win = True
        total_neighbors = 1

    return win


def launch(players: list[PlayerInfo]):
    """
    Lance une partie de Puissance 4 entre deux joueurs.

    Les joueurs placent tour à tour leur jeton ("🔴" ou "🟡") sur une grille de 6x7.
    La partie se termine lorsqu'un joueur aligne 4 jetons ou lorsque toutes les cases sont remplies.

    Arguments:
        players (list): Une liste contenant les noms des deux joueurs.
    """
    player_1: PlayerInfo = players[0]
    player_2: PlayerInfo = players[1]
    current_player: PlayerInfo = player_1
    round_number: int = 0
    winner: bool = False
    token: str
    column: int

    # Initialisation du plateau avec des emplacements vides
    board: list = [["🔘" for _ in range(7)] for _ in range(6)]
    display_board(board)

    # Boucle principale du jeu
    while round_number <= 42 and not winner:
        round_number += 1
        token = "🔴" if current_player == player_1 else "🟡"
        column = 0

        if not current_player.is_bot:
            # Demande de la colonne pour placer le jeton, vérifie sa validité
            while column < 1 or column > 7 or board[0][column - 1] != "🔘":
                column = game_tool.ask_int(
                    f"à votre tour {current_player.pseudo} choissisez une colonne : ", 0
                )
        else:
            # Le bot choisit une colonne en fonction de son niveau de difficulté
            column = get_bot_move(current_player.bot_level, board, token)

        # Ajout du jeton et vérification de la victoire
        winner = add_token(board, column - 1, token)

        # Efface l'écran et affiche le plateau après le coup
        clear_terminal()
        display_board(board)

        # Si un joueur gagne, affiche un message de victoire
        if winner:
            game_tool.display_victory(current_player.pseudo, 1)
            if not current_player.is_bot:
                data.add_score_point(current_player.pseudo, "bonus", 1)
            time.sleep(4)
            clear_terminal()

        else:
            # Passe au joueur suivant
            current_player = player_2 if current_player == player_1 else player_1

    # Si la partie se termine sans gagnant, affiche un message de match nul
    if not winner:
        clear_terminal()
        game_tool.display_box("Match nul", " personne ne gagne de point")
        time.sleep(4)
        clear_terminal()
