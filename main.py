import menu
import toolbox
import filler_animation
import clear
from constant import JOYSTICK, DONKEY_KONG

if __name__ == "__main__":
    toolbox.display_box(
        texte=JOYSTICK,
        center_texte=True,
        icon="🕹️ ",
        padding=0,
    )

    filler_animation.slider(3, 36, "🕹️", "▪️", "▫️")
    clear.clear(1)
    clear.clear_terminal()
    
    menu.game()

    print(DONKEY_KONG)
