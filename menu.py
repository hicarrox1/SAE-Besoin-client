import toolbox
import clear
import jeux_morpion
import jeux_devinette
import jeux_bonus
import jeux_alumette


def game():
    choix: int
    run: bool = True

    while run:
        toolbox.display_box(
            "",
            "Choisissez ce que vous voulez faire\n1. devinette   2. allumettes\n3. morpion     4. bonus     \n5.Changer d'icon\n6. afficher les scores\n0.Quitter",
            icon="🎮",
            padding=1,
            center_texte=True,
        )

        choix = toolbox.ask_int("choix: ", 0)

        clear.clear_terminal()

        match choix:
            case 1:
                toolbox.launch_game("devinette", jeux_devinette.launch)
            case 2:
                toolbox.launch_game("allumetes", jeux_alumette.jeu_allumettes_2_joueurs)
            case 3:
                toolbox.launch_game("morpion", jeux_morpion.morpion)
            case 4:
                toolbox.launch_game("bonus", jeux_bonus.launch)
            case 5:
                toolbox.change_icon()
            case 6:
                toolbox.game_ranking()
            case 0:
                run = False
            case _:
                run = False
