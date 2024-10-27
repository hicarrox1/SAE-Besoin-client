import sys
import toolbox
import clear
import time


def get_view_level(current_level: int, max_level: int):
    return "💣" + current_level * "🔴" + (max_level - current_level) * "🟢"

print()

def launch(joueur: int):
    max_level = 10

    level = 0
    user_input = -1

    print(get_view_level(level, max_level))
    user_input = input("Entrez quelque chose : ")

    if user_input != "5":
        level += 1

    while user_input != "5" and level < max_level:
        # Remplacer l'input avec une nouvelle
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[F")
        print(get_view_level(level, max_level))
        sys.stdout.write("\r")  # Retour au début de la ligne
        sys.stdout.write("Entrez quelque chose :    ")
        sys.stdout.write("\033[3D")
        sys.stdout.flush()
        user_input = input("")
        level += 1

    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    print(get_view_level(level, max_level))

    clear.clear(1)

    if level < max_level:
        toolbox.affiche_victoire(1, "hicarrox")
    else:
        toolbox.afffichage_box(titre="Defaite", texte=" Vous avez perdu", icon="⚫")

    time.sleep(3)
    clear.clear(5)
