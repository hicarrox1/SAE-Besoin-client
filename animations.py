import display_tool
import time
import clear


def start_game_animation(player_1_icon: str, player_2_icon: str):
    """
    Animation de début de jeu.

    Arguments :
        player_1_icon (str) : L'icône du joueur 1.
        player_2_icon (str) : L'icône du joueur 2.
    """
    # boucle de l'animation
    for i in range(18):
        text = (
            f"{player_1_icon}"
            + (9 - i) * " "
            + " ⚔️  "
            + (9 - i) * " "
            + f"{player_2_icon}"
        )
        display_tool.display_box(text=text, center_texte=True, padding=1)

        # pause de 0.1 seconde entre chaque frame
        time.sleep(0.1)

        clear.clear_terminal()
