import game_tool
from clear import clear, clear_terminal, special_print
import time
import data


def afficher_allumettes(allumettes: int):
    """
    Affiche le nombre d'allumettes restantes avec une représentation visuelle.

    Arguments :
        allumettes (int): Nombre d'allumettes restantes dans le jeu.
    """
    # Affichage des allumettes restantes avec un visuel utilisant des emojis.
    game_tool.display_box(
        text=f"Nombre d'allumettes restantes : {allumettes}\n"
        + "Allumettes : \n"
        + "🔥" * allumettes,
        padding=1,
        center_texte=True,
    )


def jeu_allumettes(players: list):
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
    matches_count: int = 21
    choice: int
    temp: str

    # Définition des joueurs en fonction de l'ordre donné.
    current_player = players[0]
    other_player = players[1]

    while matches_count > 0:
        # Afficher l'état actuel des allumettes.
        afficher_allumettes(matches_count)

        choice = 0
        while choice != 1 and choice != 2 and choice != 3:
            # Demander au joueur actuel combien d'allumettes retirer.
            choice = game_tool.ask_int(
                f"Joueur {current_player}, combien d'allumettes souhaitez-vous retirer ? (1, 2 ou 3) : ",
                0,
            )
            clear(0)

        # Mettre à jour le nombre d'allumettes restantes.
        matches_count -= choice

        if matches_count <= 0:
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
