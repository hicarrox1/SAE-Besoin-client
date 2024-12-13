import game_tool
import data
from clear import clear_terminal
import time


def afficher_plateau(plateau: list):
    """
    Affiche l'état actuel du plateau de jeu.

    Le plateau est une grille 6x7 où chaque emplacement peut être vide ("🔘") 
    ou occupé par un jeton ("🔴" ou "🟡"). La méthode formate et affiche la grille.

    Arguments:
        plateau (list): Une liste 2D représentant le plateau de jeu.
    """
    plateau_affichage: str = ""
    # Boucle pour formater l'affichage du plateau
    for i in range(len(plateau)):
        plateau_affichage += " | ".join(plateau[i]) + "\n"
        if i != len(plateau) - 1:
            plateau_affichage += "-----" * 7 + "\n"
    plateau_affichage += "\n"

    # Affichage du plateau dans une boîte centrée
    game_tool.display_box(
        titre=" ", text=plateau_affichage, center_texte=True, padding=1
    )


def add_jeton(plateau: list, colonne: int, jeton: str) -> bool:
    """
    Ajoute un jeton dans une colonne donnée.

    Le jeton est inséré à la position la plus basse disponible dans la colonne choisie.
    La fonction vérifie si ce mouvement permet de gagner la partie.

    Arguments:
        plateau (list): Une liste 2D représentant le plateau de jeu.
        colonne (int): L'indice de la colonne (0-indexée) où insérer le jeton.
        jeton (str): Le symbole du joueur ("🔴" ou "🟡").

    Retourne:
        bool: True si le joueur a gagné après ce coup, False sinon.
    """
    ligne: int
    # Recherche de la première ligne vide dans la colonne
    for i in range(len(plateau)):
        if plateau[i][colonne] == "🔘":
            ligne = i
    # Placement du jeton à la position trouvée
    plateau[ligne][colonne] = jeton

    ## Vérifie si le joueur a gagné après ce coup
    return check_if_win(plateau, jeton, [ligne, colonne])


def check_if_win(plateau: list, jeton: str, pos: list) -> bool:
    """
    Vérifie si un joueur a gagné la partie.

    Analyse les directions (horizontale, verticale, et diagonales) pour détecter une série de 4 jetons alignés.

    Arguments:
        plateau (list): Une liste 2D représentant le plateau de jeu.
        jeton (str): Le symbole du joueur à vérifier ("🔴" ou "🟡").
        pos (list): La position [ligne, colonne] où le dernier jeton a été ajouté.

    Retourne:
        bool: True si le joueur a une ligne de 4 jetons ou plus, False sinon.
    """
    win: bool = False
    total_voisins: int = 1
    directions: list = [
        [(0, 1), (0, -1)], # Vérification horizontale
        [(1, 0), (-1, 0)], # Vérification verticale
        [(1, 1), (-1, -1)], # Vérification diagonale montante
        [(1, -1), (-1, 1)], # Vérification diagonale descendante    
    ]
    current_pos: list

    # Vérification dans toutes les directions possibles
    for direction in directions:
        for dx, dy in direction:
            current_pos = [pos[0], pos[1]]
            try:
                # Exploration dans la direction actuelle
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
            win = True
        total_voisins = 1

    return win


def launch(players: list):
    """
    Lance une partie de Puissance 4 entre deux joueurs.

    Les joueurs placent tour à tour leur jeton ("🔴" ou "🟡") sur une grille de 6x7.
    La partie se termine lorsqu'un joueur aligne 4 jetons ou lorsque toutes les cases sont remplies.

    Arguments:
        players (list): Une liste contenant les noms des deux joueurs.
    """
    player_1: str = players[0]
    player_2: str = players[1]
    current_player: str = player_1
    numero_tour: int = 0
    gagnant: bool = False
    jeton: str
    colonne: int

    # Initialisation du plateau avec des emplacements vides
    plateau: list = [["🔘" for _ in range(7)] for _ in range(6)]
    afficher_plateau(plateau)

    # Boucle principale du jeu
    while numero_tour <= 42 and not gagnant:
        numero_tour += 1
        jeton = "🔴" if current_player == player_1 else "🟡"
        colonne = 0

        # Demande de la colonne pour placer le jeton, vérifie sa validité
        while colonne < 1 or colonne > 7 or plateau[0][colonne - 1] != "🔘":
            colonne = game_tool.ask_int(
                f"à votre tour {current_player} choissisez une colonne : ", 0
            )

        # Ajout du jeton et vérification de la victoire
        gagnant = add_jeton(plateau, colonne - 1, jeton)

        # Efface l'écran et affiche le plateau après le coup
        clear_terminal()
        afficher_plateau(plateau)

        # Si un joueur gagne, affiche un message de victoire
        if gagnant:
            game_tool.display_victory(current_player, 1)
            data.add_score_point(current_player, "bonus", 1)
            time.sleep(4)
            clear_terminal()

        else:
            # Passe au joueur suivant
            current_player = player_2 if current_player == player_1 else player_1

    # Si la partie se termine sans gagnant, affiche un message de match nul
    if not gagnant:
        clear_terminal()
        game_tool.display_box("Match nul", " personne ne gagne de point")
        time.sleep(4)
        clear_terminal()
