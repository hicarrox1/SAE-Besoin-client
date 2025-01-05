import display_tool
import time
import clear

for i in range(18):
    text = "joueur 1" + (9 - i) * " " + " ⚔️   " + (9 - i) * " " + "joueur 2"
    display_tool.display_box(text=text, center_texte=True, padding=1)

    time.sleep(0.1)

    clear.clear_terminal()