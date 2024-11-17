import menu
import toolbox
import filler_animation
import clear
from constant import JOYSTICK, DONKEY_KONG

if __name__ == "__main__":
    toolbox.display_box(
        texte=JOYSTICK,
        center_texte=True,
        icon="🕹️",
        padding=0,
    )

    filler_animation.launch_load_anim(3, 36, "🕹️", "▪️", "▫️")

    clear.clear(19)

    menu.game()

    print(DONKEY_KONG)
