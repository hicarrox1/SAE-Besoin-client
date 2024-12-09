import menu
import toolbox
import filler_animation
import clear
from constant import JOYSTICK, DONKEY_KONG, BEGIN_MESSAGE
import time

if __name__ == "__main__":

    toolbox.special_print(f"\n{BEGIN_MESSAGE}")

    toolbox.display_box(
        text=JOYSTICK,
        center_texte=True,
        icon="🕹️ ",
        padding=0,
    )

    filler_animation.slider(3, 36, "🕹️", "▪️", "▫️")
    clear.clear(1)
    clear.clear_terminal()

    menu.game()

    clear.special_print(DONKEY_KONG)
    time.sleep(1)
    clear.clear_terminal()
