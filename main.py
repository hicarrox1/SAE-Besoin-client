import toolbox
import jeux_test
import clear

if __name__ == "__main__":
    choix: int
    run: bool = True

    while run:
        print("\n🎮 -------------- Menu ---------------🎮")
        print("|  Choisissez ce que vous voulez faire  |")
        print("| 1. jeux devinette   2. jeux allumettes|")
        print("| 3. jeux morpion     4. jeux bonus     |")
        print("|              0.Quitter                |")
        print("🎮 -----------------------------------🎮\n")

        choix = int(input("choix: "))
        clear.clear(8)

        match choix:
            case 1:
                toolbox.launch_game("devinette", jeux_test.launch)
            case 2:
                toolbox.launch_game("allumetes", jeux_test.launch)
            case 3:
                toolbox.launch_game("morpion", jeux_test.launch)
            case 4:
                toolbox.launch_game("bonus", jeux_test.launch)
            case 0:
                run = False
            case _:
                run = False
