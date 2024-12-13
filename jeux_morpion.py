import clear
import data
import time
import game_tool


def afficher_plateau(plateau: list):
    """
    Affiche l'état actuel du plateau de jeu.

    Le plateau est représenté sous forme de grille avec des lignes et des colonnes séparées par des symboles. 
    La méthode utilise une boîte pour afficher visuellement l'état du jeu.

    Arguments:
        plateau (list): Une liste 2D représentant le plateau de jeu, où chaque élément est " ", "X" ou "O".
    """
    # Construction de la représentation visuelle du plateau
    plateau_affichage: str = ""
    for i in range(len(plateau)):
        plateau_affichage += " | ".join(plateau[i]) + "\n"
        if i != len(plateau) - 1:
            plateau_affichage += "--- --- ---\n"
    plateau_affichage += "\n"

    # Affichage du plateau dans une boîte centrée
    game_tool.display_box("plateau", plateau_affichage, center_texte=True)


def verifier_gagnant(plateau: list, joueur: str) -> bool:
    """
    Vérifie si un joueur a gagné la partie.

    Cette fonction analyse les lignes, colonnes et diagonales pour détecter une combinaison gagnante.

    Arguments:
        plateau (list): Une liste 2D représentant le plateau de jeu.
        joueur (str): Le symbole du joueur ("X" ou "O") à vérifier.

    Retourne:
        bool: True si le joueur a gagné, False sinon.
    """
    # Vérification des lignes et colonnes
    win: bool = False
    for i in range(3):
        if plateau[i][0] == plateau[i][1] == plateau[i][2] == joueur:
            win = True
        if plateau[0][i] == plateau[1][i] == plateau[2][i] == joueur:
            win = True
    # Vérification des diagonales
    if plateau[0][0] == plateau[1][1] == plateau[2][2] == joueur:
        win = True
    if plateau[0][2] == plateau[1][1] == plateau[2][0] == joueur:
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
    plateau: list = [[" " for _ in range(3)] for _ in range(3)]
    player_1: str = players[0]
    player_2: str = players[1]
    current_player: str = player_1
    verif: bool = True
    nb_tour: int = 1
    gagnant:bool = False
    ligne: int
    colonne: int

    # Boucle principale du jeu
    while nb_tour <= 9 and not gagnant:
        nb_tour += 1
        afficher_plateau(plateau)

        # Saisie et validation des coordonnées
        verif = True
        while verif:
            ligne = 0
            while ligne != 1 and ligne != 2 and ligne != 3:
                ligne = int(game_tool.ask_int("Entrez le numéro de ligne (1-3) : ", 0))
            colonne = 0
            while colonne != 1 and colonne != 2 and colonne != 3:
                colonne = int(
                    game_tool.ask_int("Entrez le numéro de colonne (1-3) : ", 0)
                )
            ligne -= 1
            colonne -= 1

            if plateau[ligne][colonne] == " ":
                clear.clear_terminal()
                verif = False

        # Mise à jour du plateau
        plateau[ligne][colonne] = "X" if current_player == player_1 else "O"

        # Vérification de la victoire
        if verifier_gagnant(plateau, "X" if current_player == player_1 else "O"):
            afficher_plateau(plateau)
            game_tool.display_victory(player_1, 1)
            data.add_score_point(current_player, "morpion", 1)
            time.sleep(4)
            clear.clear_terminal()
            gagnant = True

        # Changement de joueur
        current_player = player_2 if current_player == player_1 else player_1

    # Match nul si aucun gagnant après 9 tours
    if not gagnant:
        afficher_plateau(plateau)
        game_tool.display_box("Match nul", " personne ne gagne de point")
        time.sleep(4)
        clear.clear_terminal()
