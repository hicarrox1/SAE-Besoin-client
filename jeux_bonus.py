import toolbox
import data
from clear import clear_terminal
import time


def afficher_plateau(plateau):
    plateau_affichage = ""
    for i in range(len(plateau)):
        plateau_affichage += " | ".join(plateau[i]) + "\n"
        if i != len(plateau) - 1:
            plateau_affichage += "-----" * 7 + "\n"
    plateau_affichage += "\n"

    toolbox.display_box(
        titre=" ", texte=plateau_affichage, center_texte=True, padding=1
    )


def add_jeton(plateau: list, colonne: int, jeton: str):
    ligne: int
    for i in range(len(plateau)):
        if plateau[i][colonne] == "🔘":
            ligne = i
    plateau[ligne][colonne] = jeton
    if check_if_win(plateau, jeton, [ligne, colonne]):
        return True
    return False


def check_if_win(plateau: list, jeton: str, pos: list) -> bool:
    total_voisins = 1
    directions = [
        [(0, 1), (0, -1)],
        [(1, 0), (-1, 0)],
        [(1, 1), (-1, -1)],
        [(1, -1), (-1, 1)],
    ]
    dx = 0
    dy = 0

    for direction in directions:
        for dx, dy in direction:
            current_pos = [pos[0], pos[1]]
            try:
                while (
                    plateau[current_pos[0] + dx][current_pos[1] + dy] == jeton
                    and (current_pos[0] + dx) >= 0
                    and (current_pos[1] + dy) >= 0
                ):
                    total_voisins += 1
                    current_pos[0] = current_pos[0] + dx
                    current_pos[1] = current_pos[1] + dy
            except:
                pass
        if total_voisins >= 4:
            return True
        total_voisins = 1

    return False


def launch(players: list):
    player_1 = players[0]
    player_2 = players[1]
    current_player = player_1

    plateau = [["🔘" for _ in range(7)] for _ in range(6)]
    afficher_plateau(plateau)

    numero_tour = 0
    gagnant = False
    while numero_tour <= 42 and not gagnant:
        numero_tour += 1
        jeton = "🔴" if current_player == player_1 else "🟡"
        colonne = 0
        while colonne < 1 or colonne > 7 or plateau[0][colonne - 1] != "🔘":
            colonne = toolbox.ask_int(
                f"à votre tour {current_player} choissisez une colonne : ", 0
            )
        gagnant = add_jeton(plateau, colonne - 1, jeton)
        clear_terminal()
        afficher_plateau(plateau)

        if gagnant:
            toolbox.display_victory(current_player, 1)
            data.add_score_point(current_player, "bonus", 1)
            time.sleep(4)
            clear_terminal()

        else:
            current_player = player_2 if current_player == player_1 else player_1

    if not gagnant:
        clear_terminal()
        toolbox.display_box("Match nul", " personne ne gagne de point")
        time.sleep(4)
        clear_terminal()
