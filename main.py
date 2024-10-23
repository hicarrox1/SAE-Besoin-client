import toolbox


if __name__ == "__main__":

    choix: int
    run: bool = True

    while run:

        print("bonjour voici score precedent")
        toolbox.afficher_score()

        print("\n🎮 --------------- Menu ---------------🎮\n|  Choisissez ce que vous voulez faire  |")
        print("| 1. jeux devinette", end= " ")
        print("  2. jeux allumettes|")
        print("| 3. jeux morpion ", end= " ")
        print("   4. jeux bonus     |")
        print("|              0.Quitter                |")
        print("🎮 ------------------------------------🎮")

        run = False
        #choix = int(input("choix: "))

        """match choix:

            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 0:
                run = False
            case _:
                run = False"""

    