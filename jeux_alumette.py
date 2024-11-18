import toolbox
from clear import clear, clear_terminal, special_print
import time
import data


def afficher_allumettes(allumettes):
    toolbox.display_box(
        texte=f"Nombre d'allumettes restantes : {allumettes}\n"
        + "Allumettes : \n"
        + "🔥" * allumettes,
        padding=1,
        center_texte=True,
    )


def jeu_allumettes(players: list):
    current_player: str
    other_player: str
    matches_count: int = 21
    choice: int
    temp: str

    current_player = players[0]
    other_player = players[1]

    while matches_count > 0:
        afficher_allumettes(matches_count)

        choice = 0
        while choice != 1 and choice != 2 and choice != 3:
            choice = toolbox.ask_int(
                f"Joueur {current_player}, combien d'allumettes souhaitez-vous retirer ? (1, 2 ou 3) : ",
                0,
            )
            clear(0)

        matches_count -= choice

        if matches_count <= 0:
            special_print(
                f"Le joueur {current_player} a pris la dernière allumette. Le joueur {other_player} a perdu !"
            )

        temp = current_player
        current_player = other_player
        other_player = temp

        clear_terminal()

    toolbox.display_victory(current_player, 3)
    data.add_score_point(current_player, "allumetes", 3)
    time.sleep(4)
    clear_terminal()
