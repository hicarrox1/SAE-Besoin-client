"""import display_tool
import time
import clear

for i in range(20):
    text = "joueur 1" + (10 - i) * " " + " ⚔️  " + (10 - i) * " " + "joueur 2"
    display_tool.display_box(text=text, center_texte=True, padding=1)

    time.sleep(0.1)

    clear.clear_terminal()
"""

import random


def display(board: list):
    for rowi in board:
        for columni in rowi:
            print(f"{columni} |", end="")
        print("\n", end="")


def joue(row, col, bo, token):
    bo[row][col] = token


def check_winner(board: list, token: str) -> bool:
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


def meilleur_coup(plateau: list, token: str) -> list[int]:
    # Définit l'adversaire
    adversaire = "X" if token == "O" else "O"

    # Parcourt toutes les cases pour trouver le meilleur coup
    for row in range(3):
        for col in range(3):
            if plateau[row][col] == " ":
                # Simule un coup pour le joueur
                plateau[row][col] = token
                if check_winner(plateau, token):
                    plateau[row][col] = " "  # Annule le coup
                    return [row, col]
                plateau[row][col] = " "  # Annule le coup

    # Bloquer un coup gagnant de l'adversaire
    for row in range(3):
        for col in range(3):
            if plateau[row][col] == " ":
                # Simule un coup pour l'adversaire
                plateau[row][col] = adversaire
                if check_winner(plateau, adversaire):
                    plateau[row][col] = " "  # Annule le coup
                    return [row, col]
                plateau[row][col] = " "  # Annule le coup

    possible = []

    # Si aucun coup gagnant ou de blocage, choisir une case libre
    for row in range(3):
        for col in range(3):
            if plateau[row][col] == " ":
                possible.append([row, col])

    if len(possible) >= 1:
        return possible[random.randint(0, len(possible) - 1)]
    return None  # Aucun coup possible (le plateau est plein)


plateau = [["O", " ", " "], ["O", " ", " "], ["X", " ", " "]]
column = 1
row = 2


display(plateau)
print("-----------------------------------")
pos = meilleur_coup(plateau, "X")
joue(pos[0], pos[1], plateau, "X")
display(plateau)
