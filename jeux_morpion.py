import clear
import data
import time
import toolbox

def afficher_plateau(plateau):
    
    plateau_affichage = ""
    for i in range(len(plateau)):
        plateau_affichage += " | ".join(plateau[i])+"\n"
        if i != len(plateau)-1:
            plateau_affichage += "--- --- ---\n"
    plateau_affichage += "\n"
    
    toolbox.display_box("plateau",plateau_affichage, center_texte=True)


def verifier_gagnant(plateau, joueur):
    for i in range(3):
        if plateau[i][0] == plateau[i][1] == plateau[i][2] == joueur:
            return True
        if plateau[0][i] == plateau[1][i] == plateau[2][i] == joueur:
            return True
    if plateau[0][0] == plateau[1][1] == plateau[2][2] == joueur:
        return True
    if plateau[0][2] == plateau[1][1] == plateau[2][0] == joueur:
        return True
    return False

def morpion(player_begin: int):
    print("")
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    player_1 = data.get_name(player_begin)
    player_2 = data.get_name((player_begin+1)%2)
    current_player = player_1
    verif = True
    nb_tour = 1
    gagnant= False

    while nb_tour <= 9 and not gagnant:
        nb_tour += 1
        afficher_plateau(plateau)
        print(f"\n{current_player}, à vous de jouer !")
        verif = True
        while verif:
            taille = 1
            try:
                ligne = int(input("Entrez le numéro de ligne (1-3) : ")) - 1
                taille += 1
                colonne = int(input("Entrez le numéro de colonne (1-3) : ")) - 1
                taille += 1
                if ligne in range(3) and colonne in range(3):
                    if plateau[ligne][colonne] == " ":
                        clear.clear(14)
                        verif = False
                    else:
                        clear.clear(2)
                        print("Cette case est déjà prise, réessayez.")
                else:
                    clear.clear(2)
                    print("Les numéros doivent être entre 1 et 3.")
            except ValueError:
                clear.clear(taille)
                print("Veuillez entrer des nombres valides.")


        plateau[ligne][colonne] = 'X' if current_player == player_1 else "O"


        if verifier_gagnant(plateau, 'X' if current_player == player_1 else "O"):
            afficher_plateau(plateau)
            toolbox.display_victory(player_1, 1)
            data.add_score(1,data.get_name_id(current_player),"morpion")
            time.sleep(4)
            clear.clear(16)
            gagnant = True

        current_player = player_2 if current_player == player_1 else player_1
    
    if not gagnant:
        afficher_plateau(plateau)
        toolbox.display_box("Match nul"," personne ne gagne de point")
        time.sleep(4)
        clear.clear(16)