import menu
import game_tool
import filler_animation_tool
import clear
from constant import JOYSTICK, DONKEY_KONG, BEGIN_MESSAGE
import time

if __name__ == "__main__":
    # affiche un message d'avertisement pour le bon fonctionement
    game_tool.special_print(f"\n{BEGIN_MESSAGE}")

    # affiche un menu de chargement
    game_tool.display_box(
        text=JOYSTICK,
        center_texte=True,
        icon="🕹️ ",
        padding=0,
    )
    filler_animation_tool.slider(3, 36, "🕹️", "▪️", "▫️")
    clear.clear(1)
    clear.clear_terminal()

    # lance le menu
    menu.game()

    # affiche une image de fin pendant une seconde1

    clear.special_print(DONKEY_KONG)
    time.sleep(1)
    clear.clear_terminal()
