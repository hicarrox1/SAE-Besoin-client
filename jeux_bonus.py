import toolbox
import data
from clear import clear
import time

def afficher_plateau(plateau):
    
    plateau_affichage = ""
    for i in range(len(plateau)):
        plateau_affichage += " | ".join(plateau[i])+"\n"
        if i != len(plateau)-1:
            plateau_affichage += "---  " * 7 +"\n"
    plateau_affichage += "\n"
    
    print(plateau_affichage)

def add_jeton(plateau:list, colonne: int, jeton: str):
    
    for i in range(len(plateau)):
        if plateau[i][colonne] == "🔘":
            ligne = i
    plateau[ligne][colonne] = jeton

    if verif_gagnant(plateau,jeton,colonne,ligne):
        return True
    return False

def verif_gagnant(plateau: list, jeton: str, colonne: int, ligne):

    for l in range(-1,2):
        for c in range(-1,2):

            if l == 0 and c == 0:
                pass
            else:
                cmpt = 1
                for i in range(1,4):
                    try:
                        if plateau[ligne+(i*l)][colonne+(i*c)] == jeton: cmpt += 1
                        if cmpt == 4: return True
                        
                    except:
                        pass
    return False

def launch(player_begin: int):

    game = True
    choix : int

    player_1 = data.get_name(player_begin)
    player_2 = data.get_name((player_begin+1)%2)
    current_player = player_1

    while game:

        plateau = [["🔘" for _ in range(7)] for _ in range(6)]
        afficher_plateau(plateau)

        numero_tour = 0
        gagnant = False
        while numero_tour <= 42 and not gagnant:
            numero_tour += 1
            jeton = "🔴" if current_player == player_1 else "🟡"
            colonne = 0
            while colonne < 1 or colonne > 7 or plateau[0][colonne-1] != "🔘":
                try:
                    colonne = int(input(f"à votre tour {current_player} choissisez une colonne : "))
                    clear(0)
                except ValueError:
                    clear(0)
            gagnant = add_jeton(plateau,colonne-1,jeton)

            clear(12) 
            afficher_plateau(plateau)

            if gagnant:
                
                clear(12)
                toolbox.affiche_victoire(current_player, 1)
                data.add_score(1,data.get_name_id(current_player),"bonus")
                time.sleep(4)
                clear(5)
    
            else:
                current_player = player_2 if current_player == player_1 else player_1
        
        if not gagnant:
            clear(12) 
            toolbox.afffichage_box("Match nul"," personne ne gagne de point")
            time.sleep(4)
            clear(5)

        print('voulez vous rejouer taper 0. Non 1. Oui')
        choix = int(input(""))

        time.sleep(1)
        clear(1)

        if choix == 1:
            game = True
        else:
            game = False