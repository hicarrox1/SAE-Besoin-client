import toolbox
import jeux_test
import clear
import jeux_morpion
import jeux_devinette
import jeux_bonus
from change_name import change_name

if __name__ == "__main__":
    choix: int
    run: bool = True

    while run:
        
        toolbox.afficher_all_score()

        print("🎮 -------------- Menu ---------------🎮")
        print("|  Choisissez ce que vous voulez faire  |")
        print("| 1. jeux devinette   2. jeux allumettes|")
        print("| 3. jeux morpion     4. jeux bonus     |")
        print("|           5.Changer de nom            |")
        print("|              0.Quitter                |")
        print("🎮 -----------------------------------🎮\n")
        
        choix = toolbox.demander_info_entier("choix: ", 0)

        clear.clear(23)

        match choix:
            case 1:
                toolbox.launch_game("devinette", jeux_devinette.launch)
            case 2:
                toolbox.launch_game("allumetes", jeux_test.launch)
            case 3:
                toolbox.launch_game("morpion", jeux_morpion.morpion)
            case 4:
                toolbox.launch_game("bonus", jeux_bonus.launch)
            case 5:
                change_name()
            case 0:
                run = False
            case _:
                run = False
