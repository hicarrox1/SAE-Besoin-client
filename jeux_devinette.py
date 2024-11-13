import toolbox
import data
from clear import clear
import time

def get_nombre_choisi(name_player_choose):
    number_choose = 0
    while number_choose < 1 or number_choose > 1000:
            number_choose = toolbox.demander_info_entier(f"{name_player_choose} veuillez choisir un nombre entre 1 et 1000 ? ", 0)
    return number_choose

def deviner_nombre(number_choose, name_player_guess):
    number_test = None
    cmpt_try = 0
    print("---------------------------")
    while number_test != number_choose:
        number_test = toolbox.demander_info_entier(f"{name_player_guess}, devinez le nombre : ", None)
        if number_test != None:
            cmpt_try += 1
            clear(0)
            if number_test == number_choose:
                print(f"Bravo {name_player_guess} vous avez trouvé en : {cmpt_try} essai")
                time.sleep(2)
                clear(0)
                return cmpt_try
            elif number_test < number_choose:
                print("Trop petit ↘️")
            else:
                print("Trop grand ↗️")
        
def launch(player_begin: int):

    game = True
    choix : int

    player_1 = data.get_name(player_begin)
    player_2 = data.get_name((player_begin+1)%2)

    player_1_cmpt = 0
    player_2_cmpt = 0

    while game:
        
        nombre_a_deviner = get_nombre_choisi(player_2)
        player_1_cmpt = deviner_nombre(nombre_a_deviner, player_1)
        
        nombre_a_deviner = get_nombre_choisi(player_1)
        player_2_cmpt = deviner_nombre(nombre_a_deviner, player_2)

        if player_1_cmpt < player_2_cmpt:
            name_player_win = player_1
        else:
            name_player_win = player_2

        if player_1_cmpt == player_2_cmpt:
            toolbox.afffichage_box("Match nul"," personne ne gagne de point")
            time.sleep(4)
            clear(4)
        else:
            toolbox.affiche_victoire(name_player_win,1)
            data.add_score(1,data.get_name_id(name_player_win),"devinette")
            time.sleep(2)
            clear(4)

        choix = toolbox.demander_info_entier('voulez vous rejouer taper 0. Non 1. Oui \n', 0)
        clear(0)
        time.sleep(1)
        

        if choix == 1:
            game = True
            current_player = player_2 if current_player == player_1 else player_1
        else:
            game = False