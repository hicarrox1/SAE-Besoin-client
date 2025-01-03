import game_tool
import clear
import jeux_morpion
import jeux_devinette
import jeux_bonus
import jeux_alumette
import menu_score
import menu_icon


def game():
    """
    fonction principal du gestionaire de jeux
    """
    choix: int
    run: bool = True

    while run:
        game_tool.display_box(
            "",
            "Choisissez ce que vous voulez faire\n1. devinette   2. allumettes\n3. morpion     4. bonus     \n5.Changer d'icon\n6. afficher les scores\n0.Quitter",
            icon="🎮",
            padding=1,
            center_texte=True,
        )

        # demande à l'utilisateur ce qu'il veut faire
        choix = game_tool.ask_int("choix: ", 0)

        clear.clear_terminal()

        # en fonction de choix lance les fonctions associer
        match choix:
            case 1:
                game_tool.launch_game("devinette", jeux_devinette.launch)
            case 2:
                game_tool.launch_game("allumetes", jeux_alumette.matche_game)
            case 3:
                game_tool.launch_game("morpion", jeux_morpion.morpion)
            case 4:
                game_tool.launch_game("bonus", jeux_bonus.launch)
            case 5:
                menu_icon.change_icon_menu()
            case 6:
                menu_score.manage_score()
            case 0:
                run = False
            case _:
                run = False
