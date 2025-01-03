import clear
import data
import time
import game_tool
import bot


def get_bot_move(bot_level: int, board: list, current_token: str) -> list[int]:
    bot_move: list[int] = [0, 0]
    match bot_level:
        case 2:
            pass
        case 3:
            pass
        case 1 | _:
            bot_move = [bot.random_bot([1, 3]), bot.random_bot([1, 3])]
    return bot_move


def display_board(board: list):
    """
    Affiche l'état actuel du plateau de jeu.

    Le plateau est représenté sous forme de grille avec des lignes et des colonnes séparées par des symboles.
    La méthode utilise une boîte pour afficher visuellement l'état du jeu.

    Arguments:
        board (list): Une liste 2D représentant le plateau de jeu, où chaque élément est " ", "X" ou "O".
    """
    # Construction de la représentation visuelle du plateau
    plateau_affichage: str = ""
    for i in range(len(board)):
        plateau_affichage += " | ".join(board[i]) + "\n"
        if i != len(board) - 1:
            plateau_affichage += "--- --- ---\n"
    plateau_affichage += "\n"

    # Affichage du plateau dans une boîte centrée
    game_tool.display_box("plateau", plateau_affichage, center_texte=True)


def check_win(board: list, token: str) -> bool:
    """
    Vérifie si un joueur a gagné la partie.

    Cette fonction analyse les lignes, colonnes et diagonales pour détecter une combinaison gagnante.

    Arguments:
        board (list): Une liste 2D représentant le plateau de jeu.
        joueur (str): Le symbole du joueur ("X" ou "O") à vérifier.

    Retourne:
        bool: True si le joueur a gagné, False sinon.
    """
    # Vérification des lignes et colonnes
    win: bool = False
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == token:
            win = True
        if board[0][i] == board[1][i] == board[2][i] == token:
            win = True
    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] == token:
        win = True
    if board[0][2] == board[1][1] == board[2][0] == token:
        win = True
    return win


def morpion(players: list):
    """
    Lance une partie de morpion entre deux joueurs.

    Les joueurs placent tour à tour leur symbole ("X" ou "O") sur une grille de 3x3.
    La partie se termine lorsqu'un joueur aligne 3 symboles ou qu'il n'y a plus de cases disponibles.

    Arguments:
        players (list): Une liste contenant les noms des deux joueurs.
    """
    # Initialisation du plateau de jeu et des variables de suivi
    print("")
    board: list = [[" " for _ in range(3)] for _ in range(3)]
    player_1: str = players[0]
    player_2: str = players[1]
    current_player: str = player_1
    input_check: bool
    round_number: int = 1
    have_winner: bool = False
    row: int
    column: int

    # Boucle principale du jeu
    while round_number <= 9 and not have_winner:
        round_number += 1
        display_board(board)

        # Saisie et validation des coordonnées
        input_check = True
        while input_check:
            row = 0
            while row != 1 and row != 2 and row != 3:
                row = int(game_tool.ask_int("Entrez le numéro de ligne (1-3) : ", 0))
            column = 0
            while column != 1 and column != 2 and column != 3:
                column = int(
                    game_tool.ask_int("Entrez le numéro de colonne (1-3) : ", 0)
                )
            row -= 1
            column -= 1

            if board[row][column] == " ":
                clear.clear_terminal()
                input_check = False

        # Mise à jour du plateau
        board[row][column] = "X" if current_player == player_1 else "O"

        # Vérification de la victoire
        if check_win(board, "X" if current_player == player_1 else "O"):
            display_board(board)
            game_tool.display_victory(player_1, 1)
            data.add_score_point(current_player, "morpion", 1)
            time.sleep(4)
            clear.clear_terminal()
            have_winner = True

        # Changement de joueur
        current_player = player_2 if current_player == player_1 else player_1

    # Match nul si aucun gagnant après 9 tours
    if not have_winner:
        display_board(board)
        game_tool.display_box("Match nul", " personne ne gagne de point")
        time.sleep(4)
        clear.clear_terminal()
