import random

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


def best_move(board: list, token: str) -> list[int]:
    # Définit l'adversaire
    adversaire = "🔴" if token == "🟡" else "🟡"

    token_positions: list =[]
    for col in range(7):
        for i in range(len(board)):
            if board[i][col] == "🔘":
                row = i
        token_positions.append([row,col])
    
    for token_position in token_positions:
        if check_if_win(board,token,token_position):
            return token_position
        
    for token_position in token_positions:
        if check_if_win(board,adversaire,token_position):
            return token_position
        
    return token_positions[random.randint(0,6)]


board=[["🔘","🔘","🔘","🔘","🔘","🔘","🔘"],
["🔘","🔘","🔘","🔘","🔘","🔘","🔘"],
["🔘","🔘","🔘","🔘","🔘","🔘","🔘"],
["🔘","🔘","🔘","🔘","🔘","🔘","🔘"],
["🔴","🔘","🔘","🔘","🔘","🔘","🔘"],
["🔴","🔘","🟡","🟡","🔘","🔘","🔘"]]

move = best_move(board,"🟡")
board[move[0]][move[1]] = "🟡"

print(move)
for i in board:
    for m in i:
        print(m, end="")
    print("", end="\n")

"""
# Parcourt toutes les cases pour trouver le meilleur coup
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                # Simule un coup pour le joueur
                if check_if_win(board, token, row, col):
                    return [row, col]

    # Bloquer un coup gagnant de l'adversaire
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                if check_if_win(board, adversaire, row, col):
                    return [row, col]

    possible = []

    # Si aucun coup gagnant ou de blocage, choisir une case libre
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                possible.append([row, col])

    if len(possible) >= 1:
        return possible[random.randint(0, len(possible) - 1)]
    return None  # Aucun coup possible (le plateau est plein)
"""